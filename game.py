from grid import Grid
from blocks import *
import random
import pygame

# 定義 Game 類別
class Game:
    # 初始化方法，用來建立遊戲的初始狀態
    def __init__(self):
        # 創建遊戲網格和方塊列表，並設定當前方塊和下一個方塊
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        #EX模式"自動旋轉"
        self.revolve = False
        self.auto_rotato = False
        self.rotation_timer = pygame.time.get_ticks()  # 記錄上次旋轉的時間
        self.rotation_interval = 50  # 旋轉的間隔時間設置為 1000 毫秒
        
        pygame.mixer.music.load("Sounds/music.ogg")  #抓取音樂
        pygame.mixer.music.play(-1)  #聲音會一直重複跑

    # 更新分數的方法，根據消除的行數給予相應的分數，並加上方塊向下移動的分數
    def update_score(self, lines_cleared):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500

    # 隨機獲取一個方塊的方法
    def get_random_block(self):
        # 如果方塊列表為空，重新填充
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)  # 從方塊列表中隨機選擇一個方塊
        self.blocks.remove(block)  # 從方塊列表中移除已選擇的方塊
        return block

    # 向左移動當前方塊的方法
    def move_left(self):
        self.current_block.move(0, -1)
        # 如果方塊移動後超出邊界或無法適應網格，還原移動並鎖定方塊，還原移動並不執行移動
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    # 向右移動當前方塊的方法
    def move_right(self):
        self.current_block.move(0, 1)
        # 如果方塊移動後超出邊界或無法適應網格，還原移動並鎖定方塊，還原移動並不執行移動
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    # 向下移動當前方塊的方法
    def move_down(self):
        self.current_block.move(1, 0)
        # 如果方塊移動後超出邊界或無法適應網格，還原移動並鎖定方塊，還原移動並不執行移動
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # 將方塊固定在網格上的方法
    def lock_block(self):
        # 獲取當前方塊的儲存格位置
        tiles = self.current_block.get_cell_position()
        # 在網格上將方塊的 id 賦值給相應位置
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # 將當前方塊設定為下一個方塊，並生成新的下一個方塊
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        # 清除滿行並檢查新方塊是否適應
        rows_cleared = self.grid.clear_full_rows()
        # 更新分數）
        self.update_score(rows_cleared)
        #當方塊不再適應game_over = True
        if self.block_fits() == False:
            self.game_over = True
        if self.revolve == True:
            self.auto_rotato = True

    # 重置遊戲狀態的方法
    def reset(self):
        self.grid.reset()  # 重置網格內容
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # 重新生成所有方塊
        self.current_block = self.get_random_block()  # 獲取新的當前方塊
        self.next_block = self.get_random_block()  # 獲取新的下一個方塊
        self.score = 0

    # 檢查方塊是否適應於網格的方法
    def block_fits(self):
        # 獲取方塊的儲存格位置
        tiles = self.current_block.get_cell_position()
        # 檢查每個儲存格，如果有任何一個不為空，返回 False
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        # 所有儲存格都為空，返回 True
        return True


    #旋轉
    def ex_rotate(self):
        if self.auto_rotato:
            current_time = pygame.time.get_ticks()
            # 控制旋轉的時間間隔
            if current_time - self.rotation_timer >= self.rotation_interval:
                self.current_block.rotate()
                self.rotation_timer = current_time  # 更新上次旋轉的時間
        else:
            self.current_block.rotate()  # 呼叫當前方塊的旋轉方法
        # 如果方塊種動後超出邊界或無法適應網格，還原移動並鎖定方塊，還原移動並不執行移動
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    # 檢查方塊是否在網格內的方法
    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            # 如果方塊的某一個儲存格超出網格邊界，返回 False
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # 繪製遊戲畫面的方法
    def draw(self, screen):
        # 分別繪製網格和當前方塊
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        self.next_block.draw(screen, 270, 270)
