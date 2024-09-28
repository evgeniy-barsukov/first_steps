def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

with open('in_nums.txt', 'r') as f:
    primes = [int(line.strip()) for line in f if is_prime(int(line))]

with open('../../Desktop/out_nums.txt', 'w') as f:
    for prime in primes:
        last_digit = prime % 10
        result = fib(last_digit)
        f.write(str(result) + '\n')
