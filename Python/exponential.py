base = int(input("Enter base : "))
power = int(input("Enter power : "))
num = 1
res = 1
while(num<=power):
    res = res*base
    num += 1
print(res)

