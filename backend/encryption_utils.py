from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_file(key, file):
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    plaintext = file.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    encrypted_data = base64.b64encode(iv + ciphertext)
    return encrypted_data

def decrypt_file(key, encrypted_data):
    iv_cipher_text = base64.b64decode(encrypted_data)
    iv = iv_cipher_text[:AES.block_size]
    cipher_text = iv_cipher_text[AES.block_size:]
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plaintext.decode()
