# Xây dựng một chương  trình  nhằm nhập số  giờ  làm việc  hàng tuần 
# của nhân viên  và  mức  lương theo giờ  tiêu  chuẩn. 
#Từ đó, thực hiện tính toán số tiền thực nhận của nhân viên. 
#Cần lưu ý rằng số giờ tiêu chuẩn mỗi tuần là 44 giờ, và mỗi giờ làm thêm sẽ được trả 150% so với mức lương theo giờ tiêu chuẩn.

so_gio_lam = float(input("Nhập số giờ làm việc mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mối giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")