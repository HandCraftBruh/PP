print("\nЗадание 1.\n")
a=int(input("Введите целое число A: "))
b=int(input("Введите целое число B: "))
if (a>=b):
    print("Число A должно быть меньше или равно числу B!")

for i in range (a,b+1):
    print(i, end="; ")

print("\nЗадание 3.\nЗаново введите значения для A и B.\n")
a=int(input("Введите целое число A: "))
b=int(input("Введите целое число B: "))

if (a<=b):
    print("Число A должно быть больше или равно числу B!")

for i in range (a,b-1,-1):
    if (i%2)!=0:
        print(i, end="; ")

print("\nЗадание 5.\n")
n=int(input("Введите натуральное число n: "))

c=1
sum=0
while c<n:
    for i in range(1,n+1):
        sum+=i**3
        c+=1
print("Сумма:",sum)