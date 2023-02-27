# Conditions:

from math import sqrt
x=4
if x>0: print(sqrt(x))

if x>=0:
    y = sqrt(x)
    print(y)


#if et else :
import math
if x>0:
    y = math.sqrt(x)
else:
    print(f"{x} est négatif, et n'a pas doc de racine carrée")

# Utilisation de l'elif:

a = 1
b = 2
c = 4
if a!=0:
    delta = b*b-4*a*c
    if delta>0:
        print("écrire le test")
    elif delta ==0:
        print("écrire le test")
    else:
         print("écrire le test")
else:
    if(b!=0):
     print("0")
    else:
        print("écrire le test")

# Instruction While :

s=0
i=100

while i>0:
    s +=i
    i -= 1
    print(f"Somme de 100 premiers entiers = {s}")

import math
x = float(input("Entrer un nombre:  "))

if x>=0:
    y = math.sqrt(x)
    print(f"La racine carrée de {x} est {y}")
else:
    print(f"{x} n'a pas donc de racine carrée")
    
