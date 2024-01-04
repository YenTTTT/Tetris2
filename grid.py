import pygame
from colors import Colors
class Grid:
    def __init__(self):
        # 初始化網格屬性
        self.num_rows = 20  # 網格行數
        self.num_cols = 10  # 網格列數
        self.cell_size = 30  # 每一個像素的單元格大小
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]  # 創建初始網格
        self.colors =Colors.get_cell_colors() # 取得所有顏色

    def print_grid(self):
        # 顯示網格的方法，用於測試和調試
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    # 判斷座標是否在網格內的方法
    def is_inside(self, row, column):
        # 如果座標在網格內，返回 True；否則返回 False
        if 0 <= row < self.num_rows and 0 <= column < self.num_cols:
            return True
        return False

    # 檢查網格的儲存格是否為空的方法
    def is_empty(self, row, column):
        # 如果儲存格為 0，表示為空，返回 True；否則返回 False
        if self.grid[row][column] == 0:
            return True
        return False

    # 檢查指定行是否滿行的方法
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # 清除指定行的方法
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # 將指定行向下移動指定行數的方法
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # 清除滿行並移動上方行的方法，返回被清除的行數
    def clear_full_rows(self):
        completed = 0
        # 由底部向上檢查每一行
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # 重置網格內容的方法
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0



    def draw(self, screen):
        # 繪製網格的方法
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                # 獲取單元格的值
                cell_value = self.grid[row][column]
                # 創建單元格的矩形
                cell_rect = pygame.Rect(column * self.cell_size +11, row * self.cell_size +11, self.cell_size -1, self.cell_size -1)
                # 以對應的顏色填充單元格
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
