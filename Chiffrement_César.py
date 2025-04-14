alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

texte = input("Entrez votre texte : ").upper()
decalage = int(input("Entrez le décalage : "))

resultat = ''
for lettre in texte:
    if lettre in alphabet:
        position = alphabet.find(lettre)
        nouvelle_position = position + decalage
        if nouvelle_position >= 26:
            nouvelle_position -= 26
        elif nouvelle_position < 0:
            nouvelle_position += 26
        resultat += alphabet[nouvelle_position]
    else:
        resultat += lettre

print("Résultat :", resultat)