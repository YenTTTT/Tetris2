from colors import Colors
import pygame
from position import Position

# 定義 Block 類別
class Block:
    # 初始化方法，用來設定 Block 物件的屬性
    def __init__(self, id):
        self.id = id  # 區塊的識別id
        self.cells = {}  # 區塊的儲存格
        self.cell_size = 30  # 單一儲存格的尺寸
        self.row_offset = 0  # 行偏移量的初始值
        self.column_offset = 0  # 列偏移量的初始值
        self.rotation_state = 0  # 旋轉狀態的初始值
        self.colors = Colors.get_cell_colors()  # 取得儲存格顏色的字典

    # 移動方塊的方法，接受行和列的偏移量
    def move(self, rows, columns):
        self.row_offset += rows  # 將行偏移量增加指定的行數
        self.column_offset += columns  # 將列偏移量增加指定的列數

    # 獲取儲存格位置的方法
    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]  # 獲取當前旋轉狀態下的儲存格位置
        moved_tiles = []
        # 將每個儲存格的位置根據偏移量進行更新
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # 旋轉方塊的方法
    def rotate(self):
        self.rotation_state += 1
        # 如果旋轉狀態達到最大值，重置為初始值
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # 復原上一次旋轉的方法
    def undo_rotation(self):
        self.rotation_state -= 1
        # 如果旋轉狀態為負數，重置為最大旋轉狀態
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1


    # 繪製區塊的方法
    def draw(self, screen, offset_x, offset_y):
        # 取得當前旋轉狀態的儲存格列表
        tiles = self.get_cell_position()
        # 迭代每一個儲存格，繪製矩形
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)