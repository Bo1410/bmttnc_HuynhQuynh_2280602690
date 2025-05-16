# Tạo một chương trình để nhập vào hai số X và Y; 
# từ đó, xây dựng một mảng hai chiều.
# Giá trị của mỗi phần tử tại hàng i và cột j của mảng sẽ là i*j, 
# với i chạy từ 0 đến X-1 và j từ 0 đến Y-1. Chẳng hạn, 
# nếu X và Y được nhập là 3 và 5, thì kết quả sẽ là:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]. 
# Hướng dẫn: Tạo file “ex02_06.py” trong “lab_01”

input_str = input("Nhập X,Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
print(multilist)
