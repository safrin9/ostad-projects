print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option=int(input("Enter an option for Basic Calculator Opration: "))

if option==1:
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    n3=n1+n2
    print("Addition is: "+str(n3))

    # print("Addtion is:",n3)
    # print(f"Additon is: {n3}")

elif option==2:
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    n3=n1-n2
    print("Subtraction is: "+str(n3))
    # print(f"Subtraction is {n3}")

elif option==3:
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    n3=n1*n2
    print("Multiplication is: "+str(n3))
    # print(f"Multiplication is {n3}")

elif option==4:
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    n3=n1/n2
    print("Division is: "+str(n3))
    # print(f"Division is {n3:.2f}")

else:
    print("Invalid option")
