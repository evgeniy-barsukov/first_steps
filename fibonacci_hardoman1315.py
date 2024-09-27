def fibonacci(num: int) -> int:
    if num == 2:
        isPrime = True
    elif num <= 1 or num % 2 == 0:
        isPrime = False
    else:
        isPrime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                isPrime = False
                break
            isPrime = True
    if isPrime:
        lastDigit = num % 10
        previous, current = 0, 1
        for _ in range(lastDigit):                    
            previous, current = current, previous + current
        return previous

with open('in_nums.txt': str, 'r') as input_file:
    with open('out_nums.txt': str, 'w') as output_file:
        for line in input_file:
            currentLine = int(line.strip())
            fibonacciNum = fibonacci(currentLine)
            if fibonacciNum is not None:
                output_file.write(str(fibonacciNum) + '\n')
