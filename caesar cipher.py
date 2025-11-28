ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
def caesarCipher(plaintext, key):
    plaintext = plaintext.lower()
    plaintext = plaintext.strip()
    ciphertext = ""
    for i in plaintext:
        p = ALPHABET.index(i)
        nP = (p + key) % 27 
        if i == " ":
            ciphertext += " "
        elif p == " ":
              p = ALPHABET.index(i + 1)
              ciphertext += ALPHABET[nP]
        else:
             ciphertext += ALPHABET[nP]
    return ciphertext
def caesarDecrypter(cText, key):
     cText.strip()
     cText.lower()
     plaintext = ""
     for i in cText:
          p = ALPHABET.index(i)
          if i == " ":
               plaintext += " "
          else:
               nP = (p - key) % 27
               plaintext += ALPHABET[nP]
     return plaintext
choice = int(input("What do you want to do? Encrypt or Decrypt? (0 and 1 respectively):  "))
match choice:
     case 0:
        plaintext =  str(input("What text do you want to encrypt?"))
        key = int(input("By what key do you want to encrypt by?"))
        print("This is your encrypted message: ", caesarCipher(plaintext, key))
     case 1:
        ciphertext = str(input("What is the ciphertext?"))
        key = int(input("By what key do you want to shift back by?"))
        print("Your decrypted message is:", caesarDecrypter(ciphertext, key))