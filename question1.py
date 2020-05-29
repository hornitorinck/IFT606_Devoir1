import string
import random

alphanumericals = string.ascii_lowercase + string.ascii_uppercase + string.digits

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def generateKey(numLetters: int)->str:
    key = ''
    for i in range(numLetters):
        key += random.choice(alphanumericals)
    return key

def encode(text: str, key: str)->bytes:
    return byte_xor(bytes(text, "ascii"), bytes(key, "ascii"))

def decode(cypher: bytes, key: str)->str:
    return byte_xor(cypher, bytes(key, "ascii")).decode('ascii')

if __name__ == "__main__":
    # TODO: valider l'entree
    message = input("Enter your cypher text: ")
    key = generateKey(len(message))
    print("Securely passed key to Alice.")
    cypher = encode(message, key)
    print(f"Cypher text: {cypher}")
    message = decode(cypher, key)
    print(message)