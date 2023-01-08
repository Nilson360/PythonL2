x = str(3) #forcer le type de la variable
y = int(3)
z = float(3)
print(type(x)) #voir le type de la variable
print(type(y))
print(type(z))

print("-------------------Many values to multiple variables------------------------------")
#Many values to multiple variables

a,b,c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

print("-------------------Unpack a collection------------------------------")
#Unpack a collection

fruits = ["apple","banana","cherry"]
ap, ba , ch = fruits

print(ap,ba,ch)
