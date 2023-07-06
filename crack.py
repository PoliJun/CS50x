from string import digits, ascii_letters
from itertools import product

n=1
for i in range(8):
    n*=62
print(n)
exit(1)

for passcode in product(ascii_letters, repeat=4):
    print(*passcode)
