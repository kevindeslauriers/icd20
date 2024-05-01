def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    plaintext = "thediligentstudentmeticulouslyreviewedthecomplexalgorithmbeforeimplementingitintheprogram"
    shift = 5

    # Encrypt the plaintext
    encrypted_text = caesar_encrypt(plaintext, shift)
    print("Encrypted:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Decrypted:", decrypted_text)


main()
