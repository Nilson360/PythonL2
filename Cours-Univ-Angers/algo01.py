s = "combien y a-t-il de voyelles dans cette phrase ?"
nb_voyelle = 0
for c in s:
  if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='y':
    nb_voyelle += 1
print(f"'{s}' contient {nb_voyelle} voyelles.")