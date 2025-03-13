import socket
from config import HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message to send: ")
        s.sendall(message.encode())  # Gửi tin nhắn đến server