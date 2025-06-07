from agents.application.trade import Trader
from agents.application.expiring_markets_reporter import ExpiringMarketsReporter # Added
import time

from scheduler import Scheduler as PythonScheduler # Renamed to avoid confusion with our class
from scheduler.trigger import Monday


class Scheduler: # Custom Scheduler wrapper
    def __init__(self) -> None:
        # self.trader = Trader() # Removed: Specific to TradingAgent
        self.schedule = PythonScheduler() # Instantiate the imported scheduler library

    def start(self) -> None:
        print("Scheduler starting... Will execute jobs as per schedule.")
        while True:
            self.schedule.run_pending() # Changed from exec_jobs() to standard run_pending()
            time.sleep(1)


class TradingAgent(Scheduler):
    def __init__(self) -> None:
        super().__init__() # Corrected super() call
        self.trader = Trader()
        self.expiring_markets_reporter = ExpiringMarketsReporter(days_to_expiration_threshold=35) # Added

        # Schedule weekly trade using standard 'schedule' library syntax
        # Assuming Monday from scheduler.trigger is compatible or .monday is the way
        self.schedule.every().monday.do(self.trader.one_best_trade) # Changed from self.weekly()

        # Schedule hourly market expiration check
        self.schedule.every().hour.do(self.expiring_markets_reporter.check_and_report_expiring_markets) # Added

        print("TradingAgent initialized. Scheduled tasks: weekly one_best_trade, hourly expiring_markets_report.")

# main block to run this for testing
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv() # Load environment variables from .env file
    print("Initializing agent and scheduling jobs for testing...") # Updated print message
    # This part is for testing the cron setup itself.
    # Ensure environment variables for Polymarket and News APIs are set if tasks run immediately.
    # from dotenv import load_dotenv
    # load_dotenv() # Uncomment if .env file is used for keys

    agent = TradingAgent()

    print("Scheduled jobs:")
    if hasattr(agent.schedule, 'jobs'):
        for job in agent.schedule.jobs:
            print(job)
    else:
        print("Could not retrieve job list from scheduler, attribute 'jobs' not found.")

    print("Starting agent's scheduler loop (will run indefinitely)...")
    try:
        agent.start()
    except KeyboardInterrupt:
        print("Scheduler stopped manually.")
