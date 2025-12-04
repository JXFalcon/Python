import cv2

# Mở webcam (0 là camera mặc định)
cam = cv2.VideoCapture(0)

# Kiểm tra xem camera có mở được không
if not cam.isOpened():
    print("Không mở được camera")
    exit()

# Đọc một frame từ webcam
ret, frame = cam.read()

if ret:
    # Lưu ảnh chụp thành file
    cv2.imwrite("photo.jpg", frame)
    print("Ảnh đã được chụp và lưu thành photo.jpg")
else:
    print("Không thể chụp ảnh")

# Giải phóng camera
cam.release()
