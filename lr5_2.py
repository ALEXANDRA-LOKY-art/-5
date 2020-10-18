import stdiomask

alphabet = "abcdefghijklmnopqrstuvwxyz"
fst = input("Введите первое слово: ")
snd = input("Введите второе слово: ")
trd = input("Введите третье слово: ")
passw=""
passw+=alphabet[(alphabet.index(fst[0]) + 1 % (len(alphabet) - 1))]
passw+=alphabet[(alphabet.index(fst[0]) + 2 % (len(alphabet) - 1))]
passw+=alphabet[(alphabet.index(snd[-1]) + 1 % (len(alphabet) - 1))]
if len(trd)% 2 != 0:
    passw+=alphabet[(alphabet.index(trd[-2]) + 1 % (len(alphabet) - 1))]
else:
    passw+=alphabet[(alphabet.index(trd[len(trd)//2]) - 1 % (len(alphabet) - 1))]
passw+=alphabet[(len(fst)+len(snd)++ 4 % 26)]
print(passw)
userPassw=stdiomask.getpass()
if userPassw==passw:
    print("Success")
else:
    print("Print bad password")
