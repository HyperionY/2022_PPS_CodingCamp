import sys

str_t = sys.stdin.readline()
str_t = str_t[:-1]
alpabet = [0] * 26

for i in str_t:
  if ord(i) > 96:
    alpabet[ord(i) - 97] += 1
  else:
    alpabet[ord(i) - 65] += 1

compare_list = sorted(alpabet, reverse=True)
if compare_list[0] == compare_list[1]:
  print("?")
else:
  print(chr(alpabet.index(compare_list[0]) + 65))