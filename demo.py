#!/usr/bin/env python3
"""
Polymarket Agents Comprehensive Demo

This demo showcases the full functionality of the Polymarket Agents framework
in an interactive and educational manner.
"""

import os
import sys
import json
import time
import random
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@dataclass
class DemoMarket:
    """Simulated market data for demo purposes"""
    id: str
    question: str
    description: str
    outcomes: List[str]
    prices: List[float]
    volume: float
    end_time: str
    category: str

@dataclass
class DemoNews:
    """Simulated news data for demo purposes"""
    title: str
    content: str
    source: str
    published_at: str
    sentiment: float
    relevance: float

class PolymarketAgentsDemo:
    """
    Comprehensive demo of Polymarket Agents functionality
    """
    
    def __init__(self):
        self.demo_markets = self._generate_demo_markets()
        self.demo_news = self._generate_demo_news()
        self.ai_predictions = {}
        self.trading_history = []
        
    def _generate_demo_markets(self) -> List[DemoMarket]:
        """Generate realistic demo market data"""
        markets = [
            DemoMarket(
                id="market_001",
                question="Will AI achieve AGI by 2025?",
                description="This market resolves to 'Yes' if an AI system demonstrates general intelligence capabilities across multiple domains by December 31, 2025.",
                outcomes=["Yes", "No"],
                prices=[0.15, 0.85],
                volume=125000.50,
                end_time="2025-12-31",
                category="Technology"
            ),
            DemoMarket(
                id="market_002", 
                question="Will Bitcoin reach $100,000 in 2024?",
                description="This market resolves to 'Yes' if Bitcoin (BTC) reaches or exceeds $100,000 USD at any point during 2024.",
                outcomes=["Yes", "No"],
                prices=[0.35, 0.65],
                volume=89000.25,
                end_time="2024-12-31",
                category="Cryptocurrency"
            ),
            DemoMarket(
                id="market_003",
                question="Will there be a recession in 2024?",
                description="This market resolves to 'Yes' if the US economy experiences two consecutive quarters of negative GDP growth in 2024.",
                outcomes=["Yes", "No"],
                prices=[0.28, 0.72],
                volume=156000.75,
                end_time="2024-12-31",
                category="Economics"
            ),
            DemoMarket(
                id="market_004",
                question="Will SpaceX land humans on Mars by 2030?",
                description="This market resolves to 'Yes' if SpaceX successfully lands human astronauts on Mars by December 31, 2030.",
                outcomes=["Yes", "No"],
                prices=[0.12, 0.88],
                volume=67000.00,
                end_time="2030-12-31",
                category="Space"
            ),
            DemoMarket(
                id="market_005",
                question="Will renewable energy exceed 50% of US electricity by 2026?",
                description="This market resolves to 'Yes' if renewable energy sources generate more than 50% of US electricity in any month of 2026.",
                outcomes=["Yes", "No"],
                prices=[0.42, 0.58],
                volume=78000.30,
                end_time="2026-12-31",
                category="Energy"
            )
        ]
        return markets
    
    def _generate_demo_news(self) -> List[DemoNews]:
        """Generate realistic demo news data"""
        news = [
            DemoNews(
                title="Major AI Breakthrough: New Model Shows Human-Level Reasoning",
                content="Researchers announce breakthrough in AI reasoning capabilities, bringing AGI timeline estimates forward.",
                source="TechCrunch",
                published_at="2024-01-15 10:30:00",
                sentiment=0.8,
                relevance=0.9
            ),
            DemoNews(
                title="Bitcoin Institutional Adoption Reaches New Highs",
                content="Major corporations continue adding Bitcoin to treasury reserves, driving price momentum.",
                source="CoinDesk",
                published_at="2024-01-14 14:22:00",
                sentiment=0.7,
                relevance=0.85
            ),
            DemoNews(
                title="Federal Reserve Signals Potential Rate Cuts",
                content="Fed chairman hints at possible interest rate reductions if economic indicators worsen.",
                source="Reuters",
                published_at="2024-01-13 09:15:00",
                sentiment=-0.3,
                relevance=0.8
            ),
            DemoNews(
                title="SpaceX Advances Mars Mission Timeline",
                content="Elon Musk announces accelerated development of Starship for Mars missions.",
                source="Space News",
                published_at="2024-01-12 16:45:00",
                sentiment=0.6,
                relevance=0.75
            ),
            DemoNews(
                title="Renewable Energy Installations Hit Record Pace",
                content="Solar and wind capacity additions exceed projections for Q4 2023.",
                source="Energy Weekly",
                published_at="2024-01-11 11:30:00",
                sentiment=0.65,
                relevance=0.7
            )
        ]
        return news
    
    def print_header(self, title: str):
        """Print a formatted header"""
        print(f"\n{Colors.HEADER}{'='*60}")
        print(f"{Colors.BOLD}{title.center(60)}")
        print(f"{'='*60}{Colors.ENDC}\n")
    
    def print_section(self, title: str):
        """Print a formatted section header"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}--- {title} ---{Colors.ENDC}")
    
    def display_welcome(self):
        """Display welcome message and demo overview"""
        self.print_header("POLYMARKET AGENTS COMPREHENSIVE DEMO")
        
        print(f"{Colors.BLUE}Welcome to the Polymarket Agents Demo!{Colors.ENDC}")
        print(f"{Colors.GREEN}This interactive demo showcases the full capabilities of the AI-powered")
        print(f"prediction market trading system.{Colors.ENDC}\n")
        
        print(f"{Colors.CYAN}🎯 Demo Features:{Colors.ENDC}")
        print("  1. Market Analysis & Filtering")
        print("  2. News Sentiment Integration") 
        print("  3. AI-Powered Trading Decisions")
        print("  4. Superforecasting Capabilities")
        print("  5. RAG-Based Market Research")
        print("  6. Risk Management & Portfolio Optimization")
        
        input(f"\n{Colors.WARNING}Press Enter to begin the demo...{Colors.ENDC}")
    
    def demo_market_analysis(self):
        """Demonstrate market analysis capabilities"""
        self.print_section("1. MARKET ANALYSIS & FILTERING")
        
        print(f"{Colors.BLUE}🔍 Scanning available prediction markets...{Colors.ENDC}")
        time.sleep(1)
        
        print(f"\n{Colors.GREEN}Found {len(self.demo_markets)} active markets:{Colors.ENDC}")
        
        for i, market in enumerate(self.demo_markets, 1):
            price_yes, price_no = market.prices
            implied_prob = price_yes * 100
            
            print(f"\n{Colors.CYAN}{i}. {market.question}{Colors.ENDC}")
            print(f"   Category: {market.category}")
            print(f"   Current Odds: Yes ${price_yes:.2f} ({implied_prob:.1f}%) | No ${price_no:.2f}")
            print(f"   Volume: ${market.volume:,.2f}")
            print(f"   Expires: {market.end_time}")
        
        print(f"\n{Colors.WARNING}🤖 AI Analysis: Filtering markets for optimal trading opportunities...{Colors.ENDC}")
        time.sleep(2)
        
        # Simulate AI filtering logic
        high_volume_markets = [m for m in self.demo_markets if m.volume > 80000]
        print(f"{Colors.GREEN}✅ Identified {len(high_volume_markets)} high-volume markets with good liquidity{Colors.ENDC}")
        
        input(f"\n{Colors.WARNING}Press Enter to continue to news analysis...{Colors.ENDC}")
    
    def demo_news_integration(self):
        """Demonstrate news sentiment analysis"""
        self.print_section("2. NEWS SENTIMENT INTEGRATION")
        
        print(f"{Colors.BLUE}📰 Gathering relevant news from multiple sources...{Colors.ENDC}")
        time.sleep(1)
        
        print(f"\n{Colors.GREEN}Recent news articles analyzed:{Colors.ENDC}")
        
        for i, news in enumerate(self.demo_news, 1):
            sentiment_icon = "📈" if news.sentiment > 0 else "📉" if news.sentiment < 0 else "➡️"
            sentiment_color = Colors.GREEN if news.sentiment > 0 else Colors.FAIL if news.sentiment < 0 else Colors.WARNING
            
            print(f"\n{Colors.CYAN}{i}. {news.title}{Colors.ENDC}")
            print(f"   Source: {news.source} | Published: {news.published_at}")
            print(f"   {sentiment_icon} Sentiment: {sentiment_color}{news.sentiment:+.2f}{Colors.ENDC} | Relevance: {news.relevance:.2f}")
            print(f"   Summary: {news.content}")
        
        print(f"\n{Colors.WARNING}🤖 AI Sentiment Analysis: Correlating news impact with market movements...{Colors.ENDC}")
        time.sleep(2)
        
        # Simulate sentiment impact analysis
        for market in self.demo_markets:
            relevant_news = [n for n in self.demo_news if market.category.lower() in n.content.lower() or 
                           any(word in n.content.lower() for word in market.question.lower().split())]
            if relevant_news:
                avg_sentiment = sum(n.sentiment for n in relevant_news) / len(relevant_news)
                print(f"{Colors.GREEN}📊 {market.question}: Average sentiment {avg_sentiment:+.2f}{Colors.ENDC}")
        
        input(f"\n{Colors.WARNING}Press Enter to continue to AI decision making...{Colors.ENDC}")
    
    def demo_ai_predictions(self):
        """Demonstrate AI-powered prediction generation"""
        self.print_section("3. AI-POWERED TRADING DECISIONS")
        
        print(f"{Colors.BLUE}🧠 Running AI superforecaster analysis...{Colors.ENDC}")
        time.sleep(1)
        
        print(f"\n{Colors.CYAN}Superforecaster Analysis Process:{Colors.ENDC}")
        print("1. Breaking down questions into components")
        print("2. Analyzing historical base rates")
        print("3. Evaluating current factors and trends")
        print("4. Incorporating news sentiment")
        print("5. Calculating probabilistic predictions")
        
        time.sleep(2)
        
        for market in self.demo_markets[:3]:  # Analyze first 3 markets
            print(f"\n{Colors.WARNING}🎯 Analyzing: {market.question}{Colors.ENDC}")
            time.sleep(1)
            
            # Simulate AI analysis
            base_rate = random.uniform(0.1, 0.9)
            news_adjustment = random.uniform(-0.1, 0.1)
            final_prediction = max(0.05, min(0.95, base_rate + news_adjustment))
            
            current_price = market.prices[0]
            edge = abs(final_prediction - current_price)
            
            print(f"   📊 Base rate analysis: {base_rate:.2f}")
            print(f"   📰 News sentiment adjustment: {news_adjustment:+.2f}")
            print(f"   🎯 Final AI prediction: {final_prediction:.2f}")
            print(f"   💰 Current market price: {current_price:.2f}")
            print(f"   ⚖️  Edge detected: {edge:.2f}")
            
            self.ai_predictions[market.id] = {
                'prediction': final_prediction,
                'current_price': current_price,
                'edge': edge,
                'confidence': random.uniform(0.6, 0.9)
            }
            
            if edge > 0.1:
                action = "BUY" if final_prediction > current_price else "SELL"
                print(f"   {Colors.GREEN}✅ TRADE SIGNAL: {action} - Strong edge detected!{Colors.ENDC}")
            else:
                print(f"   {Colors.WARNING}⚠️  No trade - insufficient edge{Colors.ENDC}")
        
        input(f"\n{Colors.WARNING}Press Enter to continue to RAG research...{Colors.ENDC}")
    
    def demo_rag_research(self):
        """Demonstrate RAG-based market research"""
        self.print_section("4. RAG-BASED MARKET RESEARCH")
        
        print(f"{Colors.BLUE}🔍 Initializing Retrieval-Augmented Generation system...{Colors.ENDC}")
        time.sleep(1)
        
        print(f"\n{Colors.CYAN}RAG System Components:{Colors.ENDC}")
        print("📚 Vector database with market history")
        print("📊 Technical analysis patterns")
        print("📰 News archive and sentiment trends")
        print("🏛️  Economic indicators and correlations")
        print("🎯 Expert predictions and track records")
        
        time.sleep(1)
        
        # Simulate RAG queries
        queries = [
            "Historical accuracy of AI prediction markets",
            "Bitcoin price correlation with institutional adoption",
            "Recession indicators and market sentiment",
            "SpaceX mission success rates and timeline accuracy"
        ]
        
        print(f"\n{Colors.WARNING}🔎 Running knowledge base queries...{Colors.ENDC}")
        
        for query in queries:
            print(f"\n{Colors.CYAN}Query: {query}{Colors.ENDC}")
            time.sleep(1)
            
            # Simulate RAG response
            confidence = random.uniform(0.7, 0.95)
            sources_found = random.randint(15, 45)
            
            print(f"   📄 Found {sources_found} relevant sources")
            print(f"   🎯 Confidence score: {confidence:.2f}")
            print(f"   📈 Key insight: {self._generate_insight(query)}")
        
        input(f"\n{Colors.WARNING}Press Enter to continue to trade execution...{Colors.ENDC}")
    
    def _generate_insight(self, query: str) -> str:
        """Generate demo insights based on query"""
        insights = {
            "AI prediction": "AI prediction markets show 73% accuracy over 2-year periods",
            "Bitcoin": "95% correlation between institutional announcements and 30-day returns", 
            "Recession": "Current indicators suggest 28% probability based on yield curve analysis",
            "SpaceX": "Historical mission success rate: 94%, timeline accuracy: 67%"
        }
        
        for key, insight in insights.items():
            if key.lower() in query.lower():
                return insight
        return "Analysis suggests moderate confidence in current market pricing"
    
    def demo_trade_execution(self):
        """Demonstrate automated trade execution"""
        self.print_section("5. AUTOMATED TRADE EXECUTION")
        
        print(f"{Colors.BLUE}⚡ Executing optimal trades based on AI analysis...{Colors.ENDC}")
        time.sleep(1)
        
        portfolio_value = 10000.0
        print(f"\n{Colors.CYAN}Starting Portfolio Value: ${portfolio_value:,.2f}{Colors.ENDC}")
        
        for market_id, prediction in self.ai_predictions.items():
            market = next(m for m in self.demo_markets if m.id == market_id)
            
            if prediction['edge'] > 0.1:
                position_size = min(0.1, prediction['edge'] * prediction['confidence'])
                trade_amount = portfolio_value * position_size
                
                side = "BUY" if prediction['prediction'] > prediction['current_price'] else "SELL"
                outcome = "Yes" if side == "BUY" else "No"
                
                print(f"\n{Colors.WARNING}🎯 EXECUTING TRADE:{Colors.ENDC}")
                print(f"   Market: {market.question}")
                print(f"   Side: {Colors.GREEN if side == 'BUY' else Colors.FAIL}{side}{Colors.ENDC}")
                print(f"   Outcome: {outcome}")
                print(f"   Amount: ${trade_amount:,.2f} ({position_size*100:.1f}% of portfolio)")
                print(f"   Price: ${prediction['current_price']:.2f}")
                print(f"   Expected value: {prediction['prediction']:.2f}")
                
                trade = {
                    'market': market.question,
                    'side': side,
                    'amount': trade_amount,
                    'price': prediction['current_price'],
                    'expected_return': (prediction['prediction'] - prediction['current_price']) * trade_amount
                }
                self.trading_history.append(trade)
                
                time.sleep(1)
                print(f"   {Colors.GREEN}✅ Trade executed successfully!{Colors.ENDC}")
        
        total_exposure = sum(abs(trade['amount']) for trade in self.trading_history)
        expected_profit = sum(trade['expected_return'] for trade in self.trading_history)
        
        print(f"\n{Colors.CYAN}📊 Trading Summary:{Colors.ENDC}")
        print(f"   Total positions: {len(self.trading_history)}")
        print(f"   Total exposure: ${total_exposure:,.2f}")
        print(f"   Expected profit: ${expected_profit:+,.2f}")
        print(f"   Expected ROI: {(expected_profit/portfolio_value)*100:+.2f}%")
        
        input(f"\n{Colors.WARNING}Press Enter to continue to risk management...{Colors.ENDC}")
    
    def demo_risk_management(self):
        """Demonstrate risk management and optimization"""
        self.print_section("6. RISK MANAGEMENT & OPTIMIZATION")
        
        print(f"{Colors.BLUE}⚖️  Running portfolio risk analysis...{Colors.ENDC}")
        time.sleep(1)
        
        print(f"\n{Colors.CYAN}Risk Metrics:{Colors.ENDC}")
        
        # Simulate risk calculations
        portfolio_correlation = random.uniform(0.1, 0.3)
        max_drawdown = random.uniform(0.05, 0.15)
        sharpe_ratio = random.uniform(1.2, 2.1)
        win_rate = random.uniform(0.65, 0.85)
        
        print(f"   📊 Portfolio correlation: {portfolio_correlation:.2f}")
        print(f"   📉 Maximum drawdown: {max_drawdown*100:.1f}%")
        print(f"   📈 Expected Sharpe ratio: {sharpe_ratio:.2f}")
        print(f"   🎯 Historical win rate: {win_rate*100:.1f}%")
        
        print(f"\n{Colors.WARNING}🛡️  Risk Management Rules:{Colors.ENDC}")
        print("   • Maximum 10% position size per market")
        print("   • Stop-loss at 20% portfolio drawdown")
        print("   • Diversification across at least 5 categories")
        print("   • Daily risk assessment and rebalancing")
        
        print(f"\n{Colors.GREEN}✅ Portfolio within risk parameters{Colors.ENDC}")
        
        time.sleep(2)
        
        print(f"\n{Colors.CYAN}🔄 Optimization Suggestions:{Colors.ENDC}")
        print("   • Increase position in high-confidence AI prediction market")
        print("   • Reduce exposure to highly correlated crypto markets")
        print("   • Consider hedging with inverse correlation positions")
        
        input(f"\n{Colors.WARNING}Press Enter to view final results...{Colors.ENDC}")
    
    def demo_results_summary(self):
        """Display comprehensive results summary"""
        self.print_section("DEMO RESULTS SUMMARY")
        
        print(f"{Colors.BLUE}📈 Performance Summary{Colors.ENDC}")
        
        # Calculate demo performance metrics
        total_trades = len(self.trading_history)
        total_expected_return = sum(trade['expected_return'] for trade in self.trading_history)
        initial_capital = 10000.0
        
        print(f"\n{Colors.CYAN}Trading Performance:{Colors.ENDC}")
        print(f"   Initial Capital: ${initial_capital:,.2f}")
        print(f"   Total Trades: {total_trades}")
        print(f"   Expected Return: ${total_expected_return:+,.2f}")
        print(f"   Expected ROI: {(total_expected_return/initial_capital)*100:+.2f}%")
        
        print(f"\n{Colors.GREEN}🎯 AI System Accuracy:{Colors.ENDC}")
        print(f"   Markets Analyzed: {len(self.demo_markets)}")
        print(f"   Profitable Signals: {len([p for p in self.ai_predictions.values() if p['edge'] > 0.1])}")
        print(f"   Average Confidence: {sum(p['confidence'] for p in self.ai_predictions.values())/len(self.ai_predictions)*100:.1f}%")
        
        print(f"\n{Colors.CYAN}🔍 Data Sources Integrated:{Colors.ENDC}")
        print(f"   News Articles: {len(self.demo_news)}")
        print(f"   Market Data Points: {len(self.demo_markets) * 10}")
        print(f"   RAG Knowledge Sources: 247")
        
        print(f"\n{Colors.WARNING}⚠️  Important Disclaimer:{Colors.ENDC}")
        print(f"   This is a demonstration with simulated data.")
        print(f"   Real trading involves significant risks.")
        print(f"   Past performance does not guarantee future results.")
        
    def run_interactive_mode(self):
        """Run interactive exploration mode"""
        self.print_section("INTERACTIVE EXPLORATION MODE")
        
        while True:
            print(f"\n{Colors.CYAN}Choose an option:{Colors.ENDC}")
            print("1. Analyze specific market")
            print("2. Research market topic")
            print("3. Get AI prediction")
            print("4. View portfolio")
            print("5. Exit demo")
            
            choice = input(f"\n{Colors.WARNING}Enter your choice (1-5): {Colors.ENDC}")
            
            if choice == "1":
                self._analyze_specific_market()
            elif choice == "2":
                self._research_topic()
            elif choice == "3":
                self._get_ai_prediction()
            elif choice == "4":
                self._view_portfolio()
            elif choice == "5":
                break
            else:
                print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")
    
    def _analyze_specific_market(self):
        """Analyze a specific market in detail"""
        print(f"\n{Colors.CYAN}Available Markets:{Colors.ENDC}")
        for i, market in enumerate(self.demo_markets, 1):
            print(f"{i}. {market.question}")
        
        try:
            choice = int(input(f"\n{Colors.WARNING}Select market (1-{len(self.demo_markets)}): {Colors.ENDC}")) - 1
            if 0 <= choice < len(self.demo_markets):
                market = self.demo_markets[choice]
                print(f"\n{Colors.BLUE}📊 Detailed Analysis: {market.question}{Colors.ENDC}")
                print(f"Description: {market.description}")
                print(f"Current Prices: Yes ${market.prices[0]:.2f}, No ${market.prices[1]:.2f}")
                print(f"Implied Probability: {market.prices[0]*100:.1f}%")
                print(f"Trading Volume: ${market.volume:,.2f}")
                print(f"Market Category: {market.category}")
                
                if market.id in self.ai_predictions:
                    pred = self.ai_predictions[market.id]
                    print(f"\n{Colors.GREEN}🤖 AI Analysis:{Colors.ENDC}")
                    print(f"Predicted Probability: {pred['prediction']*100:.1f}%")
                    print(f"Edge vs Market: {pred['edge']*100:+.1f}%")
                    print(f"Confidence Level: {pred['confidence']*100:.1f}%")
            else:
                print(f"{Colors.FAIL}Invalid selection.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")
    
    def _research_topic(self):
        """Research a specific topic"""
        topic = input(f"\n{Colors.WARNING}Enter research topic: {Colors.ENDC}")
        print(f"\n{Colors.BLUE}🔍 Researching: {topic}{Colors.ENDC}")
        time.sleep(1)
        
        print(f"Found 23 relevant sources in knowledge base...")
        print(f"Analysis complete. Key findings:")
        print(f"• Historical patterns suggest 67% accuracy")
        print(f"• Current sentiment trending positive")
        print(f"• Risk factors include regulatory uncertainty")
        
    def _get_ai_prediction(self):
        """Get AI prediction for a custom question"""
        question = input(f"\n{Colors.WARNING}Enter your prediction question: {Colors.ENDC}")
        print(f"\n{Colors.BLUE}🧠 AI Analyzing: {question}{Colors.ENDC}")
        time.sleep(2)
        
        prediction = random.uniform(0.1, 0.9)
        confidence = random.uniform(0.6, 0.95)
        
        print(f"AI Prediction: {prediction*100:.1f}% probability")
        print(f"Confidence Level: {confidence*100:.1f}%")
        print(f"Key factors: Historical trends, current sentiment, expert consensus")
    
    def _view_portfolio(self):
        """View current portfolio status"""
        print(f"\n{Colors.BLUE}💼 Current Portfolio:{Colors.ENDC}")
        if self.trading_history:
            for i, trade in enumerate(self.trading_history, 1):
                print(f"{i}. {trade['market'][:50]}...")
                print(f"   {trade['side']} ${trade['amount']:,.2f} @ ${trade['price']:.2f}")
                print(f"   Expected Return: ${trade['expected_return']:+,.2f}")
        else:
            print("No active positions")
    
    def run_demo(self):
        """Run the complete demo"""
        try:
            self.display_welcome()
            self.demo_market_analysis()
            self.demo_news_integration()
            self.demo_ai_predictions()
            self.demo_rag_research()
            self.demo_trade_execution()
            self.demo_risk_management()
            self.demo_results_summary()
            
            print(f"\n{Colors.GREEN}🎉 Demo Complete!{Colors.ENDC}")
            
            explore = input(f"\n{Colors.WARNING}Would you like to explore interactively? (y/n): {Colors.ENDC}")
            if explore.lower() == 'y':
                self.run_interactive_mode()
            
            print(f"\n{Colors.BLUE}Thank you for exploring Polymarket Agents!{Colors.ENDC}")
            print(f"{Colors.CYAN}For more information, visit: https://github.com/polymarket/agents{Colors.ENDC}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}Demo interrupted by user. Goodbye!{Colors.ENDC}")
        except Exception as e:
            print(f"\n{Colors.FAIL}An error occurred: {e}{Colors.ENDC}")

if __name__ == "__main__":
    demo = PolymarketAgentsDemo()
    demo.run_demo()