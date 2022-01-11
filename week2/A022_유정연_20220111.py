import sys

n = int(sys.stdin.readline())
call_list = list(map(int, sys.stdin.readline().split()))
Y_time, Y_cost, Y_total = 30, 10, 0
M_time, M_cost, M_total = 60, 15, 0

for i in range(n):
  Y_total += (call_list[i] // Y_time) * Y_cost + Y_cost

  M_total += (call_list[i] // M_time) * M_cost + M_cost

if Y_total < M_total: print("Y {:}".format(Y_total))
elif Y_total > M_total: print("M {:}".format(M_total))
else: print("Y M {:}".format(M_total))