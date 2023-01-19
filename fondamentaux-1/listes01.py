# Étude des listes avec python - Calcul approfondie 2023
# 
# Une liste est une structure de données qui contient une série de valeurs.
# Dans une liste nous pouvons avoir des données de differents types ou du même type (int, float string)

# EXEMPLE DE LISTES 
animaux = ["girafe", "tigre", "singe","souris"]
tailles = [5, 2.5, 1.75, 0.15] 
mixte = ["girafe", 5, "souris", 0.15]

# La première liste est composée que sur des données du type String
# Le seconde tous les données sont du type Number(int et float)
# Le troisième est un mix des deux , int, string et float.

print(animaux)
print(tailles)
print(mixte)

# Chaque élément d'une liste occupée une position allant de 0 à n-1

# OPÉRATIONS SUR LES LISTES

# Dans les listes, nous pouvons utiliser les opérateurs, + pour concaténer deux listes et l'opérateur * pour la duplication
ani1 =["girade", "tigre"]
ani2 = ["singe","souris"]

print(ani2+ani2)

# Pour ajounter un élément dans une liste, on utilise la méthode .append()
a = []
a.append(13)
a.append("maison")
print(a)

# Par contre, nous pouvons aussi ajouter un élément avec l'opérateur +
# Mais, prévilegions toujours la méthode .append()
a = a +[-5]
print(a)

# TRANCHES
# Ce principe consiste à choisir une plage à afficher/utiliseur en utilisant l'indiçage, sur le modèle [m:n+1],
#m est un élément inclus et n+1 est exclu

# EXEMPLE 
print("---------------- TRANCHES ----------------")
print(animaux[0:2])
print(animaux[0:3])

# En utilisant les tranches nous pouvons définir aussi le pas 
#[début:fin:pas]

print("---------------- TRANCHES AVEC PAS----------------")
X = [0,1,2,3,4,5,6,7,8,9]
print(animaux[0:3:2])
print(X[1:6:3])