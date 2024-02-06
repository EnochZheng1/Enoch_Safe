from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_file(key, input_file_path, output_file_path):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file_path, 'rb') as file_in:
        plaintext = file_in.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    with open(output_file_path, 'wb') as file_out:
        file_out.write(base64.b64encode(ciphertext))

def decrypt_file(key, iv, input_file_path, output_file_path):
    iv = base64.b64decode(iv)
    with open(input_file_path, 'rb') as file_in:
        ciphertext = base64.b64decode(file_in.read())
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_file_path, 'wb') as file_out:
        file_out.write(plaintext)

key = get_random_bytes(16)
