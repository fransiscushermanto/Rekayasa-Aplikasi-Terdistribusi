import sys

angka = 0
huruf = 0
lambang = 0

def split(word):
    return [char for char in word]

for line in sys.stdin:
    for c in split(line):
        if c.isdigit():
            angka += 1
        elif c.isalpha():
            huruf += 1
        else:
            lambang += 1

sys.stdout.write("Total Angka: " + str(angka) + "\n")
sys.stdout.write("Total Huruf: " + str(huruf) + "\n")
sys.stdout.write("Total Lambang: " + str(lambang) + "\n")
