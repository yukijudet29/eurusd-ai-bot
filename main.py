from market_data import get_market_data
from strategy import analyze_market
from telegram_bot import send_message

import time
from datetime import datetime


def run_bot():

    print("AI Trading Bot Running...")

    while True:

        try:

            print("Analyzing EUR/USD Market...")

            df = get_market_data()

            analysis = analyze_market(df)

            signal = analysis['signal']

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            message = f"""
🚨 EURUSD AI MARKET UPDATE 🚨

Time: {current_time}

Action: {signal}

Entry Price: {analysis['price']}

Stop Loss: {analysis['stop_loss']}
Take Profit: {analysis['take_profit']}

Lot Size: {analysis['lot_size']}
Deviation: {analysis['deviation']}

RSI: {analysis['rsi']}

Win Probability: {analysis['confidence']}%
Loss Probability: {analysis['loss_probability']}%

Timeframe: 1 Minute
Strategy: EMA + RSI AI Analysis
"""

            send_message(message)

            print(message)

            # Wait 1 minute
            time.sleep(60)

        except Exception as e:

            print("Error:", e)

            time.sleep(60)


run_bot()