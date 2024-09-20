def fibonacciSeq(n):
    if (n == 1) or (n == 0):
        return n
    else:
        return fibonacciSeq(n - 1) + fibonacciSeq(n - 2)

def isPrime(n, i = 2):
    if n <= 2:
        return True if n == 2 else False
    if (n % i) == 0:
        return False
    if (i * i) > n:
        return True
    
    return isPrime(n, i + 1)

# 

with open("in_nums.txt", "r") as inFile:
    nums = inFile.read().split()
    inFile.close()

with open("out_nums.txt", "w") as outFile:
    for num in nums:
        lastDigit = int(num[-1])
        num = int(num)

        if isPrime(num):
            outFile.write(f'{fibonacciSeq(lastDigit)}\n')
    outFile.close()

    