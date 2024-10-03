sum_lines = sum(1 for line in open('in_nums.txt', 'r'))
print('Кол-во чисел в файле = ', sum_lines)


data = []
with open("in_nums.txt") as file:
    for line in file:
        data.append(int(line.strip()))


def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True




def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

array = []

for num in data:
    if is_prime(num):
        last_digit = num % 10
        fib_num = fibonacci(last_digit)
        array.append(fib_num)

with open('out_nums.txt', 'w') as outfile:
    for fib_num in array:
        outfile.write(str(fib_num) + '\n')
