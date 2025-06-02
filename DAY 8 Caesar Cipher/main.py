import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = alphabet + alphabet
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
    encrypted_word = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_word += letter
        else:
            encrypted_word += (alphabet[alphabet.index(letter) + shift_amount])
    print(f"Here is the encoded result: {encrypted_word}")
def decrypt(original_text, shift_amount):
    decrypted_word = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_word += letter
        else:
            decrypted_word += (alphabet[alphabet.index(letter) - shift_amount])
    print(f"Here is the decoded result: {decrypted_word}")

def caesar(c_direction):
    if c_direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
caesar(direction)
decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
while decision == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction)
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
print("Goodbye")