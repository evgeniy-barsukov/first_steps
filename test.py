# число фибоначчи
def fib_func(num:int)->int:
    if num <= 1:
        return num
    else:
        return fib_func(num - 1) + fib_func(num - 2)


# функция проверяет является ли число простым
def is_simple_num(num:int)->bool:
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


with open('in_nums.txt', 'r') as file:
    with open('out_nums.txt', 'w') as outp:
        for line in file:
            if is_simple_num(int(line)):
                last_num = int(line.rstrip()[-1])
                outp.write(str(fib_func(last_num)) + '\n')
