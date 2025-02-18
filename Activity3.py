def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
num1=int(input("Enter a number "))
num2=int(input("Enter another number "))
choice=int(input("Choose 1 to add / 2 to subtract / 3 to multiply / 4 to divide "))
if choice==1:
    print(add(num1,num2))
elif choice==2:
    print(subtract(num1,num2))
elif choice==3:
    print(multiply(num1,num2))
elif choice==4:
    print(division(num1,num2))
else:
    print("Invalid")