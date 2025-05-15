import tkinter as tk
from tkinter import filedialog, messagebox
import binary_data_handler
import huffman
from tkinter import ttk
import time
import threading
import os

def update_ui():
        image_path_label.pack(pady=10)
        image_path_entry.pack(pady=5, fill=tk.X)
        browse_button.pack(pady=5)
        compress_button.pack(pady=5)
        decompress_button.pack(pady=5)
        compression_ratio_label.pack(pady=5)
        compression_time_label.pack(pady=5)

def browse_image_path():
    image_path = filedialog.askopenfilename(filetypes=[("Tệp hình ảnh", "*.jpg *.jpeg *.png *.bin")])
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, image_path)

def compress_image():
    def compress_in_thread():
        try:
            progress.start()
            start_time = time.time()
            
            image_path = image_path_entry.get()
            if not image_path:
                messagebox.showerror("Lỗi", "Vui lòng chọn tệp hình ảnh.")
                return
            
               # Hiển thị trạng thái đang xử lý
            compression_ratio_label.config(text="Đang nén...")
            compression_time_label.config(text="Thời gian nén: Đang tính...")
            root.update()  # Cập nhật giao diện ngay lập tức
            
            image_bit_string = binary_data_handler.read_image_bit_string(image_path)
            compressed_image_bit_string = huffman.compress_data(image_bit_string, './io/outputs/huffman_codes_image.txt')
            
            if compressed_image_bit_string:
                compressed_path = "io/outputs/compressed_image.bin"
                binary_data_handler.save_data(compressed_image_bit_string, compressed_path, 'image')
                compression_ratio = len(image_bit_string) / len(compressed_image_bit_string)
                compression_ratio_label.config(text=f"Tỷ lệ nén (CR): {compression_ratio:.2f}")
                
                elapsed_time = time.time() - start_time
                compression_time_label.config(text=f"Thời gian nén: {elapsed_time:.2f}s")
            else:
                messagebox.showerror("Lỗi", "Nén hình ảnh không thành công.")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi nén ảnh: {str(e)}")
        finally:
            progress.stop()
            
    # Tạo và khởi chạy luồng mới
    threading.Thread(target=compress_in_thread, daemon=True).start()
    
def decompress_image():
    compressed_path = "io/outputs/compressed_image.bin"
    compressed_image_bit_string = binary_data_handler.read_image_bit_string(compressed_path)

    if compressed_image_bit_string:
        huffman_codes_path = './io/outputs/huffman_codes_image.txt'
        huffman_codes = {}
        with open(huffman_codes_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                huffman_codes[key] = value

        decompressed_image_bit_string = huffman.decompress_data(compressed_image_bit_string, huffman_codes)
        decompressed_path = "io/outputs/decompressed_image.jpg"
        binary_data_handler.save_data(decompressed_image_bit_string, decompressed_path, 'image')
        decompression_complete_label.config(text="Giải nén hoàn tất!")
    else:
        messagebox.showerror("Lỗi", "Giải nén không thành công. Không tìm thấy hình ảnh đã nén.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Khai phá dữ liệu Nhóm 10")

# Tạo và thiết lập kiểu tùy chỉnh
style = ttk.Style()
style.theme_use("clam")  # Thay đổi thành 'clam' để có giao diện hiện đại hơn
root.configure(bg="#e0f7fa")  # Thiết lập màu nền

# Thiết lập kích thước cửa sổ (chiều rộng x chiều cao)
root.geometry("600x600")  # Tăng chiều cao cửa sổ để cải thiện bố cục

# Thêm một tiêu đề lớn
title_label = ttk.Label(root, text="Huffman Coding", font=("Arial", 18), background="#4dd0e1", foreground="white", padding=(10, 5))
title_label.pack(pady=10)

# Tạo và đặt các widget cho nén hình ảnh
image_path_label = ttk.Label(root, text="Đường dẫn hình ảnh:", background="#e0f7fa", font=("Arial", 12))
image_path_entry = ttk.Entry(root, font=("Arial", 12))
browse_button = ttk.Button(root, text="Chọn ảnh", command=browse_image_path, style='Accent.TButton')
compress_button = ttk.Button(root, text="Nén ảnh", command=compress_image, style='Accent.TButton')
decompress_button = ttk.Button(root, text="Giải nén", command=decompress_image, style='Accent.TButton')
compression_ratio_label = ttk.Label(root, text="Tỷ lệ nén (CR):", background="#e0f7fa", font=("Arial", 12))
compression_time_label = ttk.Label(root, text="Thời gian nén: 0.00s", background="#e0f7fa", font=("Arial", 12)) #New code
decompression_complete_label = ttk.Label(root, text="", background="#e0f7fa", font=("Arial", 12))

# Cấu hình kiểu cho nút
style.configure('Accent.TButton', background="#64b5f6", foreground="white", font=("Arial", 12), borderwidth=1)
style.map('Accent.TButton', background=[('active', '#42a5f5')])

progress = ttk.Progressbar(root, mode='indeterminate')
progress.pack(pady=5)

update_ui()
# Bắt đầu vòng lặp chính
root.mainloop()