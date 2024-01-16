def chiffrement_cesar(message, cle):
    resultat = ""
    for i, caractere in enumerate(message):
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            decalage = ord(cle[i % len(cle)]) - ord('a') if cle[i % len(cle)].islower() else ord(cle[i % len(cle)]) - ord('A')
            resultat += chr((ord(caractere) - base + decalage) % 26 + base)
        else:
            resultat += caractere
    return resultat

def dechiffrement_cesar(message_chiffre, cle):
    return chiffrement_cesar(message_chiffre, ''.join([chr((26 - (ord(c) - ord('a'))) + ord('a')) if c.islower() else chr((26 - (ord(c) - ord('A'))) + ord('A')) for c in cle]))

# Exemple d'utilisation
message_original = "Bonjour, comment ca va ?"
cle = "clesecrete"

# Chiffrement
message_chiffre = chiffrement_cesar(message_original, cle)
print("Message chiffré:", message_chiffre)

# Déchiffrement
message_dechiffre = dechiffrement_cesar(message_chiffre, cle)
print("Message déchiffré:", message_dechiffre)
