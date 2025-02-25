pin = int(input("Enter Pin: "))
if pin == 1111 or pin == 2222:
    print('Correct Pin!')
    option = input("enter an option\n1. add 2 numbers\n2. mul 2 numbers\n3. subtract 2 numbers\nEnter option here: ")
    if option == "1":
        print("you've chosen option 1")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        res= num1 + num2
        print(res)
    elif option == "2":
        print("you've chosen option 2")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        res= num1 * num2
        print(res)
    elif option == "3":
        print("you've chosen option 3!")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        res= num1 - num2
        print(res)
    else:
        print("The option you've chosen isnt part of the listed options")

else: 
    print("Incorrect!")