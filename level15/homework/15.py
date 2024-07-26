#Write a program that takes asks user for number (use input). If number is even, print that number is even. Else print that number is not even, also print next even number, for example if input is 15, print 16.

num1 = int(input("shemoitanet ricxvi"))
num2 = 15

while num1 <= num2:
     print("ar aris luwi")
     break
else:
    print("luwia")

#Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

registered_password = "GOA BEST"
authorized = False

while authorized != True:
    user_input = input("enter your password: ")

    if user_input == registered_password:
        print("accses granted")
        authorized = True
    else:
        print("Access denied")

#Write an algorithm that takes a string as input and returns True if first character of that string is "G".

list = ["GOA"]
print(list[0])

#Ask user for five names (use input five times). Add all of them in one list and print only first three names.

name1 = input("enter your name: ")
name2 = input("enter your name: ")
name3 = input("enter your name: ")
name4 = input("enter your name: ")
name5 = input("enter your name: ")

print(name1, name2, name3[:3])

#Write an algorithm that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.







#Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).

for i in range(10, -1, -1):
    print(i)

#Implement a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding operation. Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.







#Ask user to enter name and print the last character of that string.







#Using for loop, ask user for number. Then create a list which will have even numbers in next range: from 0 to user's number. At last, print out whole list. 








#Ask user for whole number. Then create a factorial for this number and print it out (If you don't know what a factorial is, google it). 
