import tkinter as tk
from tkinter import filedialog
import requests

def encrypt_file():
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        key = input("Enter the encryption key: ")
        files = {'file': open(input_file_path, 'rb')}
        response = requests.post('http://127.0.0.1:5000/api/encrypt', data={'key': key}, files=files)
        encrypted_data = response.json()
        print("Encrypted Data:", encrypted_data)

def decrypt_file():
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        key = input("Enter the encryption key: ")
        data = {'key': key, 'encrypted_data': open(input_file_path, 'rb').read()}
        response = requests.post('http://127.0.0.1:5000/api/decrypt', json=data)
        decrypted_data = response.content.decode()
        print("Decrypted Data:", decrypted_data)

root = tk.Tk()
root.title("File Encryption Tool")

encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(pady=10)

root.mainloop()
