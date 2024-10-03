from math import factorial
from operator import truediv
def read_from_file(filename = 'in_nums.txt'):
    num_list = []
    with open(filename, 'r') as file:
        for line in file:
            num_list.append(line.strip())
        return num_list

def write_to_file(text_data_list: list, file_name : str = 'out_nums.txt') -> None:
    with open(file_name, 'w') as file:
        for text_data in text_data_list:
            file.write(str(text_data) + '\n')
        file.close()


def  is_prime(number: int) -> bool:
    if number == 1:
        return False
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
        return True

def get_fibonacci_number(number: int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return get_fibonacci_number(number - 1) + get_fibonacci_number(number - 2)

out_list = []
nums = read_from_file()
for number in nums:
    if is_prime(int(number)):
        out_list.append(get_fibonacci_number(int(number) % 10))
write_to_file(out_list)