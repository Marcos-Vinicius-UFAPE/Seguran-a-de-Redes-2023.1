def hill_encrypt(message, key):
    string = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    
    message = message.upper() # Coloca a string passada em maiúsculo
    n = key.ncols() # Verifica o tamanho da chave

    if len(message) % n != 0: # Coloca 'Z' no final da mensagem se necessário
        message += 'Z' * (n - len(message) % n)

    ciphertext = '' # Inicializa uma string vazia

    for i in range(0, len(message), n): # Divide a mensagem em blocos de tamanho n, percorrendo os mesmos
        block = message[i:i+n] # Converte o bloco em vetor coluna
        block = vector([string.index(ch) for ch in block])

        encrypted_block = block * key  % 26 # Encripta o bloco

        ciphertext += ''.join([string[i] for i in encrypted_block]) # Converte o vetor resultante em uma string

    return ciphertext

def hill_decrypt(message, key):
    string = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'

    n = key.ncols() # Verifica o tamanho da chave
    plaintext = ''  # Inicializa uma string vazia
    
    inverse = key^-1 % 26
    
    for i in range(0, len(message), n): # Divide a mensagem em blocos de tamanho n, percorrendo os mesmos
        block = message[i:i+n] # Converte o bloco em um vetor de coluna
        block = vector([string.index(ch) for ch in block])
        
        decrypted_block = block * inverse % 26 # Decripta o bloco
        plaintext += ''.join([string[i] for i in decrypted_block]) # Converte o bloco decriptado em string

    plaintext = plaintext.rstrip('Z') # Remove os caracteres adicionais colocados no final da string

    return plaintext

message = "SEGURANCAREDES"
# Encrypt the plaintext message

ciphertext = hill_encrypt(message, matrix([[1,2],[3,5]]))

print("Ciphertext: ", ciphertext)
result = hill_decrypt(ciphertext, matrix([[1,2],[3,5]]))
print("Result: ", result)