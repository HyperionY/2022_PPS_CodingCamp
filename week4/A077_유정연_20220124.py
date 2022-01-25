import sys

num_list = [0 for i in range(8)]
stack = []
total = 0

for i in range(8):
  num_list[i] = int(sys.stdin.readline())

new_list = sorted(num_list)
total = sum(new_list[3:])

for i in range(len(num_list)):
  if num_list[i] in new_list[3:]:
    stack.append(i+1)
total_list = " ".join(map(str, stack))

print(total)
print(total_list)
