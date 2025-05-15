import os

# Đọc file ảnh và chuyển thành chuỗi bit (mỗi byte thành 8 bit)
def read_image_bit_string(image_path):
    bit_string = ""
    with open(image_path, 'rb') as image:
        byte = image.read(1) # Đọc từng byte
        while byte:
            byte_value = ord(byte)
            bits = bin(byte_value)[2:].rjust(8, '0')  # Chuyển thành 8 bit
            bit_string += bits
            byte = image.read(1)
    return bit_string

# Lưu dữ liệu theo các định dạng khác nhau 
def save_data(data, path, data_type):
    if data_type == 'image':
        # Chuyển đổi chuỗi bit thành các byte và ghi vào tệp
        byte_array = bytearray(int(data[i:i+8], 2) for i in range(0, len(data), 8))
        with open(path, 'wb') as file:
            file.write(byte_array)  # Lưu dữ liệu dưới dạng nhị phân
    elif data_type == 'dictionary':
        with open(path, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}:{value}\n")  # Lưu từ điển dưới dạng văn bản
    elif data_type == 'text':
        with open(path, 'wb') as file:
            file.write(data.encode())  # Lưu chuỗi văn bản dưới dạng nhị phân
    else:
        raise ValueError("Kiểu dữ liệu không hợp lệ. Các giá trị hỗ trợ: 'image', 'dictionary', 'text'")
