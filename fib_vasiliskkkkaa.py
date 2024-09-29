def simple(num):  # Проверка на простое число
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fib(num):  # Вычисление числа Фибоначчи
    if num == 0 or num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


with open('in_nums.txt', 'r') as infile:
    numbers = [int(line.strip()) for line in infile]

fib_numbers = []

for num in numbers:
    if simple(num):
        last_digit = num % 10
        fib_num = fib(last_digit)
        fib_numbers.append(fib_num)

with open('out_nums.txt', 'w') as outfile:
    for fib in fib_numbers:
        outfile.write(f"{fib}\n")