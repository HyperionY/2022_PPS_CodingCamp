import sys

n = int(sys.stdin.readline())

for _ in range(n):
  n_list = list(map(int, sys.stdin.readline().split()))
  n_list.sort(reverse = True)
  print(n_list[2])