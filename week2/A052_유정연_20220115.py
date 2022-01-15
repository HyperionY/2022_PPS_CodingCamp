import sys

n = int(sys.stdin.readline())

for _ in range(n):
  stack = []
  answer = 0
  s = (sys.stdin.readline())[:-1]

  for i in s:
    if i == "O":
      stack.append(len(stack)+1)
    elif i == "X":
      if stack:
        answer += sum(stack)
        stack = []
        
  answer += sum(stack)
  print(answer)