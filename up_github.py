import subprocess
import sys

def run_cmd(cmd):
    """Chạy lệnh shell và in ra kết quả"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

# ⚠️ Thay đổi các biến này cho phù hợp
repo_url = "https://github.com/JXFalcon/File_anh.git"   # link repo của bạn
branch = "main"                                        # nhánh muốn push
commit_message = "Upload all jpg images"               # nội dung commit

# 1. Khởi tạo git nếu chưa có
run_cmd("git init")

# 2. Thêm remote (chỉ cần làm 1 lần, sau đó có thể bỏ qua)
run_cmd("git remote remove origin")  # xoá remote cũ nếu có
run_cmd(f"git remote add origin {repo_url}")

# 3. Thêm tất cả ảnh JPG vào staging
run_cmd("git add *.jpg")

# 4. Commit
run_cmd(f'git commit -m "{commit_message}"')

# 5. Đặt nhánh chính
run_cmd(f"git branch -M {branch}")

# 6. Push lên GitHub
run_cmd(f"git push -u origin {branch}")
