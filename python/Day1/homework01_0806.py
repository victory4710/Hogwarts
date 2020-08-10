"""
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


def game():  # 定义game方法
    my_hp = 1000  # 我的生命值1000
    my_power = 200  # 我的攻击力 200
    your_hp = 1000  # 敌人的生命值1000
    your_power = 195  # 敌人的攻击力 195
    while True:  # 开始战斗循环
        my_hp = my_hp - your_power  # 计算我方本回合攻击后剩余血量
        print(f"我还剩{my_hp}的血量。")  # 打印剩余血量

        your_hp = your_hp - my_power  # 计算敌方本回合攻击后剩余血量
        print(f"敌人还剩{your_hp}的血量。")  # 打印剩余血量

        if my_hp <= 0:  # 我的血量小于0，中断循环，打印我输了。
            print("我输了。")
            break
        elif your_hp <= 0:  # 敌人的血量小于0，中断循环，打印我赢了
            print("我赢了！")
            break


game()  # 调用函数
