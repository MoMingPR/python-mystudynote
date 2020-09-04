import time \\声明包

player_life = 130
player_attack =15

enemy_life =150
enemy_attack=10 \\玩家和敌人的数值

while player_life > 0 and enemy_life > 0:
         player_life = player_life - enemy_attack
         enemy_life = enemy_life - player_attack
         print('敌人发动攻击，玩家的血量：'+str(player_life))
         print('玩家发动攻击，敌人的血量：'+str(enemy_life)) \\循环
         time.sleep(1.5) \\调用函数
if player_life > 0 and enemy_life <= 0:  \\输出条件
    print('玩家获胜')
else:
    print('敌人获胜')
