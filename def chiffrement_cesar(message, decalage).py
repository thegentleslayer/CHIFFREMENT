def chiffrement_cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            resultat += chr((ord(caractere) - base + decalage) % 26 + base)
        else:
            resultat += caractere
    return resultat

def dechiffrement_cesar(message_chiffre, decalage):
    return chiffrement_cesar(message_chiffre, -decalage)

# Exemple d'utilisation
message_original = "Bonjour, comment ca va ?"
decalage = 3

# Chiffrement
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message chiffré:", message_chiffre)

# Déchiffrement
message_dechiffre = dechiffrement_cesar(message_chiffre, decalage)
print("Message déchiffré:", message_dechiffre)


