text = input("Enter a string: ")
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)
