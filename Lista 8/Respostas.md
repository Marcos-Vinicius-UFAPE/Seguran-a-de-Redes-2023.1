**1. Por que mdc(n, n + 1) = 1 é para dois inteiros consecutivos n e n + 1?**

O MDC de dois números é o maior número que os divide sem deixar resto. Para qualquer número inteiro n, os números n e n+1 são consecutivos. Se assumirmos que algum número d é divisor tanto de n quanto de n+1, então ele também teria que dividir a diferença entre os dois, que é (n+1) - n = 1. Como o único inteiro positivo que divide 1 é o próprio 1, isso implica que o MDC(n, n+1) deve ser 1.


**2. Usando o teorema de Fermat, encontre 3^201 mod 11.**

O Pequeno Teorema de Fermat afirma que se p é um número primo, então para qualquer inteiro a, o número a^p − a é um múltiplo inteiro de p. Na forma de congruências, a^p ≡ a (mod p). Como 201 não é uma potência de 11, simplificamos o problema encontrando 201 módulo 11 diretamente: 201 ≡ 3 (mod 11) pois 201 = 18 * 11 + 3.

**3. Use o teorema de Fermat para encontrar um número a entre O e 72, com a congruente a 9794 módulo 73.**

O Pequeno Teorema de Fermat também nos diz que se p é primo e a não é divisível por p, então a^(p-1) ≡ 1 (mod p). Para o caso com p = 73, que é primo, e a = 9794, podemos escrever 9794 ≡ a^k (mod 73), onde k é algum inteiro positivo. Como 73 é primo, podemos usar o Pequeno Teorema de Fermat para encontrar que a^(72) ≡ 1 (mod 73) para qualquer inteiro a que não seja um múltiplo de 73. O número 9794 pode ser escrito como 9794 = 72 * 136 + 2, então 9794 ≡ 2 (mod 73).

**4. Use o teorema de Euler para encontrar um número a entre 0 e 9, tal que a seja congruente a 7^1000 módulo 10. (Observe que isso é o mesmo que o último dígito da expansão decimal de 7^1000.)**

O Teorema de Euler afirma que se n e a são primos entre si, então a^φ(n) ≡ 1 (mod n), onde φ(n) é a função totiente de Euler. Como 10 e 7 são primos entre si, podemos usar este teorema. Mas aqui, como estamos procurando o módulo 10, que não é primo, ainda podemos usar o fato de que 7^4 ≡ 1 (mod 10) porque 7 é relativamente primo a 10, e φ(10) = 4. Portanto, 7^1000 ≡ (7^4)^(250) ≡ 1^250 ≡ 1 (mod 10). O último dígito de 7^1000 é 1.

**5. Use o teorema de Euler para encontrar um número x entre 0 e 28, com x 85 congruente a 6 módulo 35 (Você não precisará usar qualquer pesquisa por força bruta).**

Primeiro, encontramos φ(35), que é φ(5) * φ(7) = 4 * 6 = 24 porque 35 = 5 * 7 e 5 e 7 são primos. De acordo com o Teorema de Euler, se mdc(a, n) = 1, então a^φ(n) ≡ 1 (mod n). Portanto, x^24 ≡ 1 (mod 35) para qualquer x que seja primo com 35. Como 85 = 24 * 3 + 13, podemos escrever x^85 como (x^24)^3 * x^13. Como x^24 ≡ 1 (mod 35), isso simplifica para x^13 ≡ 6 (mod 35).
Para encontrar tal x sem força bruta, procuramos um inteiro que, ao ser elevado à 13ª potência, resulte em um número terminado em 6 e seja primo com 35. O número 1 é o único número entre 0 e 28 que satisfaz essa condição, e 1^13 ≡ 1 (mod 35). No entanto, 1 não satisfaz a congruência original porque 1 não é congruente a 6 módulo 35. Portanto, devemos encontrar uma abordagem diferente. Note que se x é primo com 35, então x^24 ≡ 1 (mod 35), e podemos multiplicar ambos os lados da congruência x^24 ≡ 1 (mod 35) por 6 para obter x^24 * 6 ≡ 6 (mod 35).
Isso significa que para qualquer x que seja primo com 35, x^(φ(35) + 1) ≡ 6 (mod 35). Como 85 não está na forma 24k + 1, não podemos encontrar um x usando esse método que satisfaça a congruência dada diretamente. No entanto, podemos encontrar um inteiro m tal que m^1 ≡ 6 (mod 35) e então elevar m à potência que nos dá x^85. Sabemos que 6^1 ≡ 6 (mod 35), e elevar 6 a qualquer potência que termine em 1 nos dará o mesmo último dígito. Portanto, estamos procurando um expoente na forma de 24k + 13 que seja próximo de 85, e como acontece, 85 em si está nessa forma (24 * 3 + 13). Assim, x = 6 satisfaz x^85 ≡ 6^85 ≡ 6 (mod 35).

**6. Observe, na Tabela 8.2, que φ(n) é par para n > 2. Isso é verdadeiro para todo n > 2. Dê um argumento conciso para explicar por que isso acontece.**

A função totiente de Euler, denotada por φ(n), conta o número de inteiros até n que são primos entre si com n. Para qualquer inteiro n > 2, há um número par de inteiros até n porque para cada número coprimo k há um n-k correspondente que também é primo com n. Como n > 2 implica que n não é primo, haverá pelo menos um par de números coprimos, portanto φ(n) é par.

**7. Se n é composto e passa no teste de Miller-Rabin para a base a, então n é chamado de pseudo-primo forte à base a. Mostre que 2047 é um pseudoprimo à base 2.**

O teste de primalidade de Miller-Rabin é baseado na propriedade de que para qualquer número primo n, n-1 é um número par e pode ser escrito como 2^s * d, onde s e d são inteiros, e d é ímpar.
Se n é primo, então para qualquer a < n, ou a^d ≡ 1 (mod n) ou existe um 't' tal que 0 ≤ t < s e a^(2^t * d) ≡ -1 (mod n).
Aplicamos isso a 2047 = 2^11 - 1, que é 2^11 - 1 = 23 * 89. Escrevendo 2047 - 1 como 2^s * d, obtemos 2^10 * 1, então s = 10 e d = 1. Em seguida, verificamos se 2^d ≡ 1 (mod 2047) ou se 2^(2^t * d) ≡ -1 (mod 2047) para 0 ≤ t < s.
Acontece que 2^2 ≡ 4, 2^4 ≡ 16, 2^8 ≡ 256 e 2^16 ≡ 65536. Como 2047 não é uma potência de 2, precisamos reduzir isso módulo 2047 para encontrar se algum desses é igual a -1. Acontece que 2^(2^10) ≡ 1 (mod 2047), o que significa que 2047 passa no teste de Miller-Rabin para a base 2, indicando que é um forte pseudo-primo para a base 2.


**8. O exemplo usado por Sun-Tsu para ilustrar o CRT foi**
   
   **x = 2 (mod 3); x = 3 (mod 5); x = 2 (mod 7).**

**Solucione para x.**

Para resolver um sistema de congruências lineares, podemos usar o Teorema Chinês do Resto, que afirma que se n1, n2, ..., nk são inteiros positivos primos entre si dois a dois, então o sistema de congruências simultâneas x ≡ a1 (mod n1), x ≡ a2 (mod n2), ..., x ≡ ak (mod nk) tem uma solução, e essa solução é única módulo N = n1 * n2 * ... * nk.

Para o sistema dado:
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)

Os módulos são primos entre si. Procedemos com o Teorema Chinês do RestoImportant Information: [Enter any specific mathematical terms or phrases that you want to ensure are included or clarified in the translation.]