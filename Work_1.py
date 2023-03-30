

def main():
    num1 = int(input("Base_num:"))
    num2 = int(input("Target_num:"))
    x = first_pow(num1, num2)
    y = log(x, num1)
    print((y-1, y))

def first_pow(num1, num2):    
    target = 1

    for i in range(num2):
        target *= num1
        if target >= num2:
            return target

def log(x, num1):      
    count = 0

    while x >= 1:
        x = x / num1
        count += 1
        if x == 1:
            return count

main()    
