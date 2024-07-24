#Write a program that prints numbers from 1 to 10 using a while loop.

i = 1
result = 0
while  i <= 10:
    print(i)
    i = i + 1


#Write a program that prints the even numbers from 1 to 10 using a for loop.

for i in range(12):
    if i % 2 == 0:
        print(i)


#Write a program that asks the user to enter a number and then prints whether the number is positive, negative, or zero using an if-else statement.

num1 = int(input("shemoitanet ricxvi"))
num2 = 5

while num1 <= num2:
    print("ar aris dadebiti")
    break
else:
    print("dadebitia")


#Write a program that asks the user to enter a password. If the password is "abc123", print "Access granted"; otherwise, print "Access denied".

registered_password = "abc123"
authorized = False

while authorized != True:
    user_input = input("enter your password: ")

    if user_input == registered_password:
        print("accses granted")
        authorized = True
    else:
        print("Access denied")

#Write a program that prints numbers from 1 to 10, but stops if the number is 5 using a while loop and the break statement. break

i = 1
result = 0
while  i <= 5:
    print(i)
    i = i + 1

#Write a program that asks the user to enter a number between 1 and 5. If the number is less than 1 or greater than 5, print "Invalid input". If the number is between 1 and 5, print "Valid input"






#Write a program that asks the user to enter a number. If the number is divisible by 3, print "Fizz".






#If the number is divisible by 5, print "Buzz". If the number is divisible by both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.



