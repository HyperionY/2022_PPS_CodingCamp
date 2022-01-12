import sys

n = int(sys.stdin.readline())
position = int(sys.stdin.readline())


if n > 5:
  print("Love is open door")
else:
  if position == 1: position -= 1
  else: position += 1

  for i in range(n - 1):
    print(position)
    if position == 1: position -= 1
    else: position += 1
