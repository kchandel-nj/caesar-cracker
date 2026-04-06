# Libraries
from CharToNum import ctn

class caesar_cipher:

    def __init__(self) -> None:
        self.converter = ctn()

    def encrypt(self, word: str, shift: int) -> str:
        
        ciphertext = ""
        for char in word.lower():
            if char != " ":
                ciphertext += self.converter.numToChar(self.converter.charToNum(char) + shift)
            else:
                ciphertext += char

        return ciphertext
    
    def decrypt(self, ciphertext: str, shift: int) -> str:

        return self.encrypt(ciphertext, 0 - shift)