import sys

time_list = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
total_time = 0
s = (sys.stdin.readline())[:-1]

for i in s:
  total_time += time_list[ord(i) - 65]

print(total_time)