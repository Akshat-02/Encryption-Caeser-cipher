import cart

print(cart.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(plain_text,shift,direction):
    if direction == "encode":
        encrypted_text = ""
        for char in plain_text:
            if char in alphabet:
            
                n = alphabet.index(char) + shift
                encrypted_text += alphabet[n]
            
            else:
                encrypted_text += char
    
        print(encrypted_text)

    if direction == "decode":
        decrypted_text = ""
        for char in plain_text:
            if char in alphabet:
             
                n = int(alphabet.index(char,26,52)) - shift
                decrypted_text += alphabet[n]
    
        print(decrypted_text)

        
caeser(text,shift,direction)

