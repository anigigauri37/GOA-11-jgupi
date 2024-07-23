#calculate the sum of all even numbers from 1 to 10 using a while loop

i = 1
result = 0
while  i <= 10:
    print(i)
    i = i + 1

#while ციკლის მეშვეობით შეამოწმეთ რიცხვები 1 დან 20 ჩათვლით, რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტეთ ეგ რიცხვი

i = 1 

while i <= 20:
    if i % 5 == 0 and i % 2 == 0:
        print(i)
    i = i + 1

#for ციკლის მეშვეობით დაბეჭდეთ ყველა რიცხვი 1-100 ჩათვლით რომელიჩ იყოპა 5

for i in range(1, 100, 1):
    if i % 5 == 0:
        print(i)

#for ციკლის მეშვეობით დაბეჭდეთ ყველა ის რიცხვი რომელიც იყოფა 6-ზე 1 დან 20 ჩათვლით

for i in range(6, 20 + 1, 6):
    print(i)








