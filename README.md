# Chat dựa trên Socket

Đây là một ứng dụng chat đơn giản dựa trên socket, cho phép nhiều client kết nối đến một server và trao đổi tin nhắn trong thời gian thực. Ứng dụng bao gồm ba thành phần chính: server, client và file cấu hình.

### Các thành phần
***1. Server (socket_server.py):***

Lắng nghe các kết nối từ client.

Xử lý nhiều client đồng thời bằng cách sử dụng threading.

Gửi tin nhắn nhận được từ một client đến tất cả các client khác đang kết nối.

***2. Client (socket_client.py):***

Kết nối đến server.

Cho phép người dùng nhập tin nhắn và gửi đến server, sau đó tin nhắn sẽ được gửi đến tất cả các client khác.

***3. Cấu hình (config.py):***

Chứa địa chỉ IP và cổng của server.

### Yêu cầu ###

Python 3.x

### Cài đặt ###

**1.** Clone repository:

```
git clone https://github.com/yourusername/socket-chat-app.git
cd socket-chat-app
```

**2.** Đảm bảo bạn đã cài đặt Python. Bạn có thể kiểm tra bằng cách chạy lệnh:

```
python --version
```

**3.** Không cần cài đặt thêm thư viện nào vì ứng dụng sử dụng các module có sẵn trong Python như socket và threading.

### Cách sử dụng ###

***1. Khởi động Server:***

Chạy script server:

```
python socket_server.py
```

Server sẽ bắt đầu lắng nghe trên địa chỉ IP và cổng được chỉ định (mặc định: 127.0.0.1:65432).

***2. Khởi động Client:***

Chạy script client trong một terminal khác:

```
python socket_client.py
```

Nhập tin nhắn trong terminal của client, tin nhắn sẽ được gửi đến server và chuyển tiếp đến tất cả các client khác đang kết nối.

***3. Nhiều Client:***

Bạn có thể khởi động nhiều client bằng cách chạy socket_client.py trong các terminal khác nhau. Mỗi client sẽ có thể gửi và nhận tin nhắn.

### Cấu hình ###

Địa chỉ IP và cổng của server có thể được cấu hình trong file config.py:

```
HOST = '127.0.0.1'  # Địa chỉ IP của server
PORT = 65432        # Cổng của server
```

