alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def dechiffrer_tous_les_decalages(texte):
    texte = texte.upper()
    for decalage in range(26):
        resultat = ''
        for lettre in texte:
            if lettre in alphabet:
                position = alphabet.find(lettre)
                nouvelle_position = (position - decalage) % 26
                resultat += alphabet[nouvelle_position]
            else:
                resultat += lettre
        print(f"Décalage {decalage:>2} : {resultat}")


texte = input("Entrez le texte chiffré : ")
dechiffrer_tous_les_decalages(texte)