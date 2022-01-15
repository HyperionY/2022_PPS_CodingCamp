import sys

list_r = [0] * 42

for _ in range(10):
  n = int(sys.stdin.readline())
  rest = n % 42
  list_r[rest] = 1

print(sum(list_r))