def fib(num):
    if num == 0 or num == 1:
        return num
    else: 
        return fib(num - 1) + fib(num - 2)

def isprime(num):
    i = 2
    while i * i <= num and num % i != 0:
        i += 1
    return i * i > num

def checknum(inputfile, outputfile):
    with open(inputfile, 'r') as infile:
        numbers = infile.read()
        numbers = numbers.split()

    with open(outputfile, 'w') as outfile:
        for number in numbers:
            number = int(number)
            if isprime(number):
                lastn = number % 10
                outfile.write(f"{fib(lastn)}\n")

checknum('in_nums.txt', 'out_nums.txt')