from django.shortcuts import render
import random
# Create your views here.


def showtime(request):
    hero = {
        "border":[
            {
                "pic":"images/剑魔.jpg",
                "design":"暗裔剑魔",
                "name": "淹不死的鱼",
                "head": "images/tx1.jpg",
                "sk1": "images/传送.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60,100),
                "load": "{}%".format(random.randint(60,100))
             },
            {
                "pic": "images/猪妹.jpg",
                "design": "凛冬之怒",
                "name": "千叶雨耕",
                "head": "images/tx2.jpg",
                "sk1": "images/惩戒.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60,100),
                "load": "{}%".format(random.randint(60,100))
            },
            {
                "pic": "images/亚索.jpg",
                "design": "疾风剑豪",
                "name": "浪子彦",
                "head": "images/tx3.jpg",
                "sk1": "images/引燃.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/女警.jpg",
                "design": "皮城女警",
                "name": "夏若繁华似锦",
                "head": "images/tx4.jpg",
                "sk1": "images/治疗.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/悠米.jpg",
                "design": "魔法猫咪",
                "name": "陽光腐朽了心",
                "head": "images/tx5.jpg",
                "sk1": "images/闪现.jpg",
                "sk2": "images/虚弱.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            }
        ],
        "up": [
            {
                "pic": "images/剑姬.jpg",
                "design": "无双剑姬",
                "name": "流星不再流泪",
                "head": "images/tx6.jpg",
                "sk1": "images/闪现.jpg",
                "sk2": "images/引燃.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/酒桶.jpg",
                "design": "古拉加斯",
                "name": "时光会反光",
                "head": "images/tx7.jpg",
                "sk1": "images/惩戒.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/蚂蚱.jpg",
                "design": "马尔扎哈",
                "name": "写意东风事",
                "head": "images/tx8.jpg",
                "sk1": "images/疾跑.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/薇恩.jpg",
                "design": "暗夜猎手",
                "name": "骑帅猪的衰哥",
                "head": "images/tx9.jpg",
                "sk1": "images/治疗.jpg",
                "sk2": "images/闪现.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            },
            {
                "pic": "images/泰坦.jpg",
                "design": "诺提勒斯",
                "name": "上帝也卖萌",
                "head": "images/tx10.jpg",
                "sk1": "images/闪现.jpg",
                "sk2": "images/治疗.jpg",
                "ping": "images/绿点.png",
                "value": random.randint(60, 100),
                "load": "{}%".format(random.randint(60, 100))
            }
        ]
    }

    return render(request,"index.html",hero)