def feistel_cipher(text, rounds):
    left, right = text[:len(text)//2], text[len(text)//2:]
    
    for _ in range(rounds):
        next_right = chr(ord(right[-1]) + 1)  # Substituição simples, pode ser melhorada
        next_left = right
        right = next_right
        left = next_left
    
    cipher_text = left + right
    return cipher_text

def feistel_decipher(cipher_text, rounds):
    left, right = cipher_text[:len(cipher_text)//2], cipher_text[len(cipher_text)//2:]
    
    for _ in range(rounds):
        next_left = chr(ord(left[-1]) - 1)  # Inverso da substituição simples
        next_right = left
        left = next_left
        right = next_right
    
    text = left + right
    return text

# Exemplo com texto "AB" e 2 rounds
plaintext = "AB"
rounds = 2

# Cifragem
ciphertext = feistel_cipher(plaintext, rounds)
print(f'Texto cifrado: {ciphertext}')

# Decifragem
deciphertext = feistel_decipher(ciphertext, rounds)
print(f'Texto decifrado: {deciphertext}')
