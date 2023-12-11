import collections

def frequency_attack(ciphertext, top_n=10):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    results = []

    for shift in range(26):
        decrypted_text = decrypt_cesar(ciphertext, shift)
        letter_freq = collections.Counter(decrypted_text.lower())
        total_letters = sum(letter_freq[letter] for letter in alphabet)
        correlation_score = sum((letter_freq[letter] / total_letters) * expected_freq[letter] for letter in alphabet)

        results.append((decrypted_text, shift, correlation_score))

    # Mostrar os top_n resultados
    results.sort(key=lambda x: x[2], reverse=True)
    for i in range(min(top_n, len(results))):
        print(f"Resultado {i + 1}: Shift={results[i][1]}, Correlação={results[i][2]:.4f}")
        print(results[i][0])
        print()

def decrypt_cesar(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Frequência esperada de letras em português
expected_freq = {'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499, 'e': 0.1257, 'f': 0.0102, 'g': 0.0130,
                 'h': 0.0072, 'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278, 'm': 0.0474, 'n': 0.0505,
                 'o': 0.1073, 'p': 0.0252, 'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434, 'u': 0.0463,
                 'v': 0.0167, 'w': 0.0001, 'x': 0.0021, 'y': 0.0001, 'z': 0.0047}

# Texto cifrado para teste
ciphertext = "Uifsf jt b tfdsfu jtuxbufe dsfeju xjui b tqvhpvq vq jnh mbtu ufssz"

# Executar ataque de frequência
frequency_attack(ciphertext, top_n=10)