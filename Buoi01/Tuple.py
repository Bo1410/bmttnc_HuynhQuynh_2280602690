# Viết chương trình để tạo một Tuple từ một List nhập vào từ bàn phím.

def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input ("Nhập danh sách các số, cách nhau bằng dau phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ List:", my_tuple)