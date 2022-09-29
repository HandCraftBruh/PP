import math
x=int(input("Введите значение для x: "))
y=int(input("Введите значение для y: "))
z=((9*math.pi*y+10*math.cos(x))/(math.sqrt(y)-math.fabs(math.sin(y))))*math.pow(math.e,x)
print("z={0:.2f}".format(z))