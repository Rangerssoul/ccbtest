# coding:UTF-8
# DATE: 2018/12/24
# TIME: 12:46
# IDE : PyCharm
# NAME: func.py
# AUTHOR: Puhaiming
# COPYRIGHT: Rangerssoul


def gamename(*game):
    print("\n常见游戏：")
    for i, j in enumerate(game):
        print("第"+str(i+1)+"个游戏是："+j)

def mail_list(**mail):
    print("\n手机通信录：")
    for name,phone in mail.items():
        print(name+"的手机号是："+phone)


glist = ["warframe", "gat5", "ghost"]
mlist = {'张三': '13800001111', '李四': '13800001112', 'jack': '13678901234', 'mary': '13500017654'}

#gamename("warframe")
#gamename("warframe", "gat5", "ghost")
gamename(*glist)
mail_list(**mlist)