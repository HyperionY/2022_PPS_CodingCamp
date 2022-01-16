import sys

int_s = list(map(int, (sys.stdin.readline()[:-1])))
int_s.sort(reverse=True)

print("".join(map(str, int_s)))