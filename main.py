def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def process_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            if is_prime(number):
                last_digit = number % 10
                fib_number = fibonacci(last_digit)
                outfile.write(f"{fib_number}\n")


# Запуск обработки
process_numbers('in_nums.txt', 'out_nums.txt')

