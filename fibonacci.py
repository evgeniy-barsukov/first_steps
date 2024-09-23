def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)





res_numbers = []

with open('in_nums.txt', 'r') as in_file:
    numbers = [int(row) for row in in_file]

for number in numbers:
        last_digit = number % 10
        res_number = fib(last_digit)
        res_numbers.append(res_number)


with open('out_nums.txt', 'w') as out_file:
    for res_number in res_numbers:
        out_file.write(f"{res_number}\n")