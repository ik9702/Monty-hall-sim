import random
import sys


trial_total = 1000
change_win = 0
hold_win = 0

#시뮬레이션 본문
for q in range(trial_total):
    door = list()
    car_door = list()
    door_reveal = list()
    #자동차가 있는 문의 배열 생성
    for i in range(3):
        x = random.randrange(3)
        car_door.append(x)
    #모든 문의 배열 생성(자동차는1, 염소는 0)
    for i in range(3):
        door.append(0)
        for j in range(1):
            if i == car_door[j]:
                door[i] = 1

    #두사람의 선택
    pick = random.randrange(3)

    #바꾸지 않는 사람의 승패
    if door[pick] == 1:
        hold_win += 1
    else:
        change_win += 1

print(trial_total, hold_win, change_win)
