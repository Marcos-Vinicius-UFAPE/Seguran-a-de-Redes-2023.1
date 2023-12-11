**1. Defina resumidamente, um grupo, um anel, um corpo.**

1. Grupo: Um grupo é uma estrutura algébrica que consiste em um conjunto não vazio de elementos, juntamente com uma operação binária associativa que combina quaisquer dois elementos do conjunto, e possui um elemento neutro (identidade) e inversos para cada elemento.

2. Anel: Um anel é uma estrutura algébrica que consiste em um conjunto não vazio de elementos, juntamente com duas operações binárias (adição e multiplicação) que satisfazem propriedades específicas, como associatividade, distributividade e a existência de elementos neutros para ambas as operações. Existem anéis comutativos (quando a multiplicação é comutativa) e anéis não comutativos.

3. Corpo: Um corpo é uma estrutura algébrica mais específica e completa do que um anel. É um conjunto não vazio de elementos com duas operações binárias (adição e multiplicação) que satisfazem todas as propriedades de um anel, além do requisito de que a multiplicação seja comutativa, e que todos os elementos não nulos tenham inversos multiplicativos. Um corpo é uma estrutura fundamental em álgebra, e os números reais e complexos são exemplos de corpos.

**2. O que significa dizer que b é um divisor de a?**

Dizer que "b é um divisor de a" significa que o número b pode ser multiplicado por outro número inteiro para obter o número a como resultado, sem deixar um resto. Em termos matemáticos, se b é um divisor de a, então a é divisível por b. Isso é expresso na forma de uma equação onde a é igual a b multiplicado por algum inteiro (ou seja, a = b * k, onde k é um inteiro). 

Por exemplo, no caso de a = 12 e b = 3, podemos dizer que 3 é um divisor de 12 porque 12 pode ser dividido igualmente por 3, ou seja, 12 = 3 * 4, onde 4 é um inteiro. Portanto, 3 é um divisor de 12.

**3. Para cada uma das seguintes equações, encontre um inteiro x que satisfaça:**
**(a) 5x ≡ 4 (mod 3)**

Primeiro observamos que 5 é congruente a 2 (mod 3), porque 5 divide 2 com um resto de 1. Então a congruência se torna:
2x ≡ 4 (mod 3)

daí multiplicamos ambos os lados por 2^(-1), o inverso multiplicativo de 2 em módulo 3, que é 2:
x ≡ 4 * 2^(-1) (mod 3)

Agora, calculamos 2^(-1) em módulo 3, que é 2, porque 2 * 2 ≡ 1 (mod 3). Portanto:
x ≡ 4 * 2 (mod 3)
x ≡ 8 (mod 3)

Para encontrar um inteiro x, podemos observar que 8 é congruente a 2 (mod 3), porque 8 divide 2 com um resto de 2. Assim, x ≡ 2 (mod 3) é uma solução.

**(b) 7x ≡ 6 (mod 5)**

Primeiro, notamos que 7 é congruente a 2 (mod 5), porque 7 divide 2 com um resto de 2. Agora a congruência é:
2x ≡ 6 (mod 5)

Multiplicamos ambos os lados por 2^(-1), o inverso multiplicativo de 2 em módulo 5, que é 3:
x ≡ 6 * 3 (mod 5)
x ≡ 18 (mod 5)

18 é congruente a 3 (mod 5), pois 18 divide 3 com um resto de 3. Portanto, x ≡ 3 (mod 5) é uma solução.

**(c) 9x ≡ 8 (mod 7)**

Primeiro, notamos que 9 é congruente a 2 (mod 7), porque 9 divide 2 com um resto de 2. Agora a congruência é:
2x ≡ 8 (mod 7)

Multiplicamos ambos os lados por 2^(-1), o inverso multiplicativo de 2 em módulo 7, que é 4:
x ≡ 8 * 4 (mod 7)
x ≡ 32 (mod 7)

32 é congruente a 4 (mod 7), pois 32 divide 4 com um resto de 4. Portanto, x ≡ 4 (mod 7) é uma solução.

**4. Encontre o inverso multiplicativo de cada elemento diferente de zero em Z5.**

Em Z5, o conjunto de inteiros módulo 5, para encontrar o inverso multiplicativo de cada elemento diferente de zero (ou seja, encontrar o elemento que, quando multiplicado pelo elemento original, resulta em 1), se usa a seguinte regra:

o inverso multiplicativo b de a é aquele número que satisfaz a * b ≡ 1 (mod 5).

1. Para a = 1, o inverso multiplicativo b é 1, porque 1 * 1 ≡ 1 (mod 5).

2. Para a = 2, o inverso multiplicativo b é 3, porque 2 * 3 ≡ 1 (mod 5).

3. Para a = 3, o inverso multiplicativo b é 2, porque 3 * 2 ≡ 1 (mod 5).

4. Para a = 4, o inverso multiplicativo b é 4, porque 4 * 4 ≡ 1 (mod 5).


**5. Determine os MDC:**

**(a) mdc(24140, 16762):**

Passo 1 - Dividir 24140 por 16762:
24140 = 1 * 16762 + 7378

Passo 2 - Trocar os números. O divisor anterior (16762) se torna o novo dividendo, e o resto anterior (7378) se torna o novo divisor:
16762 = 2 * 7378 + 2006

Passo 3 - Repetir o processo:
7378 = 3 * 2006 + 2360

Passo 4:
2006 = 0 * 2360 + 2006
Chegamos a 2006 como o último divisor não nulo. Portanto, o MDC de 24140 e 16762 é 2006.

**(b) mdc(4655, 12075).**

Passo 1 - Dividir 12075 por 4655:
12075 = 2 * 4655 + 2765

Passo 2 - Trocar os números:
4655 = 1 * 2765 + 1890

Passo 3: Repetir o processo:
2765 = 1 * 1890 + 875

Passo 4: Repetir o processo:
1890 = 2 * 875 + 140

Passo 5: Repetir o processo:
875 = 6 * 140 + 35

Passo 6: Repetir o processo:
140 = 4 * 35 + 0
O último divisor não nulo é 35, então, o MDC de 4655 e 12075 é 35.

**6. Usando o algoritmo de Euclides estendido, encontre o inverso multiplicativo de:**

**(a) 1234 mod 4321;**

Usando o algoritmo de Euclides estendido, encontramos x e y:

Primeiro, a gente encontra o MDC de 1234 e 4321 usando o algoritmo de Euclides:
gcd(1234, 4321) = 1

Agora, aplicamos o algoritmo de Euclides estendido para encontrar x e y:

Passo 1:
4321 = 3 * 1234 + 119

Passo 2:
1234 = 10 * 119 + 94

Passo 3:
119 = 1 * 94 + 25

Passo 4:
94 = 3 * 25 + 19

Passo 5:
25 = 1 * 19 + 6

Passo 6:
19 = 3 * 6 + 1

Agora, trabalhamos retroativamente para encontrar x e y:

Passo 6:
1 = 19 - 3 * 6

Passo 5:
1 = 19 - 3 * (25 - 19)

Passo 4:
1 = 4 * 19 - 3 * 25

Passo 3:
1 = 4 * (119 - 94) - 3 * 25

Passo 2:
1 = 4 * 119 - 4 * 94 - 3 * 25

Passo 1:
1 = 4 * 119 - 4 * (1234 - 10 * 119) - 3 * 25

Agora, simplificando a expressão acima, obtemos:
1 = 41 * 119 - 4 * 1234 - 3 * 25

Portanto, o inverso multiplicativo de 1234 mod 4321 é 41, ou seja, 1234^(-1) ≡ 41 (mod 4321).

**(b) 24140 mod 40902;**

gcd(24140, 40902) = 2

Agora, aplicamos o retrocesso para expressar o MDC (que é 2) como uma combinação linear de 24140 e  40902:
Passo 12 (Retrocesso):
2=14−2⋅6

Passo 11:
2 = 14 − 2⋅(34 − 2⋅14) = 5.14 − 2⋅34

Passo 10:
2 = 5⋅(48 − 34) − 2⋅34 = 5⋅48 − 7⋅34
Passo 9:
2 = 5⋅48 − 7⋅(82 − 48) = 12⋅48 − 7⋅82

Passo 8:
2 = 12⋅(82 − 1⋅48) − 7⋅82 = 12⋅82 − 19⋅48

Passo 7:
2 = 12⋅82 − 19⋅(212 − 2⋅82) = 50⋅82 − 19⋅212

Passo 6:
2 = 50⋅(212 − 1⋅82) − 19⋅212 = 50⋅212 − 69⋅82

Passo 5:
2 = 50⋅212 − 69⋅(294 − 1⋅212 ) = 119⋅212 − 69⋅294

Passo 4:
2 = 119⋅(294 − 1⋅212) − 69⋅294 = 119⋅294 − 188⋅212

Passo 3:
2 = 119⋅294 − 188⋅(506 − 1⋅294) = 307⋅294 − 188⋅506

Passo 2:
2 = 307⋅(506 − 1⋅294) − 188⋅506 = 307⋅506 − 495⋅294

Passo 1:
2 = 307⋅506 − 495⋅(7378 − 14⋅506) = 7315⋅506 − 495⋅7378

Agora, simplificamos a expressão 7315⋅506 − 495⋅7378 utilizando operações módulo 40902:
7315.506 ≡ 1 (mod 40902)
- 495.7378 ≡ −495⋅(7378−18⋅40902) (mod 40902)
      ≡ − 495⋅7378 + 8910⋅40902 (mod 40902)
      ≡ − 495⋅7378 (mod 40902)
      ≡ 3556 (mod 40902)

Portanto, 3556 é o inverso multiplicativo de 24140 (mod 40902). Isso é verificado multiplicando 24140⋅3556 e observando se o resultado é congruente a 1 (mod 40902):
24140⋅3556 ≡ 1 (mod 40902)
Calculando isso, obtemos:
85913704≡1 (mod 40902)
Assim, 3556 é o inverso multiplicativo de 24140 (mod 40902).

**(c) 550 mod 1769.**

**7. Determine o inverso multiplicativo de x³ + x + 1 em GF(2^4), com m(x) = x^4 + x + 1.**

Tem que encontrar o inverso multiplicativo do elemento 3 + x + 1. Para isso, tem que encontrar um polinômio a(x) que, quando multiplicado pelo elemento 3 + x + 1, resulte em 1 no campo finito GF(2^4).

1. Se estabelece a identidade como o polinômio 1 (ou seja, a(x) = 1) e o elemento que desejamos inverter como 3 + x + 1.

2. Se aplica o algoritmo de Euclides estendido para polinômios para encontrar o MDC entre o polinômio 3 + x + 1 e o polinômio m(x) = x^4 + x + 1.

3. O MDC obtido será o polinômio a(x) que procuramos.

Aplicando o algoritmo:

Passo 1:
m(x) = x^4 + x + 1
f(x) = 3 + x + 1

Passo 2:
Se aplica o algoritmo de Euclides estendido, dividindo m(x) por f(x):

m(x) = (3 + x + 1)(x^3 + x^2 + 1) + (x^3 + x^2 + 1)

Passo 3:
Se troca polinômios e continua o processo:

f(x) = (x^3 + x^2 + 1)(x + 1) + (x^2)

Passo 4:
Repitir o processo:

(x^3 + x^2 + 1) = (x^2)(x + 1) + (x + 1)

Passo 5:
Repitir o processo:

(x^2) = (x + 1)(x) + 1

Passo 6:
Finalmente:

(x + 1) = (x)(1) + 1

Agora, o MDC encontrado é 1, o que significa que o inverso multiplicativo de 3 + x + 1 em GF(2^4) é 1. Portanto, (3 + x + 1)^(-1) ≡ 1 no campo finito GF(2^4).

**8. Para a aritmética de polinômios com coeficientes em Z10, realize os seguintes cálculos:**

**(a) (7x + 2) − (x² + 5)**

Primeiro, se subtrai o segundo polinômio do primeiro polinômio termo a termo:

(7x + 2) - (x^2 + 5) = 7x + 2 - x^2 - 5

Em seguida, se combina termos semelhantes:

7x - x^2 + 2 - 5

Simplifica ainda mais:

- x^2 + 7x - 3

O resultado da subtração é -x^2 + 7x - 3.

**(b) (6x² + x + 3) × (5x² + 2)**

Se multiplicam esses dois polinômios termo a termo. Usando a distributiva:

(6x^2 + x + 3) × (5x^2 + 2) = 6x^2 × 5x^2 + 6x^2 × 2 + x × 5x^2 + x × 2 + 3 × 5x^2 + 3 × 2

Depois se realiza as multiplicações:

30x^4 + 12x^2 + 5x^3 + 2x + 15x^2 + 6

Agora, soma-se os termos semelhantes:

30x^4 + 5x^3 + 27x^2 + 2x + 6

Então, o resultado da multiplicação é 30x^4 + 5x^3 + 27x^2 + 2x + 6.