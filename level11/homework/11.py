# Write a program that takes an input from the user and checks if it's a positive, negative, or zero number using if-else.

num = float(input("enter number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negativr")
else:
    print(num, "is zero")

#Write a program that prints all the even numbers between 1 and 20 using a for loop and if statement.

for i in range(1,20 + 1):
    if i % 2 == 0:
        print(i)

#Write a program that calculates the sum of a number entered by the user using a while loop. 

num = int(input("enter: "))
result = 0 

while num >= 0:
    result = result + num 
    num = num - 1


print(result)


#Write a program that simulates a basic ATM. It should ask the user for their PIN, and if it's correct, display a text withdrawal, deposit, and balance. 

registred_pincode = 2010
authorized = False

while authorized != True:
    user_input = int(input("enter pincode: "))

    if user_input == registred_pincode:
        print("accses granted")
        authorized = True

    else:
        print("try again")

#Write a program that simulates a simple login system. Ask the user for a username and password, and if they enter "admin" and "password123", respectively, print "Login successful" using if-else

registred_password = ""
registred_username = ""

while True:
    print("1. signup")
    print("2. login")
    print("3. exit")

    user_choice = int(input("enter your choice: "))

    if user_choice == 1:
         print("signup page")
         registred_password = input("enter password: ")
         registred_username = input("enter username: ")
         print("you have succsesfully")

    elif user_choice == 2:
        print("signin page")
        username_input = input("enter your username: ")
        password_input = input("enter your password: ")

        if username_input == registred_username and password_input == registred_password:
            print("you succsesfully entered you account")
            break
        else:
            print("try again")

    elif user_choice == 3:
        print("thanks for using our program")
        break
    else: 
        print("invalid choice")

