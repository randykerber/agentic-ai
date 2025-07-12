#!/usr/bin/env python3
"""
Quick test to run Lab 3 trading system once
"""
import asyncio
from traders import Trader
from tracers import LogTracer
from agents import add_trace_processor
from market import is_market_open
from dotenv import load_dotenv

load_dotenv(override=True)

async def test_single_trading_cycle():
    """Run a single trading cycle for testing"""
    print("🏁 Starting Lab 3 Trading Floor Test")
    
    # Add tracing
    add_trace_processor(LogTracer())
    
    # Create a single trader for testing
    trader = Trader("Warren", "Patience", "gpt-4o-mini")
    print(f"📊 Created trader: {trader.name} {trader.lastname}")
    
    # Check market status
    market_open = is_market_open()
    print(f"🏛️ Market is open: {market_open}")
    
    if not market_open:
        print("⚠️ Market is closed, but running anyway for testing...")
    
    try:
        print("🚀 Running trader...")
        await trader.run()
        print("✅ Single trading cycle completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during trading: {e}")
        raise

if __name__ == "__main__":
    print("🧪 Testing Lab 3 Trading System")
    asyncio.run(test_single_trading_cycle())
    print("🎉 Test completed!")