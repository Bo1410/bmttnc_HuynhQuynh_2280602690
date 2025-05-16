def tinh_tong(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong(numbers)
print("Tổng chẵn là: ", tong_chan)
