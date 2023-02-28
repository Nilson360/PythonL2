# Cours du 28/02/2023 
#TP : Page 1 - Exercice 1

# 1) L’entier n est divisible par 5?

n = int(input("Entrez votre numéro: "))
test = n%5
if (test==0):
    print(f"L'entier {n} est divisible par 5 car le reste de la division est {test}")
else :
    print(f"Non, l'entier {n} n'est pas divisible par 5 car le reste de la division est {test}")

# 2) Il existe un triangle de cˆot ́es a, b et c (positifs)

a,b,c = 3,4,5
max(a,b,c) <= min(a+b,a+c,b+c)

# 3) Les entiers m, l et p sont de même signe?
m = int(input("Entrez votre numéro (m): "))
l = int(input("Entrez votre numéro (l): "))
p = int(input("Entrez votre numéro (p): "))

if (m*l>=0 and m*p>=0) :
    print(f"Les entiers sont de même signe {m},{l},{p}")
else :
     print(f"Les entiers ne sont pas de même signe {m},{l},{p}")

# 4) Le point de coordonnées (x,y) est à l’intérieur du cercle centr é en O et de rayon r?

r = int(input("Entrez la valeur du rayon: "))
x = int(input("Entrez la valeur de X: "))
y = int(input("Entrez la valeur de Y: "))

from math import sqrt
test = sqrt(x**2 + y**2)

if test<= r :
    print(f"OUI, les points de coordonnées (x,y)({x},{y}) du circles de rayon {r} sont à l'intérieur du cercle")
else :
     print(f"NON, les points de coordonnées (x,y)({x},{y}) du circles de rayon {r} ne sont pas à l'intérieur du cercle")

# 5) Le cosinus et le sinus de θ ∈[0,2π] sont positifs

from math import cos,sin,pi
t= 2
cos(t)>=0 and sin(t)>= 0

 t -= 0 and t -= pi/2