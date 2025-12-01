# input = 'year_2025/day 1/example.txt'
input = 'aoc-inputs/year_2025/day 1/input.txt'

def left(d, c):
    # d = input dial
    # c = input clicks
    global answer_2
    for i in range(0,c):
        d += -1
        if d < 0:
            d = 99
        if d == 0:
            answer_2 += 1
    return d

def right(d, c):
    # d = input dial
    # c = input clicks
    global answer_2
    for i in range(0,c):
        d += 1
        if d > 99:
            d = 0
        if d == 0:
            answer_2 += 1
    return d

answer_1 = 0
answer_2 = 0
dial = 50

for line in open(input).readlines():
    line = str(line.strip('\n'))
    direction = str(line[:1])
    clicks = int(line[1:])
    if direction == "L":
        dial = left(dial, clicks)
    elif direction == "R":
        dial = right(dial, clicks)
    # if dial < 0:
    #     dial = 100 + dial
    # if dial > 99:
    #     dial = abs(100 - dial)
    if dial == 0:
        answer_1 += 1
    if dial < 0 or dial > 99:
        print(f'direction = {direction}, clicks = {clicks}, new dial = {dial}')
    # print(f'direction = {direction}, clicks = {clicks}, new dial = {dial}')

print(answer_1)
print(answer_2)