from flask import Flask, jsonify # type: ignore
from predict_model import predict_gold
from flask_cors import CORS # type: ignore
import requests

app = Flask(__name__)
CORS(app)  # 允许跨域请求（前端调用）

@app.route('/predict', methods=['GET'])

def get_gold_prices_from_alpha_vantage():
    API_KEY = "EKHY164OMH9ZUGUP"
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=XAU&to_symbol=USD&apikey={API_KEY}'
    
    try:
        response = requests.get(url)
        data = response.json()

        # 拿最近5天的收盘价
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
    
        "trend": trend
        "timing": timing

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)

