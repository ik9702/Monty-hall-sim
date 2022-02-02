import random
import copy
import sys

#sys.stdout = open('결과.txt', 'w')

door_num = 6
car_num = 2
open_num = 1
trial_total = 10000

trial_now = 0
change_win = 0
sp_happen = 0
sp_change_win = 0
hold_win = 0
fool = 0
change_pick = 0
#시뮬레이션 본문
for q in range(trial_total):
    door = list()
    car_door = list()
    door_reveal = list()

    #자동차가 있는 문의 배열 생성
    for i in range(car_num):
        x = random.randrange(door_num)
        while x in car_door:
            x = random.randrange(door_num)
        car_door.append(x)
    #모든 문의 배열 생성(자동차는1, 염소는 0)
    for i in range(door_num):
        door.append(0)
        for j in range(car_num):
            if i == car_door[j]:
                door[i] = 1
        pick = random.randrange(door_num)

    #바꾸지 않는 사람의 승패
    if door[pick] == 1:
        hold_win += 1

    #바꾼 사람의 승패
    A=0
    door_reveal = copy.deepcopy(door)
    del door_reveal[pick]

    for i in range(open_num):
        x = random.randrange(door_num-(i+1))
        if door_reveal[x] == 1:
            A = 1
        del door_reveal[x]
    if A == 1:
        sp_happen += 1
    change_pick = int(random.randrange(len(door_reveal)))
    if door_reveal[change_pick] == 1:
        change_win += 1
        if A == 1:
            sp_change_win += 1


    trial_now += 1

    if 1 in door_reveal:
        continue
    elif door[pick] == 1:
        continue
    else:
        fool += 1



print(trial_total, hold_win, change_win, fool, sp_happen ,sp_change_win)

#sys.stdout.close()
