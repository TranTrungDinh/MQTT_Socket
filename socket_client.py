import socket

HOST = '127.0.0.1'  # Địa chỉ IP của máy chủ
PORT = 65432        # Cổng mà server đang lắng nghe

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message to send: ")
        s.sendall(message.encode())  # Gửi tin nhắn đến server