import ast
from datetime import datetime, timedelta, timezone # Added timezone

from agents.polymarket.polymarket import Polymarket
from agents.connectors.news import News
from agents.utils.objects import SimpleMarket, ExpiringMarketReportItem, Article # Assuming Article is needed for news_articles type hint

class ExpiringMarketsReporter:
    def __init__(self, days_to_expiration_threshold: int = 35):
        self.polymarket_client = Polymarket()
        self.news_client = News()
        self.days_to_expiration_threshold = days_to_expiration_threshold
        # Note: POLYGON_WALLET_PRIVATE_KEY and NEWSAPI_API_KEY environment variables
        # must be set for Polymarket and News clients to work.

    def _parse_outcome_prices(self, outcome_prices_str: str) -> list[float]:
        """Safely parses the outcome_prices string into a list of floats."""
        try:
            prices = ast.literal_eval(outcome_prices_str)
            if isinstance(prices, list) and all(isinstance(p, (int, float)) for p in prices):
                return [float(p) for p in prices]
        except (ValueError, SyntaxError) as e:
            print(f"Error parsing outcome_prices: {outcome_prices_str}, Error: {e}")
        return []

    def _fetch_news_for_market(self, market_question: str) -> list[Article]:
        """Fetches news articles for a given market question."""
        try:
            # Using get_articles_for_cli_keywords as it seems more generic,
            # and get_articles_for_options expected a list for market_options.
            # The news_client.get_articles_for_options might be more suitable if we adjust its call signature
            # or if market_question is a comma-separated list of keywords.
            # For now, we'll use the market question as a single keyword phrase.
            articles = self.news_client.get_articles_for_cli_keywords(keywords=market_question)
            return articles # This returns a list[Article] as per News.get_articles_for_cli_keywords
        except Exception as e:
            print(f"Error fetching news for '{market_question}': {e}")
        return []

    def check_and_report_expiring_markets(self):
        """
        Fetches markets, identifies those expiring within the threshold,
        gathers related data, and prints a report to the console.
        """
        print("Checking for expiring markets...")
        expiring_markets_reports: list[ExpiringMarketReportItem] = []

        try:
            all_markets: list[SimpleMarket] = self.polymarket_client.get_all_markets()
        except Exception as e:
            print(f"Error fetching markets from Polymarket: {e}")
            return

        if not all_markets:
            print("No markets found.")
            return

        now = datetime.now(timezone.utc) # Changed to offset-aware UTC time

        for market in all_markets:
            if not market.active:
                continue

            try:
                # Replace 'Z' with '+00:00' for compatibility with fromisoformat across Python versions
                # if the 'Z' suffix is used. fromisoformat handles '+00:00' correctly.
                iso_compatible_date_str = market.end.replace('Z', '+00:00')
                market_end_dt_obj = datetime.fromisoformat(iso_compatible_date_str)

                # If parsing results in a naive datetime (no timezone info),
                # assume it's intended to be UTC, consistent with 'now'.
                if market_end_dt_obj.tzinfo is None:
                    market_end_dt_obj = market_end_dt_obj.replace(tzinfo=timezone.utc)

            except ValueError as e:
                print(f"Could not parse market end date for market ID {market.id} ('{market.end}'): {e}")
                continue

            # 'now' and 'market_end_dt_obj' are now both offset-aware UTC.
            days_until_expiration = (market_end_dt_obj - now).days

            if 0 <= days_until_expiration <= self.days_to_expiration_threshold:
                print(f"Market '{market.question}' (ID: {market.id}) is expiring in {days_until_expiration} days.")

                odds = self._parse_outcome_prices(market.outcome_prices)
                news = self._fetch_news_for_market(market.question) # Or market.description

                report_item = ExpiringMarketReportItem(
                    market_id=market.id,
                    question=market.question,
                    expiration_date=market.end, # Store original string format
                    days_remaining=days_until_expiration, # Added
                    odds=odds,
                    news_articles=news,
                    action_filed="No specific action defined or taken by this script."
                )
                expiring_markets_reports.append(report_item)

        if not expiring_markets_reports:
            print(f"No markets found expiring within the next {self.days_to_expiration_threshold} days.")
            return

        print("\n--- Expiring Markets Report ---")
        for report in expiring_markets_reports:
            print(f"\nMarket ID: {report.market_id}")
            print(f"Question: {report.question}")
            print(f"Expires on: {report.expiration_date} (in {report.days_remaining} days)") # Use days_remaining
            print(f"Current Odds: {report.odds}")
            print(f"Action Filed: {report.action_filed}")
            if report.news_articles:
                print("Relevant News:")
                for article_idx, article in enumerate(report.news_articles):
                    print(f"  {article_idx + 1}. {article.title} ({article.url}) - Published: {article.publishedAt}")
                    if article_idx >= 2: # Limit news articles displayed per market
                        print(f"  ... and {len(report.news_articles) - (article_idx + 1)} more.")
                        break
            else:
                print("Relevant News: No articles found.")
        print("\n--- End of Report ---")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv() # Load environment variables from .env file
    print("Running ExpiringMarketsReporter directly for testing...")
    # This requires POLYGON_WALLET_PRIVATE_KEY and NEWSAPI_API_KEY to be set in .env
    # and the .env file to be loaded, or variables present in the environment.
    # Consider adding dotenv loading here if not handled by Polymarket/News clients internally on init.
    # from dotenv import load_dotenv
    # load_dotenv() # If you have a .env file and keys are not auto-loaded by clients

    reporter = ExpiringMarketsReporter(days_to_expiration_threshold=35)
    reporter.check_and_report_expiring_markets()
