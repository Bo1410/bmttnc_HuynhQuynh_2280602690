import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str, key: int) -> str:
        """
        Columnar Transposition:
        - Viết plaintext theo hàng, mỗi hàng dài 'key'.
        - Đọc lần lượt theo cột để tạo ciphertext.
        """
        columns = [''] * key                     # danh sách chuỗi cho từng cột

        for col in range(key):
            pointer = col
            while pointer < len(plaintext):
                columns[col] += plaintext[pointer]
                pointer += key                   # nhảy xuống ký tự cùng cột ở hàng kế

        return ''.join(columns)


    def decrypt(self, ciphertext: str, key: int) -> str:
        """
        Khôi phục lại lưới:
        - Số cột  = ceil(len(ciphertext) / key)
        - Số hàng = key
        - Tính số ô trống ở cột cuối cùng (shaded boxes) để tránh đọc lệch.
        """
        num_cols = math.ceil(len(ciphertext) / key)
        num_rows = key
        num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)

        # Khởi tạo list các chuỗi cho mỗi cột
        plaintext_cols = [''] * num_cols

        col = 0
        row = 0

        for symbol in ciphertext:
            plaintext_cols[col] += symbol
            col += 1

            # Khi hết cột, hoặc tới cột cuối nhưng hàng hiện tại vượt quá phần “ô trống”
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext_cols)
