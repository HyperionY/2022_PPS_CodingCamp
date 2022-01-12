import sys

winner = 0
win_score = 0

for i in range(5):
  score = list(map(int, sys.stdin.readline().split()))
  if win_score < sum(score):
    winner = i + 1
    win_score = sum(score)

print("{:} {:}".format(winner, win_score))