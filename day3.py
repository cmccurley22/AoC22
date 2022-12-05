with open("alexinput3.txt") as f:
    input = f.read().split("\n")

    # for i in input:
    #     i = int(i)

ans = 0

for l in input:
    first, second = l[:len(l)//2], l[len(l)//2:]
    common = ""
    for c in first:
        if c in second:
            common = c
    
    if common.isupper():
        ans += ord(common) - 38
    else:
        ans += ord(common) - 96

print(ans)

ans = 0

i = 0

while i < len(input) - 2:
    a = input[i]
    b = input[i+1]
    c = input[i+2]

    for char in a:
        if char in b and char in c:
            common = char

    if common.isupper():
        ans += ord(common) - 38
    else:
        ans += ord(common) - 96
    
    i += 3
        

print(ans)