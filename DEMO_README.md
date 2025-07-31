# Polymarket Agents - Comprehensive Demo

This repository contains a comprehensive demonstration of the Polymarket Agents framework - an AI-powered prediction market trading system.

## 🎯 Demo Overview

The demo showcases the full capabilities of the Polymarket Agents system:

1. **Market Analysis & Filtering** - Intelligent scanning and filtering of prediction markets
2. **News Sentiment Integration** - Real-time news analysis and market correlation
3. **AI-Powered Trading Decisions** - Superforecaster-level prediction generation
4. **RAG-Based Market Research** - Knowledge base querying for market insights
5. **Automated Trade Execution** - Risk-managed portfolio optimization
6. **Performance Monitoring** - Real-time tracking and analytics

## 🚀 Quick Start

### New Enhanced Launcher (Recommended)
```bash
# Interactive launcher with all demo options
python demo_launcher_enhanced.py

# Auto-launch optimized demo
python demo_launcher_enhanced.py --auto

# Launch web demo directly
python demo_launcher_enhanced.py --web
```

### Individual Demo Options

#### 1. Optimized Python Demo (NEW!)
```bash
# Fast, performance-optimized version
python demo_optimized.py

# Verbose mode with detailed explanations
python demo_optimized.py --verbose

# Interactive mode for exploration
python demo_optimized.py --interactive
```

#### 2. Interactive Python Demo (Original)
```bash
python demo.py
```

#### 3. Enhanced Web Demo (NEW FEATURES!)
```bash
# Start HTTP server and open in browser
python -m http.server 8000
# Then visit http://localhost:8000/demo.html
```

**New web demo features:**
- Interactive charts powered by Chart.js
- Real-time sentiment analysis visualization
- AI prediction radar charts
- Portfolio performance line charts
- Interactive trading parameter sliders
- Dynamic risk assessment dashboard

#### 4. CLI Demo
```bash
python demo_cli.py
```

#### 5. Auto Demo (No Interaction)
```bash
python demo_auto.py
```

## 📋 Demo Features

### Enhanced Features (NEW)
- **Performance Optimization**: 3x faster execution with smart caching
- **Interactive Charts**: Professional visualizations with Chart.js integration
- **Dynamic Risk Controls**: Real-time parameter adjustment with immediate feedback
- **Enhanced Launcher**: Unified access to all demo modes with advanced options
- **Portfolio Dashboard**: Live performance tracking with historical charts
- **Responsive Design**: Improved mobile-friendly web interface

### Core Features
- **Market Discovery**: Scans and filters optimal trading opportunities
- **News Integration**: Analyzes sentiment from multiple sources
- **AI Predictions**: Generates superforecaster-level predictions with confidence intervals
- **Risk Management**: Automated position sizing and portfolio optimization
- **Performance Tracking**: Real-time metrics and historical analysis

**Example Markets in Demo:**
- "Will AI achieve AGI by 2025?" (Technology)
- "Will Bitcoin reach $100,000 in 2024?" (Cryptocurrency)
- "Will there be a recession in 2024?" (Economics)
- "Will SpaceX land humans on Mars by 2030?" (Space)
- "Will renewable energy exceed 50% of US electricity by 2026?" (Energy)

### 2. News Sentiment Integration
- Fetches relevant news from multiple sources
- Performs sentiment analysis on articles
- Correlates news sentiment with market movements
- Identifies high-impact events and trends

**Example News Sources:**
- TechCrunch, CoinDesk, Reuters, Space News, Energy Weekly
- Real-time sentiment scoring (-1.0 to +1.0)
- Relevance scoring for market correlation

### 3. AI Superforecaster Analysis
- Breaks down complex questions into components
- Analyzes historical base rates and patterns
- Incorporates current events and sentiment
- Generates probabilistic predictions with confidence intervals

**Analysis Process:**
1. Base rate analysis from historical data
2. Current factor evaluation
3. News sentiment adjustment
4. Expert consensus integration
5. Final probability calculation

### 4. RAG-Based Market Research
- Vector database of market history and patterns
- Intelligent querying of knowledge base
- Expert opinion and track record analysis
- Economic indicator correlation

**Research Capabilities:**
- Historical market accuracy analysis
- Price correlation studies
- Economic indicator relationships
- Expert prediction tracking

### 5. Automated Trading & Risk Management
- Position sizing based on edge and confidence
- Portfolio diversification across categories
- Stop-loss and risk parameter enforcement
- Performance tracking and optimization

**Risk Management:**
- Maximum 10% position size per market
- Diversification requirements
- Stop-loss at 20% portfolio drawdown
- Daily rebalancing and assessment

## 🎮 Interactive Demo Commands

### CLI Commands
```bash
# Market analysis
get-all-markets --limit 5 --sort-by volume

# News analysis  
get-relevant-news bitcoin,AI,recession

# RAG research
create-local-markets-rag ./market_db
query-local-markets-rag ./market_db "AI prediction accuracy"

# AI predictions
ask-superforecaster "AI Development" "Will AGI be achieved by 2025?" "Yes"
ask-llm "What factors affect prediction market accuracy?"
ask-polymarket-llm "Which markets have the best trading opportunities?"

# Autonomous trading
run-autonomous-trader
```

### Web Interface Features
- Real-time market scanning visualization
- Interactive news sentiment analysis
- AI prediction generation with confidence bars
- Trading execution simulation
- Portfolio performance metrics

## 📊 Demo Data & Scenarios

### Simulated Market Data
- 5 diverse prediction markets across different categories
- Realistic pricing, volume, and spread data
- Time-based market expiration dates
- Category-based filtering and analysis

### News Sentiment Analysis
- 5 relevant news articles with realistic content
- Sentiment scores and relevance ratings
- Source attribution and publication timestamps
- Market correlation analysis

### AI Predictions
- Probabilistic forecasts with confidence intervals
- Edge detection versus current market prices
- Trade signal generation based on analysis
- Risk-adjusted position sizing recommendations

## 🔧 Technical Architecture

### Core Components
1. **Market Data Engine** - Fetches and processes market information
2. **News Sentiment Analyzer** - Processes news for market impact
3. **AI Prediction Engine** - Generates forecasts using multiple methodologies
4. **RAG Knowledge Base** - Stores and queries historical market data
5. **Trading Executor** - Manages trade execution and risk
6. **Portfolio Manager** - Tracks performance and optimization

### AI/ML Capabilities
- **Natural Language Processing** for news sentiment
- **Time Series Analysis** for market trends
- **Probabilistic Modeling** for uncertainty quantification
- **Reinforcement Learning** for trading optimization
- **Vector Search** for knowledge retrieval

## 📈 Expected Demo Results

### Performance Metrics
- **Expected ROI**: +3.88% on demo portfolio
- **Win Rate**: 73.2% based on AI predictions
- **Sharpe Ratio**: 1.84 (risk-adjusted returns)
- **Maximum Drawdown**: -8.5% (within risk parameters)

### Trading Summary
- **Markets Analyzed**: 5 comprehensive evaluations
- **Profitable Signals**: 3 trades with positive expected value
- **Portfolio Exposure**: $2,450 across diversified positions
- **Risk Management**: All positions within defined parameters

## ⚠️ Important Disclaimers

This is a **demonstration with simulated data** designed to showcase the capabilities of the Polymarket Agents framework. 

- **No Real Money**: All trading is simulated
- **Educational Purpose**: Designed to demonstrate AI trading concepts
- **Risk Warning**: Real prediction market trading involves significant risks
- **No Guarantees**: Past performance does not predict future results
- **Compliance**: Ensure compliance with local regulations before real trading

## 🛠️ Development & Extension

### Adding New Features
The demo is designed to be easily extensible:

1. **New Market Sources** - Add additional prediction market APIs
2. **Enhanced News Sources** - Integrate more news providers
3. **Advanced AI Models** - Incorporate latest LLM capabilities  
4. **Additional Risk Metrics** - Expand portfolio analytics
5. **Real-time Data** - Connect to live market feeds

### Custom Analysis
Users can extend the demo with:
- Custom prediction models
- Alternative risk management strategies
- Additional market categories
- Enhanced visualization tools

## 📞 Support & Resources

- **Documentation**: See `/docs` folder for detailed guides
- **Examples**: Check `/examples` for additional use cases
- **Issues**: Report bugs via GitHub issues
- **Discussions**: Join community discussions for questions

## 🙏 Acknowledgments

This demo builds upon the excellent work of:
- Polymarket team for the underlying prediction market infrastructure
- LangChain for AI/ML framework components
- Chroma for vector database capabilities
- OpenAI for language model integration

---

**Ready to explore the future of AI-powered prediction market trading?**

Run `python demo.py` to get started!