def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("Please select the operation:")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
choice=input("Please enter a/b/c/d: ")
num_1=int(input("Please enter 1st number: "))
num_2=int(input("Please enter 2nd number: "))
if choice=="a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="b":
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=="c":
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=="d":
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("Invalid input")