#ამ ფოტოს მიხედვიტ გააკეთეთ პროგრამა. (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა რეგისტრირებულ პაროლს, while ციკლის და  if else _ის გამოყენებით) 

registered_password = "ancho121"
authorized = False

while authorized != True:
    user_input = input("enter your password: ")

    if user_input == registered_password:
        print("accses granted")
        authorized = True
    else:
        print("password incorect please try again")


#იმუშავეთ, მაგალითები გააკეთეთ, range(), for, while, if else და თითო თემაზე 10 მაგალითი უნდა იყოს გაკეთებული სხვადასხვანაირად, ნამუშევარი ატვირთეთ github_ზე 

for i in range(30):
    print("GOA IS THE BEST")


for i in range(1, 46):
    print("1 * ", i, "=", 1 + i)


num1 = int(input("shemoitanet ricxvi"))
num2 = 5

while num1 == num2:
    print("yochag shen moige")
    break
else:
    print("waage")


user_input3 = int(input("enter your gpa"))
if user_input3 < 3.0:
    print("shen shegidzlia miigo stipendia: ")
else:
    print("shen ar sheidzlia miigo stipendia: ")
user_input4 = int(input("enter your incomo: "))
if user_input4 < 50000:
    print("shen shegidzlia miigo umaglesi stipendia: ")
else: 
    print("shen ar shegidzlia miigo umaglesi stipendia: ")
