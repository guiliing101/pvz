import image
import time
import pygame
import data_object
class ObjectBase(image.Image):
    def __init__(self,id, pos):
        self.id = id
        self.hp = self.getData()['HP']    # 为什么没创建方法
        self.attack = self.getData()['ATT']    # 值是变化的不能直接取表里的值
        self.preIndexTime = 0
        self.prePositionTime = 0
        self.preSummonTime = 0
        super(ObjectBase, self).__init__(
        self.getData()['PATH'],
        0,
        pos,
        self.getData()['IMAGE_INDEX_MAX'],
        self.getData()['SIZE'])

    def getData(self): # 调用数据表里的id属性
        return data_object.data[self.id]

    def getImageIndexCD(self): # 根据id返回帧动画速率
        return self.getData()['IMAGE_INDEX_CD']

    def getPositionCD(self): # 根据id返回平移速率
        return self.getData()['POSITION_CD']

    def getSpeed(self):
        return self.getData()['SPEED']

    def getSummonCD(self):
        return self.getData()['SUMMON_CD']

    def canLoot(self):
        return self.getData()['CAN_LOOT']

    def getPrice(self):
        return self.getData()['PRICE']

    def isCollide(self, other):    # 碰撞箱检测
        return self.get_collision_rect().colliderect(other.get_collision_rect())

    def get_collision_rect(self, scale=0.7): # 碰撞箱会因图片影响导致太大
        # 返回缩小后的矩形，默认缩放为原始大小的70%
        rect = self.getRect()
        # 计算新矩形的宽高和位置
        new_width = rect.width * scale
        new_height = rect.height * scale
        new_rect = pygame.Rect(0, 0, new_width, new_height)
        new_rect.center = rect.center  # 保持中心点不变
        return new_rect

    def update(self):
        self.checkImageIndex()
        self.checkPosition()
        self.checkSummonCD()

    def checkSummonCD(self):
        if time.time() - self.preSummonTime <= self.getSummonCD():
            return
        self.preSummonTime = time.time()
        self.preSummon()
    # 帧动画实现
    def checkImageIndex(self): # 延时方法
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

# 平移实现
    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositionCD():
            return False
        self.prePositionTime = time.time()
        speed = self.getSpeed()
        self.pos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
        return True

    # 接口作用
    def preSummon(self):    # 在sunflower中重写
        pass

    def hasSummon(self):    # 在sunflower中重写
        pass

    def doSummon(self):    # 在sunflower中重写
        pass