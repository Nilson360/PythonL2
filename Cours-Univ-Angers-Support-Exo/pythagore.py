import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a!=0:
    delta = b*b-4*a*c
    if delta>0:
         x1=(-b-math.sqrt(delta))/(2*a)
         x2=(-b+math.sqrt(delta))/(2*a)
         print(f"Il y a deux racinnées réelles distinctes: {x1} et {x2}")
    elif delta==0:
            x=-b/(2*a)
            print(f"Une racine réelle double: {x}")
    else:
                print("pas de racines réelles")
else:
    if(b!=0):
        x=-c/b
        print(f"L'équation est de degré 1 et la solution est {x}")
    else:
        print("L'équation n'a pas de racines")