import subprocess
import sys

# Thử import cv2, nếu chưa có thì tự động cài
try:
    import cv2
except ImportError:
    print("Chưa có thư viện cv2, đang cài đặt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
    import cv2
tenfile = "up_github.py"
# Mở webcam (0 là camera mặc định)
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Không mở được camera")
    sys.exit()

# Đọc một frame từ webcam
ret, frame = cam.read()

if ret:
    cv2.imwrite("photo.jpg", frame)
    print("Ảnh đã được chụp và lưu thành photo.jpg")
else:
    print("Không thể chụp ảnh")

# Giải phóng camera
cam.release()
print(f"Đang mở file {"up_github.py"}...")
subprocess.run([sys.executable, tenfile])

