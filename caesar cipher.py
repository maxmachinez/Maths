#caesar cipher 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def ceaserCipher(plaintext, key):
    plaintext = plaintext.lower()
    plaintext = plaintext.strip()
    ciphertext = ""
    for i in plaintext:
        p = alphabet.index(i)
        if i == " ":
            ciphertext += " "
            nP = (p + key) % 27
            ciphertext += alphabet[nP]
        elif p == " ":
              p = alphabet.index(i + 1)
              nP = (p + key) % 27
              ciphertext += alphabet[nP]
        else:
             nP = (p + key) % 27
             ciphertext += alphabet[nP]

    return ciphertext



    

plaintext =  str(input("What text do you want to encrypt?"))
key = int(input("By what key do you want to encrypt by?"))

print("This is your encrypted message: ", ceaserCipher(plaintext, key))
