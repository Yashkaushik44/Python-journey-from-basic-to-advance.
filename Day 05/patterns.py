while(1):

    #menu
    print("\nPattern Printer\n")

    print("1. Stars")
    print("2. Numbers")
    print("0. Exit\n")

    choice = int(input("Enter your choice : "))

    print("")

    #exit
    if choice == 0:

        print("Thank you!")
        break

    #invalid
    elif choice != 1 and choice != 2:

        print("Select a valid option")
        continue

    else:

        rows = int(input("How many rows : "))

        print("")

        #print pattern
        if choice == 1:

            for i in range(1, rows + 1):

                for j in range(1, i + 1):

                    print("*", end=" ")

                print()

        else:

            for i in range(1, rows + 1):

                for j in range(1, i + 1):

                    print(j, end=" ")

                print()
