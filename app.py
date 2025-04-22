import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_gold_prices_from_alpha_vantage():
    API_KEY = "8BR6P0HMAI2Y6977"
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=XAU&to_symbol=USD&apikey={API_KEY}'
    
    try:
        response = requests.get(url)
        data = response.json()
        time_series = data.get("Time Series FX (Daily)", {})
        sorted_dates = sorted(time_series.keys(), reverse=True)
        close_prices = []

        for date in sorted_dates[:5]:
            close = float(time_series[date]["4. close"])
            close_prices.append(close)

        return close_prices
    except Exception as e:
        print("获取 Alpha Vantage 数据失败:", e)
        return []

@app.route("/predict", methods=["GET"])
def predict():
    close_prices = get_gold_prices_from_alpha_vantage()

    if not close_prices:
        return jsonify({
            "close_prices": [],
            "trend": "❓ 无法判断",
            "suggestion": "❌ 无法获取预测数据"
        })

    if close_prices[-1] > close_prices[0]:
        trend = "上涨 📈"
        suggestion = "建议买入 🛒"
    else:
        trend = "下跌 📉"
        suggestion = "建议观望 🧘"

    return jsonify({
        "close_prices": close_prices,
        "trend": trend,
        "suggestion": suggestion
    })

@app.route("/auto_trade", methods=["GET"])
def auto_trade():
    close_prices = get_gold_prices_from_alpha_vantage()
    
    if not close_prices:
        return jsonify({
            "action": "❌ 获取数据失败，无法下单"
        })

    if close_prices[-1] > close_prices[0]:
        action = "🟢 自动执行买入操作（模拟）"
    else:
        action = "🟡 趋势不明确，暂不操作"

    return jsonify({
        "close_prices": close_prices,
        "action": action
    })

if __name__ == "__main__":
    app.run(debug=True)
app.run(host='0.0.0.0', port=5000)

