player_name = 'Alice'
player_life = 20
player_power = 2

monster_name = 'Dragon'
monster_life = 10
monster_power = 4
#file을 사용하면 게임을 저장 할 수 있음.
#순서대로 프로그램이 executing 되는 것 - procedural programming <-> 객체지향


def attack_monster():
    global monster_life #함수 안쪽에서 바깥쪽을 바꿀 수 없기 때문에 global을 써야 함.
    print('player attacks monster')
    monster_life = monster_life - player_power

def attack_player():
    global player_life
    print('monster attacks player')
    player_life = player_life - monster_power #### 게임 플레이에 필요한 정보들

import random #### 실제 게임 플레이.
while True: # 무한 while loop
    if random.random() < 0.5: #랜덤하게 플레이어나 몬스터가 공격을 시작
        attack_monster() #modulation
    else:
        attack_player()
    if player_life <= 0:
        print('player dead')
        break
    elif monster_life <= 0:
        print('monster dead')
        break
