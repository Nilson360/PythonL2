"""
Le programme va itérer pour ajouter successivement un terme 1/n2 à la série.

La série étant décroissante, à chaque itération, la valeur positive cumulée est de plus
 en plus petite. Or, dans un ordinateur, la précision d'un réel est limité : ses décimales
  sont en nombre limité. Par conséquent, il va arriver un moment où le terme à cumuler sera 
  tellement petit par rapport à la somme partielle que celle-ci ne sera pas modifiée (le cumul est
   en dessous de la précision). A partir de là, inutile de continuer, le phénomène se reproduira systématiquement
    à chaque tour. On va prendre ce critère comme test d'arrêt (sans préjuger de la qualité du résultat obtenu).
"""
s = 0
i = 1
s2 = -1 # il faut juste que s2 soit différent de s pour entrer au moins une fois dans la boucle

while (s!=s2):
    s2 = s
    s +=1.0/(i*i)
    i +=1

print(f"La somme obtenue en {i} itérations est {s}")