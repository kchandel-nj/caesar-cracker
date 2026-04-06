# Libraries
from Cracker import cracker
from CaesarCipher import caesar_cipher

# Main
cc = caesar_cipher()
c = cracker()

while True:
    operation = int(input("Choose operation:\n1. Encrypt\n2. Decrypt\n3. Crack\n4. Quit\n"))
    if operation == 1:
        word = input("What will be encrypted?")
        shift = int(input("How much will it be shifted?"))
        print(cc.encrypt(word, shift))
    elif operation == 2:
        ciphertext = input("What will be decrypted?")
        key = int(input("What is the shift key?"))
        print(cc.decrypt(ciphertext, key))
    elif operation == 3:
        ciphertext = input("What is the word being cracked?")
        all = input("Would you like all possible iterations of ciphertext? [y/n]")
        if all.lower == "y":
            print(c.crack(ciphertext, True))
        else:
            print(c.crack(ciphertext, False))
    elif operation == 4:
        print("Goodbye.")
        break
    else:
        print("Error: Unknown command. Please try again.")