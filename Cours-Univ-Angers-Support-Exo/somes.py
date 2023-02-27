n = int(input("nombre: "))

print(f" La somme de {n} premiers entier", end="")

s=0
while n>0:
    s +=n
    n -=1
    print(f"{s}")