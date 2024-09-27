
# число фибоначчи
def fibFunc(num):
    if num<=1:
        return num
    else:
        return  fibFunc(num-1)+fibFunc(num-2)

# функция проверяет является ли число простым
def isSimpleNum(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


with open('in_nums.txt','r') as file:
    with open('out_nums.txt','w') as outp:
        for line in file:
            # проверка числа
            if isSimpleNum(int(line)):
                # последняя цифра
                last_num=int(line.rstrip()[-1])
                # находим число фибоначчи,преобразуем его в строку и пишем в файл
                outp.write(str(fibFunc(last_num)) + '\n')


