num = int(input("Enter the number: "))
original_num = num 
reversed_num = 0

while num > 0:
    rem = num % 10
    reversed_num = reversed_num * 10 + rem
    num = num // 10

print("Reversed number is : ",reversed_num)