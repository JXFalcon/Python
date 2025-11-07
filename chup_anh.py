import subprocess
import sys
import cv2
def cai_thu_vien(ten_thu_vien):
    try:
        __import__(ten_thu_vien)
        print(f"✅ Đã có thư viện '{ten_thu_vien}'")
    except ImportError:
        print(f"📦 Đang cài thư viện '{ten_thu_vien}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", ten_thu_vien])
# Mở webcam (0 là camera mặc định)
cam = cv2.VideoCapture(0)

# Chờ camera khởi động
ret, frame = cam.read()

if ret:
    cv2.imwrite("anh_chup.jpg", frame)
    print("✅ Đã chụp ảnh và lưu vào 'anh_chup.jpg'")
else:
    print("❌ Không thể truy cập camera.")

cam.release()
