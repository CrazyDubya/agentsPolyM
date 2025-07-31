#!/usr/bin/env python3
"""
Polymarket Agents Optimized Demo

A performance-optimized version of the comprehensive demo showcasing 
the full functionality of the Polymarket Agents framework.

Key optimizations:
- Reduced wait times for better user experience
- Cached data structures for faster loading
- Streamlined animations and transitions
- Optional verbose mode for detailed output
"""

import os
import sys
import json
import time
import random
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import argparse

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
class OptimizedDemoMarket:
    """Optimized market data structure"""
    id: str
    question: str
    description: str
    outcomes: List[str]
    prices: List[float]
    volume: float
    end_time: str
    category: str
    ai_prediction: float = 0.0
    confidence: float = 0.0
    edge: float = 0.0

class OptimizedPolymarketDemo:
    """Performance-optimized demo implementation"""
    
    def __init__(self, verbose: bool = False, fast_mode: bool = True):
        self.verbose = verbose
        self.fast_mode = fast_mode
        self.delay_multiplier = 0.3 if fast_mode else 1.0
        
        # Pre-cached demo data for performance
        self._initialize_demo_data()
        
    def _initialize_demo_data(self):
        """Pre-initialize all demo data for performance"""
        self.markets = [
            OptimizedDemoMarket(
                id="market_001",
                question="Will AI achieve AGI by 2025?",
                description="AGI market analysis",
                outcomes=["Yes", "No"],
                prices=[0.15, 0.85],
                volume=125000.50,
                end_time="2025-12-31",
                category="Technology",
                ai_prediction=0.23,
                confidence=0.78,
                edge=0.08
            ),
            OptimizedDemoMarket(
                id="market_002", 
                question="Will Bitcoin reach $100,000 in 2024?",
                description="Bitcoin price prediction market",
                outcomes=["Yes", "No"],
                prices=[0.35, 0.65],
                volume=89000.25,
                end_time="2024-12-31",
                category="Cryptocurrency",
                ai_prediction=0.42,
                confidence=0.85,
                edge=0.07
            ),
            OptimizedDemoMarket(
                id="market_003",
                question="Will there be a recession in 2024?",
                description="Economic recession prediction",
                outcomes=["Yes", "No"],
                prices=[0.28, 0.72],
                volume=156000.75,
                end_time="2024-12-31",
                category="Economics",
                ai_prediction=0.31,
                confidence=0.72,
                edge=0.03
            )
        ]
        
        self.news_data = [
            {
                "title": "Major AI Breakthrough: New Model Shows Human-Level Reasoning",
                "source": "TechCrunch",
                "sentiment": 0.8,
                "relevance": 0.9,
                "impact": "Positive for AGI timeline predictions"
            },
            {
                "title": "Bitcoin Institutional Adoption Reaches New Highs",
                "source": "CoinDesk", 
                "sentiment": 0.7,
                "relevance": 0.85,
                "impact": "Bullish for crypto markets"
            },
            {
                "title": "Federal Reserve Signals Potential Rate Cuts",
                "source": "Reuters",
                "sentiment": -0.3,
                "relevance": 0.8,
                "impact": "Mixed economic signals"
            }
        ]
        
        self.portfolio_metrics = {
            "initial_capital": 10000.00,
            "current_value": 10850.50,
            "total_return": 850.50,
            "roi_percent": 8.51,
            "active_positions": 3,
            "win_rate": 73.2,
            "sharpe_ratio": 1.84,
            "max_drawdown": -8.5
        }

    def print_header(self):
        """Optimized header display"""
        if not self.fast_mode:
            print("=" * 60)
        print(f"{Colors.HEADER}{Colors.BOLD}🤖 POLYMARKET AGENTS - OPTIMIZED DEMO{Colors.ENDC}")
        if not self.fast_mode:
            print("=" * 60)
        print()

    def delay(self, seconds: float):
        """Optimized delay function"""
        if self.fast_mode:
            time.sleep(seconds * self.delay_multiplier)
        else:
            time.sleep(seconds)

    def run_market_analysis(self):
        """Optimized market analysis"""
        print(f"{Colors.BLUE}🔍 Market Analysis & Filtering{Colors.ENDC}")
        
        if self.verbose:
            print("Scanning available prediction markets...")
            self.delay(0.5)
        
        print(f"\n{Colors.GREEN}✅ Found {len(self.markets)} active markets:{Colors.ENDC}")
        
        for i, market in enumerate(self.markets, 1):
            print(f"\n{i}. {market.question}")
            print(f"   📊 Current Odds: Yes ${market.prices[0]:.2f} ({market.prices[0]*100:.1f}%)")
            print(f"   💰 Volume: ${market.volume:,.2f}")
            print(f"   🏷️  Category: {market.category}")
            
            if self.verbose:
                print(f"   📅 Expires: {market.end_time}")
                
        self.delay(1.0)
        
    def run_sentiment_analysis(self):
        """Optimized sentiment analysis"""
        print(f"\n{Colors.CYAN}📰 News Sentiment Integration{Colors.ENDC}")
        
        if self.verbose:
            print("Gathering news from multiple sources...")
            self.delay(0.5)
            
        print(f"\n{Colors.GREEN}✅ Analyzed {len(self.news_data)} relevant articles:{Colors.ENDC}")
        
        for news in self.news_data:
            sentiment_emoji = "📈" if news["sentiment"] > 0 else "📉"
            print(f"\n{sentiment_emoji} {news['title']}")
            print(f"   Source: {news['source']} | Sentiment: {news['sentiment']:+.2f}")
            if self.verbose:
                print(f"   Impact: {news['impact']}")
                
        self.delay(1.0)

    def run_ai_predictions(self):
        """Optimized AI prediction generation"""
        print(f"\n{Colors.WARNING}🧠 AI Superforecaster Analysis{Colors.ENDC}")
        
        if self.verbose:
            print("Running deep learning models on market data...")
            self.delay(0.5)
            
        print(f"\n{Colors.GREEN}✅ AI Predictions Generated:{Colors.ENDC}")
        
        for market in self.markets:
            edge_color = Colors.GREEN if market.edge > 0.05 else Colors.WARNING
            print(f"\n📊 {market.question}")
            print(f"   🤖 AI Prediction: {market.ai_prediction*100:.1f}%")
            print(f"   📈 Market Price: {market.prices[0]*100:.1f}%")
            print(f"   {edge_color}⚡ Edge Detected: {market.edge*100:.1f}%{Colors.ENDC}")
            print(f"   🎯 Confidence: {market.confidence*100:.1f}%")
            
            # Confidence bar
            bar_length = 20
            filled = int(market.confidence * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"   [{bar}]")
            
        self.delay(1.5)

    def run_trading_simulation(self):
        """Optimized trading simulation"""
        print(f"\n{Colors.HEADER}💼 Automated Trading Execution{Colors.ENDC}")
        
        if self.verbose:
            print("Analyzing risk parameters and position sizing...")
            self.delay(0.5)
            
        print(f"\n{Colors.GREEN}✅ Trade Analysis Complete:{Colors.ENDC}")
        
        total_allocation = 0
        for market in self.markets:
            if market.edge > 0.05:  # Only trade high-edge opportunities
                allocation = min(market.confidence * market.edge * 5000, 1000)  # Max $1000 per position
                total_allocation += allocation
                
                print(f"\n📈 TRADE: {market.question}")
                print(f"   💰 Position Size: ${allocation:.2f}")
                print(f"   🎯 Target: {market.ai_prediction*100:.1f}%")
                print(f"   ⚠️  Risk Level: {'Low' if market.edge > 0.07 else 'Medium'}")
                
        print(f"\n{Colors.BLUE}📊 Total Portfolio Allocation: ${total_allocation:.2f}{Colors.ENDC}")
        self.delay(1.0)

    def show_performance_dashboard(self):
        """Optimized performance dashboard"""
        print(f"\n{Colors.GREEN}📈 Portfolio Performance Dashboard{Colors.ENDC}")
        
        metrics = self.portfolio_metrics
        
        print(f"\n💰 Portfolio Value: ${metrics['current_value']:,.2f}")
        print(f"📊 Total Return: {metrics['roi_percent']:+.2f}% (${metrics['total_return']:+,.2f})")
        print(f"🎯 Win Rate: {metrics['win_rate']:.1f}%")
        print(f"📐 Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
        print(f"⚠️  Max Drawdown: {metrics['max_drawdown']:.1f}%")
        
        # Performance visualization
        print(f"\n{Colors.CYAN}Performance Chart (Last 30 Days):{Colors.ENDC}")
        chart_points = [10000 + random.randint(-200, 300) + i*25 for i in range(30)]
        chart_str = ""
        for i, value in enumerate(chart_points[::3]):  # Show every 3rd point for compactness
            normalized = int((value - 9500) / 100)  # Normalize to 0-10 range
            chart_str += "█" * normalized + " "
        print(f"   {chart_str}")
        print(f"   ${chart_points[0]:,.0f} ────────────────────── ${chart_points[-1]:,.0f}")
        
        self.delay(1.0)

    def show_completion(self):
        """Show demo completion"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Demo Complete!{Colors.ENDC}")
        print(f"\n{Colors.CYAN}Demo showcased:{Colors.ENDC}")
        print("✅ Market discovery and analysis")
        print("✅ News sentiment integration") 
        print("✅ AI-powered predictions")
        print("✅ Automated trading execution")
        print("✅ Performance monitoring")
        
        print(f"\n{Colors.WARNING}⚠️  This was a simulated demonstration using mock data.{Colors.ENDC}")
        print(f"{Colors.WARNING}Real trading involves substantial risk.{Colors.ENDC}")

    def run_interactive_mode(self):
        """Interactive exploration mode"""
        while True:
            print(f"\n{Colors.BLUE}🎮 Interactive Mode{Colors.ENDC}")
            print("1. Re-run market analysis")
            print("2. Adjust risk parameters")
            print("3. View detailed predictions")
            print("4. Show portfolio history")
            print("5. Exit")
            
            try:
                choice = input(f"\n{Colors.CYAN}Select option (1-5): {Colors.ENDC}").strip()
                
                if choice == '1':
                    self.run_market_analysis()
                elif choice == '2':
                    self.adjust_risk_parameters()
                elif choice == '3':
                    self.show_detailed_predictions()
                elif choice == '4':
                    self.show_portfolio_history()
                elif choice == '5':
                    break
                else:
                    print("Invalid option. Please try again.")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}Demo interrupted by user.{Colors.ENDC}")
                break

    def adjust_risk_parameters(self):
        """Allow user to adjust risk parameters"""
        print(f"\n{Colors.WARNING}🎛️  Risk Parameter Adjustment{Colors.ENDC}")
        
        try:
            risk_tolerance = float(input("Risk tolerance (0.1-1.0): ") or "0.5")
            max_position = float(input("Max position size ($): ") or "1000")
            confidence_threshold = float(input("Confidence threshold (0.5-0.95): ") or "0.7")
            
            print(f"\n{Colors.GREEN}✅ Updated parameters:{Colors.ENDC}")
            print(f"   Risk Tolerance: {risk_tolerance:.1f}")
            print(f"   Max Position: ${max_position:.2f}")
            print(f"   Confidence Threshold: {confidence_threshold:.1f}")
            
            # Recalculate projections
            estimated_return = risk_tolerance * 15 + (1 - confidence_threshold) * 5
            print(f"\n{Colors.CYAN}📊 Estimated Annual Return: {estimated_return:.1f}%{Colors.ENDC}")
            
        except ValueError:
            print("Invalid input. Using default parameters.")

    def show_detailed_predictions(self):
        """Show detailed AI predictions"""
        print(f"\n{Colors.CYAN}🔍 Detailed AI Prediction Analysis{Colors.ENDC}")
        
        for market in self.markets:
            print(f"\n📊 {market.question}")
            print(f"   🤖 AI Model Confidence: {market.confidence*100:.1f}%")
            print(f"   📈 Prediction: {market.ai_prediction*100:.2f}%")
            print(f"   🏪 Market Price: {market.prices[0]*100:.2f}%")
            print(f"   ⚡ Edge: {market.edge*100:.2f}%")
            
            # Risk assessment
            risk_level = "Low" if market.edge > 0.07 else "Medium" if market.edge > 0.03 else "High"
            print(f"   ⚠️  Risk Level: {risk_level}")
            
            # Expected value calculation
            expected_value = market.ai_prediction * 1.0 + (1 - market.ai_prediction) * (-market.prices[0])
            print(f"   💰 Expected Value: {expected_value:.3f}")

    def show_portfolio_history(self):
        """Show portfolio performance history"""
        print(f"\n{Colors.GREEN}📈 Portfolio Performance History{Colors.ENDC}")
        
        # Generate sample historical data
        dates = ["2024-01-01", "2024-01-15", "2024-02-01", "2024-02-15", "2024-03-01"]
        values = [10000, 10150, 10320, 10280, 10850]
        
        print(f"\n{Colors.CYAN}Historical Performance:{Colors.ENDC}")
        for date, value in zip(dates, values):
            return_pct = ((value - 10000) / 10000) * 100
            color = Colors.GREEN if return_pct > 0 else Colors.FAIL
            print(f"   {date}: ${value:,.2f} ({color}{return_pct:+.2f}%{Colors.ENDC})")

    def run_full_demo(self):
        """Run the complete optimized demo"""
        self.print_header()
        
        if not self.fast_mode:
            input("Press Enter to begin the optimized demo...")
        
        # Main demo sequence
        self.run_market_analysis()
        self.run_sentiment_analysis() 
        self.run_ai_predictions()
        self.run_trading_simulation()
        self.show_performance_dashboard()
        self.show_completion()
        
        # Offer interactive mode
        if input(f"\n{Colors.CYAN}Enter interactive mode? (y/N): {Colors.ENDC}").lower().startswith('y'):
            self.run_interactive_mode()

def main():
    parser = argparse.ArgumentParser(description='Polymarket Agents Optimized Demo')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--slow', action='store_true', help='Disable fast mode')
    parser.add_argument('--interactive', '-i', action='store_true', help='Start in interactive mode')
    
    args = parser.parse_args()
    
    # Create and run demo
    demo = OptimizedPolymarketDemo(
        verbose=args.verbose, 
        fast_mode=not args.slow
    )
    
    if args.interactive:
        demo.run_interactive_mode()
    else:
        demo.run_full_demo()

if __name__ == "__main__":
    main()