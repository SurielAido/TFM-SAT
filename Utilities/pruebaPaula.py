import sys
import argparse

def encrypt(text, out):
    keyPos = 0
    encrypted = ""
    for x in text:
        tChtr = ord(x)
        encChtr = chr((tChtr + ord(out[keyPos])) % 255)
        encrypted += encChtr
        # if len(keyPos) > keyPos:
        keyPos = keyPos % len(out)
        return encrypted

def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)

        keyPos = keyPos % keylen
    return decrypted