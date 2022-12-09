with open("input6.txt") as f:
    input = f.read()

def find_marker(buffer, l = 4):
    for i in range(len(buffer)):
        if len(set(buffer[i - l : i])) == l:
            return i

print(find_marker(input))
print(find_marker(input, 14))