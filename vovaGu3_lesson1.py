def compute_fibonacci (num:int):
    if num == 0 or num == 1:
        return num
    else:
        return compute_fibonacci(num -1) + compute_fibonacci(num - 2)

arr=[]

def prime_number (num:int):
    pr = True
    for b in range(2,num):
         if num % b == 0 :
                pr = False
    if pr and num != 1:
        arr.append(num % 10)

with open("in_nums.txt","r",) as file:
    for row in file:
        prime_number(int(row.strip()))
    file.close()

print(arr)

with open("out_nums.txt","w",) as file:
    for row in arr:
        file.write(str(compute_fibonacci(row))+"\n")
    file.close()