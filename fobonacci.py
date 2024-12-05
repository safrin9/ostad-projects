
def fibo_1(n):
    fibonacci_series=[]
    a=0
    b=1
    c=b
    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, c
        c=a+b
    return fibonacci_series

def fibo_max(max_value):
    fibonacci_series=[]
    a=0
    b=1
    c=b
    while a<=max_value:
        fibonacci_series.append(a)
        a, b = b, c
        c=a+b
    return fibonacci_series

while True:
    print("Choose an option: ")
    print("1. Generate Fibonacci series by number of terms ")
    print("2. Generate Fibonacci series by maximum value ")
    print("3. Exit ")
    print()
    menu=int(input("Enter your choice: "))
   
    if menu==1:
        try:
            n=int(input("Enter the number of terms: "))
            if n<=0:
                print("Please enter a positive integer.")
            else:      
                series=fibo_1(n)
                print(f"Fibonacci series ({n} terms): {', '.join(map(str,series))}\n")
        except ValueError:
            print("Invalid input! Please enter an integer.")
       
    elif menu==2:
        try:
            n=int(input("Enter the maximum value: "))
            if n<0:
                print("Please enter a non-negative integer.")
            else:        
                series=fibo_max(n)
                print(f"Fibonacci series (up to {n}): {', '.join(map(str,series))}\n")
        except ValueError:
            print("Invalid input! Please enter an integer.")
    elif menu==3:
        print("Goodluck!")
        break