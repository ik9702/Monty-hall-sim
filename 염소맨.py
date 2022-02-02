import random
import copy
import sys


sys.stdout = open('결과.txt', 'w')
sys.setrecursionlimit(1000000)


def fact(x):
    if x > 1:
        return x*fact(x-1)
    else:
        x=1
        return x

door_num = 3
car_num = 1
open_num = 1
set_total = 1000
set_now = 0
trial_total = 1000
total_avg = 0

hold_winrate = 0.333217
change_winrate = 0.666783

'''
몬티홀 게임 확률
hold_winrate = 0.333217
change_winrate = 0.666783

(10,2,4게임 확률)
hold_winrate = 0.19977
change_winrate = 0.360569
'''

for p in range(1,set_total+1):

    trial_now = 0
    change_win = 0
    hold_win = 0

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
        door_reveal = copy.deepcopy(door)

        del door_reveal[pick]
        n = 1
        for i in range(open_num):
            x = random.randrange(door_num-n)
            while door_reveal[x] == 1:
                x = random.randrange(door_num-n)
            del door_reveal[x]
            n += 1

        x = random.randrange(len(door_reveal))
        if door_reveal[x] == 1:
            change_win += 1

        trial_now += 1

#확률만 알고싶을 때, 시행횟수만 정하고 set수는 1로, 그 외에는 비활성#
    #print(trial_total, hold_win, hold_win/trial_total, change_win, change_win/trial_total)

#PN구하는 코드, 확률만 구할때 비활성화
    hold_P1000 = fact(trial_total)/(fact(trial_total-hold_win)*fact(hold_win))*((hold_winrate)**hold_win)*((1-hold_winrate)**(trial_total-hold_win))
    change_P1000 = fact(trial_total)/(fact(trial_total-change_win)*fact(change_win))*((change_winrate)**change_win)*((1-change_winrate)**(trial_total-change_win))
    print(p, hold_win, hold_P1000, change_win, change_P1000)

sys.stdout.close()
