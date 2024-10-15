num = int(input("Enter the number: "))
original_num = num
sum = 0

while num > 0:
    rem = num % 10
    sum += rem ** 3
    num = num // 10

if original_num == sum:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")