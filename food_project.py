favourite_foods=[]

while True:
    print("Favourite Food Manager")
    print("0. Exit")
    print("1. Add Food")
    print("2. Remove Food")
    print("3. View favourite all foods")
    
    choice=input("Choose an option: ")
    if choice=="0":
        print("Thanks for using Favourite Food Manager")
        break

    elif choice=="1":
        food= input("Enter your favourite food name: ")
        favourite_foods.append(food)
        print(f"{food} added successfully\n")

    elif choice=="2":     
        food= input("Enter a food name which you want to remove: ")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} removed successfully\n")
        else:
            print(f"{food} doesn't exists in list\n")
    
    elif choice=="3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index,food in enumerate(favourite_foods,start=1):
                print(f"{index}.{food}")
            print()
        else:
            print("You have no favourite food")
    else:
        print("Invalid option")