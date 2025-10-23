# Four-digit numbers with all even digits and perfect square
import math

print("Four-digit numbers with all even digits and perfect square:")
for num in range(1000, 10000):
    if all(int(d) % 2 == 0 for d in str(num)):
        if int(math.sqrt(num)) ** 2 == num:
            print(num)
