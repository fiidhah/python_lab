def compare(s1, s2, n):
    return s1[:n] == s2[:n]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter number of characters to compare: "))

if compare(s1, s2, n):
    print("The first", n, "characters are same.")
else:
    print("The first", n, "characters are different.")
