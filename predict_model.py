import random

def predict_gold(close_prices):
    # 示例逻辑
    if len(close_prices) < 2:
        return "趋势不明确 🌈", "建议先观察 🤔"

    if close_prices[-1] > close_prices[-2]:
        return "上涨 📈", "建议买入 🛒"
    else:
        return "下跌 📉", "建议卖出 🚪"

