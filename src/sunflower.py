# 向日葵
import objectbase
import sunlight


class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(SunFlower, self).__init__(id, pos)
        self.hasSunlight = False  # 初始化向日葵是否有阳光的属性，初始值为False

    def hasSummon(self):  # 判断向日葵是否可以召唤阳光的方法
        return self.hasSunlight

    def preSummon(self):  # 准备召唤阳光的方法
        self.hasSunlight = True

    def doSummon(self):  # 执行召唤阳光的方法
        if self.hasSummon():
            self.hasSunlight = False  # 如果可以召唤，将hasSunlight属性设置为False，表示已经召唤过了
            return sunlight.SunLight(2, (self.pos[0] + 20, self.pos[1] - 10))  # 创建一个新的阳光对象，阳光强度为2，位置为向日葵位置偏移后的位置
