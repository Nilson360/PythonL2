import math
x = int(input("Entrer un nombre:  "))

if x>=0:
    y = math.sqrt(x)
    print(f"La racine carrée de {x} est {y}")
else:
    print(f"{x} n'a pas donc de racine carrée")
    
