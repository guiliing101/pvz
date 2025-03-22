import image
import pygame
import sunflower
import peashooter
import time
import zombiebase
import data_object
import random
from const import *
class Game(object):
    def __init__(self,ds):
        self.ds = ds
        # 加载背景
        self.back = image.Image(PATH_BACK, 0, (0,0), 0, GAME_SIZE)
        # 结束图片：僵尸吃掉你的脑子
        self.lose = image.Image(PATH_LOSE, 0, (0,0), 0, GAME_SIZE)
        # 游戏是否结束
        self.isGameOver = False
        # 用于存放游戏中植物的列表
        self.plants = []
        # 用于存放游戏中召唤物的列表
        self.summons = []
        self.hasPlant = []
        # 用于存放僵尸的列表
        self.zombies = []
        # 阳光设定 初始100
        self.gold = 100
        # 对阳光的文字显示
        self.goldFont = pygame.font.Font(None, 60)
        # 分数设定 初始0
        self.zombie = 0
        # 对打僵尸分数显示
        self.zombieFont = pygame.font.Font(None, 60)
        # 僵尸生成int化
        self.zombieGenertateTime = 0
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def renderFont(self):
        # 阳光显示
        textImage = self.goldFont.render("Gold:" + str(self.gold), True, (0,0,0))
        self.ds.blit(textImage, (13, 23))
        textImage = self.goldFont.render("Gold:" + str(self.gold), True, (255, 255, 255))
        self.ds.blit(textImage, (10, 23))
        # 分数显示
        textImage = self.zombieFont.render("Score:" + str(self.zombie), True, (0, 0, 0))
        self.ds.blit(textImage, (13, 83))
        textImage = self.zombieFont.render("Score:" + str(self.zombie), True, (255, 255, 255))
        self.ds.blit(textImage, (10, 83))
    # 绘制游戏的方法
    def draw(self):
        # 绘制背景
        self.back.draw(self.ds)
        # 遍历植物列表绘制植物
        for plant in self.plants:
            plant.draw(self.ds)
        # 遍历召唤物列表绘制召唤物
        for summon in self.summons:
            summon.draw(self.ds)
        # 遍历僵尸列表绘制僵尸
        for zombie in self.zombies:
            zombie.draw(self.ds)
        self.renderFont()
        if self.isGameOver:
            self.lose.draw(self.ds)

    # 跟新游戏状态
    def update(self):
        # 更新游戏背景状态
        self.back.update()
        # 遍历植物列表更新每个植物的状态
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():   # 检查植物是否可以召唤新对象
                summ = plant.doSummon() # 获取召唤的对象
                self.summons.append(summ)   # 将召唤的对象添加到summon列表
        # 遍历召唤物列表更新每个召唤物的状态
        for summon in self.summons:
            summon.update()
        for zombie in  self.zombies:
            zombie.update()
        # 设置僵尸的刷新时间
        if time.time() - self.zombieGenertateTime > 10:
            self.zombieGenertateTime = time.time()
            self.addZombie(ZOMBIE_BORN_X, random.randint(0, GRID_COUNT[1]-1))
        # 召唤物VS僵尸
        self.checkSummonVSZombie()
        # 僵尸VS植物
        self.checkZombieVSPlant()

        for zombie in self.zombies:
            if zombie.getRect().x < 0:
                self.isGameOver = True

        # 防止召唤物内存泄露
        for summon in self.summons:
            if summon.getRect().x > GAME_SIZE[0] or summon.getRect().y > GAME_SIZE[1]:
                self.summons.remove(summon)
                break   # 被删除掉元素的表已经不是原来的表里继续使用会出现非预期的后果

    def checkSummonVSZombie(self):
        for summon in self.summons:
            for zombie in self.zombies:
                if summon.isCollide(zombie):
                    self.fight(summon, zombie)
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
                        self.zombie += 1
                    if summon.hp <= 0:
                        self.summons.remove(summon)
                    return

    def checkZombieVSPlant(self):
        for zombie in self.zombies:
            for plant in self.plants:
                if zombie.isCollide(plant):
                    self.fight(zombie, plant)
                    if plant.hp <= 0:
                        self.plants.remove(plant)
                        break


    def getIndexByPos(self, pos):   # 获取鼠标的格子位置
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def addSunFlower(self, x, y):   # 种植向日葵
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflower.SunFlower(SUNFLOWER_ID, pos)
        self.plants.append(sf)

    def addPeaShooter(self, x, y):   # 种植豌豆射手
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = peashooter.PeaShooter(PEASHOOTER_ID, pos)
        self.plants.append(sf)

    def addZombie(self, x, y):  # 生成僵尸
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        zm = zombiebase.ZombieBase(1, pos)
        self.zombies.append(zm)

    def fight(self, a, b):
        while True:
            a.hp -= b.attack
            b.hp -= a.attack
            if b.hp <= 0:
                return True
            if a.hp <= 0:
                return False
        return False

    def checkLoot(self, mousePos):    # 捡阳光
        for summon in self.summons:
            if not summon.canLoot():
                continue
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold += summon.getPrice()
                return True
        return False

    def checkAddPlant(self, mousePos, objId):    # 种植物
        x, y = self.getIndexByPos(mousePos)
        # 限制只能在格子里种植
        if x < 0 or x >= GRID_COUNT[0]:
            return
        if y < 0 or y >= GRID_COUNT[1]:
            return
        if self.gold < data_object.data[objId]['PRICE']:    # 判断金钱不满足
            return
        if self.hasPlant[x][y] == 1:    # 判断格子是否有植物
            return
        self.hasPlant[x][y] = 1
        self.gold -= data_object.data[objId]['PRICE']
        if objId == SUNFLOWER_ID:
            self.addSunFlower(x, y)
        if objId == PEASHOOTER_ID:
            self.addPeaShooter(x, y)

    def mouseClickHandler(self, btn):
        if self.isGameOver == True:
            return
        mousePos = pygame.mouse.get_pos()   # 获取当前鼠标的位置
        if self.checkLoot(mousePos):
            return
        if btn == 1:
            self.checkAddPlant(mousePos, SUNFLOWER_ID)
        if btn == 3:
            self.checkAddPlant(mousePos, PEASHOOTER_ID)