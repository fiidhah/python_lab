def add_numbers(*nums):
    """Adds all numbers passed to the function."""
    return sum(nums)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum =", add_numbers(*nums))
