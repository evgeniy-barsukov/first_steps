def fibonacci_seq(n: int) -> int: 
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)


def is_prime(n: int, i=2) -> bool:
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True

    return is_prime(n, i + 1)


with open("in_nums.txt", "r") as in_file:
    nums = in_file.read().split()

with open("out_nums.txt", "w") as out_file:
    for num in nums:
        last_digit = int(num[-1])
        num = int(num)

        if is_prime(num):
            out_file.write(f'{fibonacci_seq(last_digit)}\n')