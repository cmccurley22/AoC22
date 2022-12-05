with open("input1.txt") as f:
    input = f.read().split("\n\n")


ans = [0, 0, 0]

for elf in input:
    elf_text = elf.split("\n")
    # print(elf)
    # print("\n")
    sum = 0
    for line in elf_text:
        # print(line)
        if line != "":
            cals = int(line)
        sum += cals
        if sum > min(ans):
            ans.remove(min(ans))
            ans.append(sum)

print(ans[0] + ans[1] + ans[2])