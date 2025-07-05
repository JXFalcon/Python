dulieu = []  # Danh sách chứa các tên sách

def lobby():
    while True:
        print("\n===== MENU QUẢN LÝ SÁCH =====")
        print("1. Hiển thị danh sách sách")
        print("2. Thêm sách")
        print("3. Xóa sách")
        print("4. Tìm kiếm sách")
        print("5. Thay đổi sách")
        print("6. Đếm số lượng sách")
        print("7. Sắp xếp danh sách sách")
        print("8. Lưu danh sách vào file")
        print("9. Đọc danh sách từ file")
        print("10. Tìm sách theo từ khóa (gần đúng)")
        print("11. Thoát chương trình")

        nhapmenu = input("Chọn chức năng (1-10): ")

        if nhapmenu == "1":
            print("\nDanh sách sách:")
            if dulieu:
                for sach in dulieu:
                    print("- " + sach)
            else:
                print("Danh sách trống.")

        elif nhapmenu == "2":
            tensach = input("Nhập tên sách mới: ")
            dulieu.append(tensach)
            print("Đã thêm sách:", tensach)

        elif nhapmenu == "3":
            tensach = input("Nhập tên sách cần xóa: ")
            if tensach in dulieu:
                dulieu.remove(tensach)
                print("Đã xóa sách:", tensach)
            else:
                print("Không tìm thấy sách trong danh sách.")

        elif nhapmenu == "4":
            tensach = input("Nhập tên sách cần tìm: ")
            if tensach in dulieu:
                print("Sách có trong danh sách:", tensach)
            else:
                print("Không tìm thấy sách.")

        elif nhapmenu == "5":
            tensach_cu = input("Nhập tên sách cần thay đổi: ")
            if tensach_cu in dulieu:
                tensach_moi = input("Nhập tên sách mới: ")
                dulieu[dulieu.index(tensach_cu)] = tensach_moi
                print("Đã cập nhật sách:", tensach_cu, "=>", tensach_moi)
            else:
                print("Không tìm thấy sách.")

        elif nhapmenu == "6":
            print("Tổng số sách trong danh sách:", len(dulieu))

        elif nhapmenu == "7":
            if dulieu:
                dulieu.sort()
                print("Đã sắp xếp danh sách theo thứ tự A-Z.")
            else:
                print("Danh sách trống.")

        elif nhapmenu == "8":
            with open("sach.txt", "w", encoding="utf-8") as f:
                for sach in dulieu:
                    f.write(sach + "\n")
            print("Đã lưu danh sách vào 'sach.txt'.")

        elif nhapmenu == "9":
            try:
                with open("sach.txt", "r", encoding="utf-8") as f:
                    dulieu.clear()
                    dulieu.extend([line.strip() for line in f])
                print("Đã đọc dữ liệu từ 'sach.txt'.")
            except FileNotFoundError:
                print("File 'sach.txt' chưa tồn tại.")
        elif nhapmenu == "10":
            print("Chức năng: Tìm sách theo từ khóa gần đúng.")
            tu_khoa = input("Nhập từ khóa cần tìm: ").lower()
            ket_qua = []

            for sach in dulieu:
                if tu_khoa in sach.lower():
                    ket_qua.append(sach)

            if ket_qua:
                print("Các sách tìm thấy:")
                for s in ket_qua:
                    print("- " + s)
            else:
                print("Không tìm thấy sách nào phù hợp.")
        elif nhapmenu == "11":
            print("Đã thoát chương trình. Hẹn gặp lại!")
            break   

        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 10.")

lobby()