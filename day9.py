import math

with open("input9.txt") as f:
    input = f.read().split("\n")

t = [0, 0]
ropes = [[0, 0] for _ in range(10)]
tails = []
tails2 = []

def move_tail(head, tail):
    if math.dist(head, tail) > math.sqrt(2):   
        if head[0] == tail[0]:
            tail[1] += (head[1] - tail[1]) / 2
        elif head[1] == tail[1]:
            tail[0] += (head[0] - tail[0]) / 2
        else:
            tail[0] += (head[0] - tail[0]) / abs(head[0] - tail[0])
            tail[1] += (head[1] - tail[1]) / abs(head[1] - tail[1])
    
    return tail

def move_ropes(ropes):
    for r in range(1, len(ropes)):
        ropes[r] = move_tail(ropes[r - 1], ropes[r])
    
    return ropes[-1]

for line in input:
    d = line[0]
    n = int(line.split(" ")[1])

    for _ in range(n):
        if d == "R":
            ropes[0][0] += 1
        elif d == "L":
            ropes[0][0] -= 1
        elif d == "U":
            ropes[0][1] += 1
        elif d == "D":
            ropes[0][1] -= 1

        tails.append("".join(str(i) for i in move_tail(ropes[0], t)))
        tails2.append("".join(str(i) for i in move_ropes(ropes)))

print(len(set(tails)))
print(len(set(tails2)))