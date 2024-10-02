# Проверяем, является ли число простым.


def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Вычисляем n-ое число Фибоначчи.


def fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Главная функция программы: открытие файла, вывод данных.
def main():
    with open("in_nums.txt", "r") as file_in:
        nums = [int(line.strip()) for line in file_in]

    fib_nums = []
    for num in nums:
        if is_prime(num):
            last_digit = num % 10
            fib_num = fibonacci(last_digit)
            fib_nums.append(fib_num)

    with open("out_nums.txt", "w") as file_out:
        for fib_num in fib_nums:
            file_out.write(str(fib_num) + "\n")


if __name__ == "__main__":
    main()
