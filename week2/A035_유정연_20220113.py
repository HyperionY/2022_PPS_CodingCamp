import sys

n_time = int(sys.stdin.readline())

for _ in range(n_time):
  list_str = sys.stdin.readline().split()
  n = float(list_str[0])
  
  for i in list_str[1:]:
    if i == '@':
      n = n * 3
    elif i == '%':
      n = n + 5
    elif i == '#':
      n = n - 7

  print("{0:0.2f}".format(n))