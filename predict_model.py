import random

def predict_gold():
    trend = random.choice(["上涨 📈", "下跌 📉"])
    timing = random.choice(["建议立即买入 🛒", "建议观望或撤出 🧯"])
    return trend, timing
