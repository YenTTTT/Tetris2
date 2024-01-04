import pygame
import sys
from game import Game
from colors import Colors

# 初始化pygame
pygame.init()

# 創建字型物件，字型大小為 40
title_font = pygame.font.Font(None, 40)
# 創建 "Score" 文字表面，文字顏色為白色
score_surface = title_font.render("Score", True, Colors.white)
# 使用 title_font 將遊戲分數轉換為表面，文字顏色為白色
# 創建 "Next" 文字表面，文字顏色為白色
next_surface = title_font.render("Next", True, Colors.white)
# 創建 "GAME OVER" 文字表面，文字顏色為白色
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
# 創建 Score 文字區域矩形
score_rect = pygame.Rect(320, 55, 170, 60)
# 創建 Next 文字區域矩形
next_rect = pygame.Rect(320, 215, 170, 180)

# 創建選單文字表面
menu_font = pygame.font.Font(None, 16)
easy_surface = menu_font.render("Easy", True, Colors.white)
normal_surface = menu_font.render("Normal", True, Colors.white)
hard_surface = menu_font.render("Hard", True, Colors.white)
EX_surface = menu_font.render("EX", True, Colors.white)
# 創建選單區域矩形
menu_rect = pygame.Rect(500, 5, 40, 40)
# 創建選單區域矩形
menu_rects = [
    pygame.Rect(480, 50, 60, 40),
    pygame.Rect(480, 91, 60, 40),
    pygame.Rect(480, 132, 60, 40),
    pygame.Rect(480,173,60,40),
]

# 創建時鐘物件，用於控制遊戲迴圈的速率
clock = pygame.time.Clock()

# 創建 Game 類別的物件
game = Game()

# 創建遊戲視窗
screen = pygame.display.set_mode((550, 620))
pygame.display.set_caption("俄羅斯方塊")

GAME_UPDATE = pygame.USEREVENT
menu_opened = False

# 遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 關閉遊戲視窗
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(event.pos):
                # 點擊在下拉式選單上，處理下拉選單的顯示/隱藏邏輯
                menu_opened = not menu_opened
            elif menu_opened:
                # 在下拉式選單打開的情況下，檢查點擊的位置
                for i, rect in enumerate(menu_rects):
                    game.revolve = False
                    game.auto_rotato = False
                    if rect.collidepoint(event.pos):
                        selected_difficulty = ["Easy", "Normal", "Hard","EX"][i]

                        # 根據選擇的難度設定速度
                        if selected_difficulty == "Easy":
                            SPEED = 200
                        elif selected_difficulty == "Normal":
                            SPEED = 150
                        elif selected_difficulty == "Hard":
                            SPEED = 120
                        elif selected_difficulty == "EX":
                            SPEED = 300
                            game.revolve = True
                            game.auto_rotato = True
                        pygame.time.set_timer(GAME_UPDATE, SPEED)  # 設定遊戲速度
                        menu_opened = False  # 關閉下拉式選單

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                if event.key == pygame.K_RETURN:
                    game.game_over=False    
                    game.reset()    #當遊戲結束時，game_over會設置為False
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()  # 按下左箭頭鍵，向左移動當前方塊
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()  # 按下右箭頭鍵，向右移動當前方塊
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()  # 按下下箭頭鍵，向下移動當前方塊
            if event.key == pygame.K_UP and game.game_over == False:
                game.ex_rotate()
                game.auto_rotato = False
        if event.type == GAME_UPDATE and game.auto_rotato == True and game.revolve == True and game.game_over == False:
            game.ex_rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()  # 定時觸發 GAME_UPDATE 事件，執行方塊向下移動
        

    # 繪製遊戲背景區

    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_blue)
    # 在視窗上繪製 "Score" 文字表面，位置為 (365, 20)
    screen.blit(score_surface, (365, 20))
    # 在視窗上繪製 "Next" 文字表面，位置為 (375, 180)
    screen.blit(next_surface, (375, 180))
    # 如果遊戲結束，則在視窗上繪製 "GAME OVER" 文字表面，位置為 (320, 450)
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450))

    # 繪製 Score 文字區域矩形，填充顏色為淺藍色
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    # 使用 blit 方法將分數值表面繪製到視窗上，並使其居中於 Score 文字區域矩形
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                  centery=score_rect.centery))
    # 繪製 Next 文字區域矩形，填充顏色為淺藍色
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # 繪製遊戲元素
    game.draw(screen)

    # 繪製下拉式選單按鈕
    pygame.draw.rect(screen, Colors.light_blue, menu_rect, border_radius=10)
    pygame.draw.polygon(screen, Colors.white, [(menu_rect.centerx - 10, menu_rect.centery - 5),
                                               (menu_rect.centerx + 10, menu_rect.centery - 5),
                                               (menu_rect.centerx, menu_rect.centery + 5)])

    # 繪製選單
    if menu_opened:
        for i, rect in enumerate(menu_rects):
            pygame.draw.rect(screen, Colors.white, rect, width=2)
            if i == 0:
                pygame.draw.rect(screen, Colors.light_blue, rect,border_top_left_radius=10, border_top_right_radius=10)
                screen.blit(easy_surface, (rect.centerx - easy_surface.get_width() // 2, rect.centery - easy_surface.get_height() // 2))
            elif i == 1:
                pygame.draw.rect(screen, Colors.light_blue, rect)
                screen.blit(normal_surface, (rect.centerx - normal_surface.get_width() // 2, rect.centery - normal_surface.get_height() // 2))
            elif i == 2:
                pygame.draw.rect(screen, Colors.light_blue, rect)
                screen.blit(hard_surface, (rect.centerx - hard_surface.get_width() // 2, rect.centery - hard_surface.get_height() // 2))
            elif i == 3:
                pygame.draw.rect(screen, Colors.light_blue, rect,border_bottom_left_radius=10, border_bottom_right_radius=10)
                screen.blit(EX_surface, (rect.centerx - EX_surface.get_width() // 2, rect.centery - EX_surface.get_height() // 2))

        
    # 更新遊戲視窗
    pygame.display.flip()

    # 控制遊戲迴圈的速率
    clock.tick(10)

