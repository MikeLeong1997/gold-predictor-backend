import random

close_prices = get_gold_prices_from_alpha_vantage()
if not close_prices:
    print("获取黄金数据失败，请稍后重试")
