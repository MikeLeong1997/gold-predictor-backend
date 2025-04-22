from flask import Flask, jsonify # type: ignore
from predict_model import predict_gold
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # 允许跨域请求（前端调用）

@app.route('/predict', methods=['GET'])
def predict():
    trend, timing = predict_gold()
    return jsonify({
        "trend": trend,
        "timing": timing
    })

if __name__ == '__main__':
    app.run(debug=True)

