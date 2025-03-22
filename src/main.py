import pygame
import sys
from pygame.locals import *
from const import *
from game import *
pygame.init() # 对pygame进行初始化
# 创建窗口
DS = pygame.display.set_mode(GAME_SIZE)
game = Game(DS)
# 创建循环运行窗口
while True:
    for event in pygame.event.get():# 判断事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 事件类型==鼠标类型
            game.mouseClickHandler(event.button)    # 处理鼠标事件的方法    事件属性（1 代表左键，2 代表中键，3 代表右键）
    game.update()
    # 设置窗口颜色
    DS.fill((255,255,255))
    game.draw()
    pygame.display.update()# 帧更新


