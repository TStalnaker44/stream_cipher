
import random

SECRET_KEY = 12345 # very secure

def main():
##    messages = ["Hi how are you?",
##                "Do you want to grab coffee?",
##                "Please answer me",
##                "Okay ghost me then"]
    messages = ["Hi"] * 5
    # Notice that the cipher text is different each time
    # because of the IV
    for iv, m in enumerate(messages):
        sendMessage(m, iv)

def sendMessage(message, iv):
    # Prepare message
    print("Message:", message)
    m = textToInt(message)
    
    ## Alice
    cipher = encrypt(m, iv)
    print("Encrypted:", intToText(int(cipher,2)))

    ## Bob
    m = intToText(decrypt(cipher, iv))
    print("Decrypted:", m)

def textToInt(string):
    return int("".join([bin(ord(c))[2:].zfill(8) for c in string]), 2)

def intToText(num):
    # Convert to binary
    b = bin(num)[2:]
    b = ("0" * (8-len(b)%8)) + b
    return "".join([chr(int(b[i:i+8],2)) for i in range(0, len(b), 8)])
        
def encrypt(message, iv):
    # Get the length for the bit string
    bits = len(bin(message)[2:])

    # Generate the bit string
    r_alice = random.Random()
    seed = SECRET_KEY ^ iv
    r_alice.seed(seed)
    key = r_alice.getrandbits(bits)

    # Encrypt the message
    cipher = message ^ key

    return bin(cipher)[2:].zfill(bits)

def decrypt(cipher, iv):
    # Get the length for the bit string
    bits = len(cipher)

    # Generate the bit string
    r_bob = random.Random()
    seed = SECRET_KEY ^ iv
    r_bob.seed(seed)
    key = r_bob.getrandbits(bits)

    # Encrypt the message
    message = int(cipher,2) ^ key

    return message

if __name__ == "__main__":
    main()
    

