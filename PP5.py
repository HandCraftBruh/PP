str=input("Введите текст:\n")

print("Изменённый текст:\n",str.replace(".",""),sep="")
dot=len(str)-len(str.replace(".",""))
print("Кол-во удаленных точек:",dot)