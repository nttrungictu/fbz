# Sử dụng hình ảnh Python chính thức
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép các tệp yêu cầu vào container
COPY requirements.txt requirements.txt

# Cài đặt các gói yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Đặt biến môi trường để Flask chạy trên tất cả các giao diện mạng
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Mở cổng 8080 để truy cập ứng dụng Flask
EXPOSE 8080

# Chạy ứng dụng Flask
CMD ["python", "app.py"]