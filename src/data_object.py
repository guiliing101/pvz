# 用于存放各种数据
data = {
    #子弹
    0:{
        'PATH' : "D:/86157/app/PyCharm Community Edition 2023.2.1/python/pz/pic/other/peabullet.png",
        'IMAGE_INDEX_MAX' : 0,
        'IMAGE_INDEX_CD' : 0,
        'POSITION_CD' : 0.008,
        'SUMMON_CD': -1,
        'SIZE' : (42,42),
        'SPEED' : (4,0),
        'CAN_LOOT' : False,
        'PRICE' : 0,
        'HP' : 1,
        'ATT' : 1,
    },
    # 僵尸
    1:{
        'PATH' : "D:/86157/app/PyCharm Community Edition 2023.2.1/python/pz/pic/zombie/0/%d.png", # 路径
        'IMAGE_INDEX_MAX' : 15, # 图片帧动画最大值
        'IMAGE_INDEX_CD' :  0.2, # 帧动画速率
        'POSITION_CD' : 0.2, # 平移速率
        'SUMMON_CD': -1,
        'SIZE' : (100,128), # 大小
        'SPEED' : (-20.5,0), # 平移位移
        'CAN_LOOT' : False, # 拾取判断
        'PRICE' : 0,
        'HP': 5,
        'ATT': 1,
    },
    # 阳光
    2:{
        'PATH' : "D:/86157/app/PyCharm Community Edition 2023.2.1/python/pz/pic/other/sunlight/%d.png",
        'IMAGE_INDEX_MAX' : 30,
        'IMAGE_INDEX_CD' :  0.06,
        'POSITION_CD' : 0.05,
        'SUMMON_CD' : -1,
        'SIZE' : (80,60),
        'SPEED' : (0,2),
        'CAN_LOOT' : True,
        'PRICE': 25,
        'HP': 10000000,
        'ATT': 0,
    },
    # 向日葵
    3:{
        'PATH' : "D:/86157/app/PyCharm Community Edition 2023.2.1/python/pz/pic/plant/sunflower/%d.png",
        'IMAGE_INDEX_MAX' : 19,
        'IMAGE_INDEX_CD' :  0.06,
        'POSITION_CD' : 1000000,
        'SUMMON_CD' : 8,
        'SIZE' : (128,128),
        'SPEED' : (0,0),
        'CAN_LOOT': False,
        'PRICE': 50,
        'HP': 5,
        'ATT': 0,
    },
    # 豌豆射手
    4:{
        'PATH' : "D:/86157/app/PyCharm Community Edition 2023.2.1/python/pz/pic/plant/peashooter/%d.png",
        'IMAGE_INDEX_MAX' : 15,
        'IMAGE_INDEX_CD' :  0.15,
        'POSITION_CD' : 1000000,
        'SUMMON_CD' : 3,
        'SIZE' : (128,128),
        'SPEED' : (0,0),
        'CAN_LOOT': False,
        'PRICE': 100,
        'HP': 5,
        'ATT': 0,
    },
}