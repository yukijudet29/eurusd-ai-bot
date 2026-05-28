
def calculate_lot_size(balance, risk_percent):

    risk_amount = balance * (risk_percent / 100)

    lot_size = risk_amount / 100

    return round(lot_size, 2)