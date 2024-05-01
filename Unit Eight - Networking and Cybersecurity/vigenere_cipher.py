import string

def create_vigenere_table():
    vigenere_table = []
    for i in range(26):
        row = [(i + j) % 26 for j in range(26)]
        vigenere_table.append(row)
    return vigenere_table

def display_vigenere_table():
    vigenere_table = create_vigenere_table()
    print("Vigenère Cipher Lookup Table:")
    print(" ", end=" ")
    for i in range(26):
        print(chr(65 + i), end=" ")
    print()
    for i in range(26):
        print(chr(65 + i), end=" ")
        for j in range(26):
            print(chr(65 + vigenere_table[i][j]), end=" ")
        print()


def vigenere_encrypt(plain_text, keyword):
    plain_text = plain_text.upper()
    keyword = keyword.upper()
    vigenere_table = create_vigenere_table()
    encrypted_text = ""
    keyword_repeated = (keyword * (len(plain_text) // len(keyword))) + keyword[:len(plain_text) % len(keyword)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            row = ord(plain_text[i]) - 65
            col = ord(keyword_repeated[i]) - 65
            encrypted_text += chr(vigenere_table[row][col] + 65)
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenere_decrypt(encrypted_text, keyword):
    encrypted_text = encrypted_text.upper()
    keyword = keyword.upper()
    vigenere_table = create_vigenere_table()
    decrypted_text = ""
    keyword_repeated = (keyword * (len(encrypted_text) // len(keyword))) + keyword[:len(encrypted_text) % len(keyword)]
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            col = ord(keyword_repeated[i]) - 65
            for j in range(26):
                if vigenere_table[j][col] == ord(encrypted_text[i]) - 65:
                    decrypted_text += chr(j + 65)
                    break
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text

# Example usage:
display_vigenere_table()
plain_text = "Hello, World!"
keyword = "KEY"
encrypted_text = vigenere_encrypt(plain_text, keyword)
print("\nPlain text:", plain_text)
print("Encrypted text:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
