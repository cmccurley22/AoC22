with open("input4.txt") as f:
    input = f.read().split("\n")

ans = 0

for l in input:
    a = l.split(",")[0]
    b = l.split(",")[1]

    a_i = [i for i in range(int(a.split("-")[0]), int(a.split("-")[1]) + 1)]
    b_i = [j for j in range(int(b.split("-")[0]), int(b.split("-")[1]) + 1)]

    overlap = False

    for i in a_i:
        if i in b_i:
            overlap = True
    
    if overlap:
        ans += 1

print(ans)