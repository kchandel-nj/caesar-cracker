# Libraries
from CaesarCipher import caesar_cipher
import enchant

class cracker:

    def __init__(self) -> None:
        self.cc = caesar_cipher()
        self.d = enchant.Dict("en_US")

    def crack(self, ciphertext: str, all: bool) -> tuple[str, int]:
        
        for i in range(1, 26):
            potential = self.cc.encrypt(ciphertext, i)
            if self.d.check(potential):
                answer = (potential, 26 - i)
                return answer
        return (ciphertext, -1)
    
cc = caesar_cipher()
crack = cracker()
word = "hello"
enc = cc.encrypt(word, 15)
print(enc)
print("Cracking...")
cracked = crack.crack(enc, False)
print(cracked)