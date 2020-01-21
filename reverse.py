num = int(input("enter a number"))
reverse = 0
while(num>0):
    reminder = num%10
    reverse = (reverse*10)+reminder
    num = int(num/10)
print(reverse)
