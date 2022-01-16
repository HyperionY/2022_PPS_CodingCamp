import sys

cur_num = -1001
stack = []
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

for i in n_list:
  if i > cur_num:
    cur_num = i
    stack.append(i)

print(" ".join(map(str, stack)))