# Функция обработки числа фибаначчи
def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

# Чтение чисел из файла in_nums.txt
with open('in_nums.txt', 'r') as infile:
    numbers = [int(line) for line in infile]

# Массив для хранения результатов
fibonacci_numbers = []

# Обработка каждого числа
for number in numbers:
        last_digit = number % 10
        fib_number = fib(last_digit)
        fibonacci_numbers.append(fib_number)

# Запись результатов в файл out_nums.txt
with open('out_nums.txt', 'w') as outfile:
    for fib_number in fibonacci_numbers:
        outfile.write(f"{fib_number}\n")