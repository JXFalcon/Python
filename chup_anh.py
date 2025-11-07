import cv2
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