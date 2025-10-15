a = list(map(int, input("Enter numbers: ").split()))
b = [x for x in a if x % 2 != 0]
print("List after removing even numbers:", b)
