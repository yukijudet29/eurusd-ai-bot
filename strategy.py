import ta


def analyze_market(df):

    df['ema50'] = ta.trend.ema_indicator(df['close'], window=50)
    df['ema200'] = ta.trend.ema_indicator(df['close'], window=200)
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)

    latest = df.iloc[-1]

    current_price = round(latest['close'], 5)

    signal = "HOLD"
    confidence = 50

    if latest['ema50'] > latest['ema200'] and latest['rsi'] > 55:
        signal = "BUY"
        confidence = 75

    elif latest['ema50'] < latest['ema200'] and latest['rsi'] < 45:
        signal = "SELL"
        confidence = 75

    # Risk Management

    if signal == "BUY":

        stop_loss = round(current_price - 0.0020, 5)

        take_profit = round(current_price + 0.0040, 5)

    elif signal == "SELL":

        stop_loss = round(current_price + 0.0020, 5)

        take_profit = round(current_price - 0.0040, 5)

    else:

        stop_loss = current_price

        take_profit = current_price

    lot_size = 0.01

    deviation = 20

    return {
        "signal": signal,
        "confidence": confidence,
        "loss_probability": 100 - confidence,
        "rsi": round(latest['rsi'], 2),
        "price": current_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "lot_size": lot_size,
        "deviation": deviation
    }