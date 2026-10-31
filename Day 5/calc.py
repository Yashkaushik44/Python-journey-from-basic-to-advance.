while(1):
    
    #menu
    print("\nWelcome to the calculator!\n")

    print("Select from the below options! \n")

    print("0.break")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide\n")

    choice = int(input("Enter your choice : "))
    
    print("")

    #break
    if choice == 0:
        
        print("Thank you for using the calculator!")

        break
    
    #input error handling
    elif choice < 0 or choice > 4:

        print("Select a valid option")

    else:

        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        
        print("")

        if choice == 1:
        
                print(f"The addition is : {num1 + num2}")
        
        elif choice == 2:

            print(f"The subtraction is : {num1 - num2}")

        elif choice == 3:
            
            print(f"The multiplication is : {num1 * num2}")

        else:

            print(f"The quotent is : {num1 / num2}")

