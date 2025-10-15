words = input("Enter words: ").split()
print("Length of longest word:", len(max(words, key=len)))
