from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__, static_folder='static')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/api/motos', methods=['POST'])
def receber_dados():
    data = request.get_json()
    print(f"📦 Dados recebidos: {data}")
    socketio.emit('nova_mensagem', data)
    return jsonify({"status": "OK"}), 200

@app.route('/')
def dashboard():
    return send_from_directory(app.static_folder, 'dashboard.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)
