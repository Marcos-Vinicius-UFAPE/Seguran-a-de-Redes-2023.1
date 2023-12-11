def encrypt_cesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt_cesar(ciphertext, shift):
    return encrypt_cesar(ciphertext, -shift)

# Exemplo de uso:
plaintext = "Hello, World!"
shift_value = 3

# Encriptação
ciphertext = encrypt_cesar(plaintext, shift_value)
print("Texto cifrado:", ciphertext)

# Decriptação
decrypted_text = decrypt_cesar(ciphertext, shift_value)
print("Texto decifrado:", decrypted_text)
