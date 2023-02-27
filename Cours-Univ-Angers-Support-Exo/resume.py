print(type(1/3))
print(type("abc"))

from math import sqrt # autre forme d'importer une fonction en ciblant l'élément volue
print(sqrt(4))
(-1.1).is_integer()
print(id("adb")) #trouver l'adresse d'une variable

print(type(1j+(1+2j)))
from math import cos,tan,sin
print(f"Le cossenus de l'angle 14 est {cos(14)}")
print(f"Le sinus de l'angle 14 est {sin(14)}")
print(f"La tengant de l'angle 14 est {tan(14)}")

# Opérateur is => utilisée pour voir si deux opérandes sont égales
# Exemple :
    2 is(1+1)
    "abc" is "a"+"b"+"c"
    2 is (1 + 1.0)


#L'entier n est un multiple de 5
#L'xpression : 
n=10
n%5==0


#Les entiers n est m sont tels que l'un est multiple de l'autre
#L'expression : 
m=12
n%m==0 or m%n==0

# Les entiers m et n sont de même signes 
#L'expression :
n*m>0

# Les entiers m,n et p sont de même signes 
#L'expression :
m*n>0 and m*p>0

# Les entiers m,n et p sont distincts 2 à 2
# L'expression :

m!=n!=p and m!=p

# Le conjugé d'un nombre complexe :

print((1+2j).conjugate())

