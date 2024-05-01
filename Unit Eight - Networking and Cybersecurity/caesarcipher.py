def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

# Example usage:
original_text = "Hello, World!"
shift = 3
text_upper = original_text.upper()
encrypted_text = caesar_cipher(text_upper, shift)
print("Original text:", original_text)
print("Encrypted text:", encrypted_text)
