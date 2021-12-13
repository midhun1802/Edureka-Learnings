print("Welcome")
Trails = 3
Userpin = 1802


while Trails != 0:
    Pin = int(input("Please enter your pin number: "))
    if Pin != Userpin:
        Trails -= 1
        print("Wrong pin please try again, you have", Trails, "Trails Left")
    else:
        UserChoice = input("D: Deposit "
                           "or W: WithDraw"
                           "or S: Statment")
        if UserChoice == "D":
            UserDeposit = input("Enter ammount you would like to deposit: ")
            print(UserDeposit, "$ have been deposited")
        if UserChoice == "W":
            UserWithDraw = input("Enter ammount that you would like withdraw: ")
            print(UserWithDraw, "$ have been withdrawn from your account")
        #if UserChoice == "S":
            #UserStatment = input("Please Press Y to Print your statment ")
            #if UserStatment == "*":
             #print(UserStatment, "$ your balance")
    UserExit = input("Would you like to continue Y/N:")
    if UserExit == "N":
        print("Thank you please visit again")
        break
    else:
        continue