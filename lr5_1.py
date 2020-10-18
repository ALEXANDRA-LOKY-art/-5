import math
import random
alphabet = "abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
P = math.pow(10, -7)
V = 100
T = 10/7
passwordsPerWeek = V * 60 * 24 * 7
S = (passwordsPerWeek * T) / P
A = len(alphabet)
L = 0
while math.pow(A, L) <= S:
    L += 1
passw=''
for i in range(L):
    passw=passw+alphabet[random.randint(0, A-1)]
print("Password : \n",passw)
print("Hack for",(A**L*P)/passwordsPerWeek)
