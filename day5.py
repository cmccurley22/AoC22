with open("flo5.txt") as f:
    input = f.read().split("\n")

crates_txt = input[0:8]
instr = input[10:]

n = 4

crates = []

for line in crates_txt:
    crates.append([line[i:i+n] for i in range(0, len(line), n)])

# print(crates)


crates2 = [[], [], [], [], [], [], [], [], []]
# crates2 = [[], [], []]

for row in crates:
    for i in range(len(row)):
        if row[i] != "    " and row[i] != "   ":
            crates2[i].append(row[i])

print(crates2)

for line in instr:
    num = int(line.split(" ")[1])
    start = int(line.split(" ")[3]) - 1
    end = int(line.split(" ")[5]) - 1

    # part 2
    moving = crates2[start][0:num]

    crates2[end] = moving + crates2[end]
    crates2[start] = crates2[start][num:]

    # print(crates2)
    
    '''for _ in range(num):
        crates2[end].insert(0, crates2[start][0])
        crates2[start].pop(0)'''

ans = ""

for c in crates2:
    # print(c)
    ans += c[0][1]

print(ans)