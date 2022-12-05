with open("input2.txt") as f:
    input = f.read().split("\n")
    
    # for i in input:
     #   i = int(i)

ans = 0

for l in input:
    o = l.split(" ")[0]
    y = l.split(" ")[1]

    if y == "X":
        ans += 0
        if o == "A":
            ans += 3
        elif o == "B":
            ans += 1
        else:
            ans += 2
    elif y == "Y":
        ans += 3
        if o == "A":
            ans += 1
        elif o == "B":
            ans += 2
        elif o == "C":
            ans += 3
    elif y == "Z":
        ans += 6
        if o == "A":
            ans += 2
        elif o == "B":
            ans += 3
        else:
            ans += 1
    
    print(ans)

    
    '''if ord(o) + 23 == ord(y):
        ans += 3
    elif (y == "X" and o == "C") or (y == "Y" and o == "A") or (y == "Z" and o == "B"):
        ans += 6'''
    

print(ans)