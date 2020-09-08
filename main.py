# Affine Cipher

# Setup
alphabet = "abcdefghijklmnopqrstuvwxyz"
#   Every possible a value that has a multiplicative inverse in the mod26
a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
#   Multiplicative inverses of every a value
a_inverses = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

# Encryption
def encrypt(plaintext, a, b):
    # Checking if the specified a value has a multiplivative inverse
    if a in a_values:
        ciphertext = ""
        for character in plaintext:
            # Creating a new variable that will allow capital letters to stay capital after encryption
            is_upper = False
            if character.lower() in alphabet:
                if character not in alphabet:
                    is_upper = True
                character = character.lower()
                encrypted_letter = alphabet[(alphabet.index(character) * a + b) % 26]
                if is_upper == True:
                    encrypted_letter = encrypted_letter.upper()
                ciphertext += encrypted_letter
            else:
                ciphertext += character
        print(ciphertext)
    else:
        print("Invalid a value.")

# Decryption
def decrypt(ciphertext, a, b):
    # Checking if the specified a value has a multiplivative inverse
    if a in a_values:
        plaintext = ""
        for character in ciphertext:
            # Creating a new variable that will allow capital letters to stay capital after decryption
            is_upper = False
            if character.lower() in alphabet:
                if character not in alphabet:
                    is_upper = True
                character = character.lower()
                decrypted_letter = alphabet[(a_inverses[a_values.index(a)] * (alphabet.index(character)- b)) % 26]
                if is_upper == True:
                    decrypted_letter = decrypted_letter.upper()
                plaintext += decrypted_letter
            else:
                plaintext += character
        print(plaintext)
    else:
        print("Invalid a value.")
