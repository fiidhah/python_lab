# Fibonacci Series of N terms
N = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci Series:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
