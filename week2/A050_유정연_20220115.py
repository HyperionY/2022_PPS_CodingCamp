import sys

s = (sys.stdin.readline())[:-1]
answer = ''

for i in s:
  target = ord(i)
  target -= 3

  if target < 65:
    target += 26
  answer += chr(target)

print(answer)