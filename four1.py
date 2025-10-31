def simple_interest(p, t, senior):
    if senior == "yes":
        r = 12
    else:
        r = 10
    return (p * t * r) / 100

p = float(input("Enter Principal: "))
t = float(input("Enter Time (in years): "))
senior = input("Is the customer a senior citizen (yes/no): ").lower()

si = simple_interest(p, t, senior)
print("Simple Interest =", si)
