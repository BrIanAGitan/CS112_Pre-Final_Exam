print('CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM')
print('CREATED BY: BRANDON IAN GIMOLATAN')
print()

def is_prime(num: object) -> object:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    start = int(input("Enter the start of the range (or 0 to exit): "))

    if start < 0:
        print("Enter a non-negative number.")
        continue
    elif start == 0:
        print("Program Terminated")
        break

    end = int(input("Enter the end of the range: "))

    if end <= start:
        print(f"Enter a number greater than {start}.")
        continue

    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if not is_prime(num):
            continue
        print(num)
