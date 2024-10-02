def fib(n):
    a, b = 1, 1
    i = 0
    while True:
        if a % 10 == n:
            return i
        a, b = b, a + b
        i += 1

with open('in_nums.txt', 'r') as file:
    numbers = file.readlines()

with open('out_nums.txt', 'w') as file:
    for number in numbers:
        number = int(number.strip())
        last_digit = number % 10
        fib_index = fib(last_digit)
        file.write(f"{fib_index}\n")