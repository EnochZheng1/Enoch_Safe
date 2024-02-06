from flask import Flask, request, jsonify
from encryption_utils import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    key = request.form.get('key', None)

    if not key:
        return jsonify({'error':'Encryption key not provided'}), 400

    encrypted_data = encrypt_file(key, file)
    return jsonify({'encrypted_data': encrypted_data.decode()}), 200

@app.route('/api/descrypt', methods=['POST'])
def decrypt():
    data = request.json
    key = data.get('key', None)
    encrypted_data = data.get('encrypted_data', None)

    if not key or not encrypted_data:
        return jsonify({'error': 'Encryption key or encrypted data not provided'}), 400

    decrypted_data = decrypt_file(key, encrypted_data.encode())
    return decrypted_data, 200

if __name__ == '__main__':
    app.run(debug=True)

