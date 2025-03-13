import socket
import threading

HOST = '127.0.0.1'  # Địa chỉ IP của máy chủ
PORT = 65432        # Cổng mà server sẽ lắng nghe

clients = []  # Danh sách để lưu trữ các kết nối client

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    clients.append(conn)  # Thêm client vào danh sách
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # In ra tin nhắn nhận được
            print(f"Received message from {addr}: {data.decode()}")
            # Gửi tin nhắn đến tất cả các client
            for client in clients:
                if client != conn:  # Không gửi lại cho chính client đã gửi
                    client.sendall(data)
    finally:
        conn.close()
        clients.remove(conn)  # Xóa client khỏi danh sách khi ngắt kết nối

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()