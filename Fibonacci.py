def check_for_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def fibonacci(num):
    if num in (0, 1):
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


with open('in_nums.txt', 'r') as r_file, open('out_nums.txt', 'w') as wr_file:
    for line in r_file:
        if check_for_prime(int(line)):
            fib_last_digit = fibonacci(int(line) % 10)
            wr_file.write(str(fib_last_digit) + '\n')