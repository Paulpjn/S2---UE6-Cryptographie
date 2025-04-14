
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cle_fixe = "KEYKEYKEYKEY"

texte = input("Message à chiffrer: ").upper()
resultat = ''

for i in range(len(texte)):
    lettre = texte[i]
    if lettre in alphabet: 
        lettre_cle = cle_fixe[i % len(cle_fixe)]
        decalage = alphabet.index(lettre_cle)
        position = alphabet.index(lettre)
        nouvelle_position = (position + decalage) % 26
        resultat += alphabet[nouvelle_position]
    else:
        resultat += lettre  
print("Message chiffré:", resultat)