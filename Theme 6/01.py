a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Если делится на 3 и на 5
    elif i % 3 == 0:
        print("Fizz")  # Если делится только на 3
    elif i % 5 == 0:
        print("Buzz")  # Если делится только на 5
    else:
        print(i)  # Если не делится ни на 3, ни на 5