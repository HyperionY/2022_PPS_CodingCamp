import sys

vowel = "aeiou"

while True:
  stack = 0
  alpa_list = [0] * 26
  prev_i = ''
  vowel_or_not = True
  answer = True
  
  s = (sys.stdin.readline())[:-1]
  if s == "end":
    break

  for i in s:
    alpa_i = ord(i) - 97
    alpa_list[alpa_i] += 1

    if stack == 0:
      stack += 1
      if i in vowel: vowel_or_not = True
      else: vowel_or_not = False
    else:
      if i in vowel:
        if vowel_or_not: 
          stack += 1
        else: 
          stack = 1
          vowel_or_not = True
      else:
        if not vowel_or_not: 
          stack += 1
        else: 
          stack = 1
          vowel_or_not =False

    if stack > 2:
      answer = False
      break

    if prev_i == i:
      if not i in "oe":
        answer = False
        break
        
    prev_i = i

  num_vowel = alpa_list[0] + alpa_list[4] + alpa_list[8] + alpa_list[14] + alpa_list[20]
  if not num_vowel:
    answer = False

  if answer:
    print("<" + s + "> is acceptable.")
  else:
    print("<" + s + "> is not acceptable.")