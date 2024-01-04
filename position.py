# 定義名為 Position 的類別，表示在二維網格中的位置
class Position:
    # 初始化方法，接受行數（row）和列數（column）作為參數
    def __init__(self, row, column):
        self.row = row  # 物件的行數屬性
        self.column = column  # 物件的列數屬性