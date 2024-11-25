from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Настройка метрик
metrics = PrometheusMetrics(app)

# Добавляем метки с корректным использованием request.path
metrics.info('app_info', 'Application Info', version='1.0.0')
metrics.default_labels = {
    'method': lambda: request.method,
    'path': lambda: request.path,  # Здесь исправлено
    'status': lambda response: response.status_code
}

# Маршрут, возвращающий 404 ошибку
@app.route('/not-found')
def not_found():
    return jsonify({"error": "Resource not found"}), 404

# Маршрут, возвращающий 500 ошибку
@app.route('/server-error')
def server_error():
    return jsonify({"error": "Internal server error"}), 500

# Маршрут, возвращающий 400 ошибку
@app.route('/bad-request')
def bad_request():
    return jsonify({"error": "Bad request"}), 400

# Здоровье приложения
@app.route('/')
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
