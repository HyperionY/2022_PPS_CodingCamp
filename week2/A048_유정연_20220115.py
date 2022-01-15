import sys

n = int(sys.stdin.readline())
total_answer = 0

for _ in range(n):
  s = (sys.stdin.readline())[:-1]
  alpa_list = ''
  answer = True
  cur_char = ''

  for i in s:
    if not i in alpa_list:
      alpa_list = alpa_list + i
      cur_char = i
    elif cur_char != i:
      answer = False
      break
  
  if answer:
    total_answer += 1

print(total_answer)