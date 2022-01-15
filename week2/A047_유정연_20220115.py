import sys

s = sys.stdin.readline()

while len(s) > 10:
  print(s[:10])
  s = s[10:]

print(s)