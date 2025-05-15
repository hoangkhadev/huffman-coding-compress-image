## Nén ảnh bằng huffman

### Tổng quan

- **main.py**:
  Tệp "main.py" đóng vai trò là điểm khởi đầu của chương trình. Nó nhận đường dẫn ảnh đầu vào và điều phối việc gọi các chức năng được mô tả trong các thành phần khác của chương trình. Các chức năng này kết thúc bằng việc nén và giải nén ảnh thông qua ứng dụng các nguyên tắc mã hóa Huffman.

- **huffman.py**:
  Module "huffman.py" chứa các hàm thực hiện mã hóa Huffman một cách cẩn thận. Các hàm này bao gồm việc tính toán tần suất byte trong ảnh đầu vào, xây dựng cây Huffman, lấy mã Huffman, và thiết lập liên kết byte với mã. Thông qua các thuật toán này, mã hóa Huffman được thực hiện, tối ưu hóa việc biểu diễn dữ liệu với sự quan tâm đến phân bố tần suất ký tự.

- **binary_data_handler.py**:
  Module "binary_data_handler.py" quản lý dữ liệu nhị phân. Nó bao gồm các hàm để đọc và ghi các tệp hình ảnh. Dữ liệu nhị phân được đọc từ ảnh và kết quả nén hoặc giải nén sẽ được ghi vào tệp đầu ra.

### Hướng dẫn cài đặt

- **Bước 1: Cài đặt**
  - 1. Clone repo:
       `https://github.com/hoangkhadev/huffman-coding-compress-image.git`
- **Bước 2: cài đặt thêm**
  - 1. Đảm bảo bạn đã cài đặt Python 3.x trên máy tính.
  - 2. Cài đặt các gói phụ thuộc bằng cách chạy lệnh.
- **Step 3: Sử dụng**

  - 1. Khởi chạy công cụ bằng lệnh: `python main.py`
  - 2. Nén một ảnh:
       Chọn ảnh mà bạn muốn nén.
       Nhấn nút "Nén ảnh" trong giao diện.
       Công cụ sẽ xử lý ảnh bằng thuật toán Huffman và lưu kết quả ảnh đã nén trong thư mục io/outputs
  - 3. Giải nén một ảnh:
       Chọn tệp ảnh nén mà bạn muốn giải nén.
       Nhấn nút "Giải nén ảnh" trong giao diện.
       Công cụ sẽ khôi phục ảnh gốc từ dữ liệu nén và lưu kết quả giải nén trong thưc mục io/outputs.

- **Bước 4: Kiểm tra**
  - Huffman Codes:
    Công cụ này tạo ra các mã Huffman cho mỗi ký hiệu trong quá trình nén. Bạn có thể tìm thấy các mã này trong tệp "huffman_codes_image.txt", tệp nén "compressed_image.bin" và ảnh sau khi giải nén tệp "decompressed_image.jpg" nằm trong thư mục "IO/Outputs.
