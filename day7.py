with open("input7.txt") as f:
    input = f.read().split("\n")

dir = []
struct = {}

l = 0
while l < len(input):
    line = input[l]
    if line[0] == "$":
        if line.split(" ")[1] == "cd":
            if line.split(" ")[2] == "..": dir.pop()
            elif line.split(" ")[2] == "/": dir.append("~")
            else: dir.append(line.split(" ")[2])
        l += 1
    else:
        struct["/".join(dir)] = [line]
        l += 1
        while l < len(input) and input[l][0] != "$":
            struct["/".join(dir)].append(input[l])
            if l < len(input): l += 1

def size(dir):
    if all([file[0].isdigit() for file in struct[dir]]):
        return sum(int(file.split(" ")[0]) for file in struct[dir])

    else:
        total_size = 0
        for file in struct[dir]:
            if file[0:3] == "dir":
                file_path = dir + "/" + file.split(" ")[1]
                total_size += size(file_path)
            else:
                total_size += int(file.split(" ")[0])
        
        return total_size

small_size = 0
outer_size = size("~")
unused_space = 70000000 - outer_size
needed_space = 30000000 - unused_space

free = []

for file in struct:
    f_size = size(file)
    if f_size <= 100000:
        small_size += f_size
    if f_size > needed_space:
        free.append(f_size)

print(small_size)
print(min(free))