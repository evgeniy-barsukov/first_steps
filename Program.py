def fibonacci(num):
    if (num == 0 or num == 1):
        return(num);
    else:
        return(fibonacci(num - 1) + fibonacci(num - 2));

with open('in_nums.txt', 'r') as input_file, open('out_nums.txt', 'w') as output_file:
    for line in input_file:
        currentLine = int(line);
        currentLine = currentLine % 100 % 10;
        output_file.write(str(fibonacci(currentLine)) + '\n');