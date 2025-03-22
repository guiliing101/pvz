# 豌豆射手
import objectbase
import peabullet
import time

class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(PeaShooter, self).__init__(id, pos)
        self.hasBullet = False  # 初始化是否发射子弹，初始值为False
        self.hasShoot = False   # 豌豆射手的动画加载到发射子弹时
    def hasSummon(self):  # 判断豌豆射手发射子弹的方法
        return self.hasBullet

    def preSummon(self):  # 发射子弹冷却时间到了
        self.hasShoot = True
        self.pathIndex = 0

    def doSummon(self):  # 执行发射子弹的方法
        if self.hasSummon():
            self.hasBullet = False  # 如果可以召唤，将hasBullet属性设置为False，表示已经发射过了
            return peabullet.PeaBullet(0, (self.pos[0]+self.size[0]-10, self.pos[1] + 30))  # 创建一个新的阳光对象，阳光强度为2，位置为向日葵位置偏移后的位置

    def checkImageIndex(self): # 延时方法
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx == 8 and self.pathIndex:
            self.hasBullet = True
        if idx >= self.pathIndexCount:
            idx = 9
        self.updateIndex(idx)