# 封装图片
import pygame
class Image(pygame.sprite.Sprite):
    def     __init__(self, pathFmt, pathIndex, pos, pathIndexCount = 0, size = None):
        self.pathFmt = pathFmt    # 格式化的路径
        self.pathIndex = pathIndex    # 图片的编号
        self.pathIndexCount = pathIndexCount    # 编号的上限
        self.size = size    # 图片大小
        self.pos = list(pos)    # 图片位置
        self.updateImage()
        # self.collision_scale = collision_scale  # 碰撞箱缩放比例（0.8 表示缩小到 80%）

    #加载图片路径更新图片，如果路径中有变量（%d）可以通过索引选择不同的图片
    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:    # 如果路径需要动态编号
            path = path % self.pathIndex
        self.image = pygame.image.load(path)    # 加载图片
        if self.size:    # 如果有指定的缩放尺寸
            self.image = pygame.transform.scale(self.image, self.size)    # 缩放

    # 用于动态图片的更新，重新加载图片
    def updateSize(self,size):
        self.size = size    # 设置尺寸
        self.updateImage()    #更新图片

    # pathIndex编号是一个变量，编写一个函数来控制编号的变量
    def updateIndex(self,pathIndex):
        self.pathIndex = pathIndex    # 更新索引路径
        self.updateImage()    #更新图片

    # 获取这个矩形
    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect
    def doLeft(self):
        self.pos[0] -= 0.3    # 改变图片平移的速度
    # 绘制函数
    def draw(self, ds):
        ds.blit(self.image, self.getRect())