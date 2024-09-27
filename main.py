def get_fibonacci(n: int) -> int:
    if (n == 1) or (n == 0):
        return n
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def is_prime(n: int, i=2) -> bool:
    if n <= 2:
        return True if n == 2 else False
    if (n % i) == 0:
        return False
    if (i * i) > n:
        return True

    return is_prime(n, i + 1)


with open("in_nums.txt", "r") as in_file:
    numbers = in_file.read().split()
    in_file.close()

with open("out_nums.txt", "w") as out_file:
    for number in numbers:
        last_digit = int(number[-1])
        number = int(number)

        if is_prime(number):
            out_file.write(f'{get_fibonacci(last_digit)}\n')
    out_file.close()
