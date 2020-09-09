# Affine Cipher

The affine cipher is a type of a monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent and encrypted using a simple mathematical function.

The secret key of this cipher is a rule that looks like this: E(x) = ax + b mod 26, more specifically, the a and b values.

To encrypt a message, use the encrypt() function that takes in three arguments: plaintext (a string), a (an integer) and b(an integer).

To decrypt a message, use the decrypt() function that takes in the same three arguments as the encrypt() funtion for the exception of the plaintext, which is replaced by the ciphertext.
