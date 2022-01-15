import sys

n = int(sys.stdin.readline())
alpa_list = [0] * 26
answer = ''

for _ in range(n):
  s = sys.stdin.readline()
  alpa_list[ord(s[0]) - 97] += 1

for i in range(len(alpa_list)):
  if alpa_list[i] > 4:
    answer = answer + chr(i + 97)

if not answer:
  print("PREDAJA")
else:
  print(answer)