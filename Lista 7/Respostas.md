**1. Qual é a diferença entre aleatoriedades estatísticas e imprevisibilidade?**
   
Enquanto a aleatoriedade estatística está mais diretamente relacionada à variabilidade em dados estatísticos e à probabilidade, a imprevisibilidade é um termo mais amplo que abrange situações em que os resultados podem não ser conhecidos com antecedência, seja devido à aleatoriedade ou a outros fatores complexos. 

**2. Liste considerações de projeto importantes para uma cifra de fluxo.**
   
Uma cifra de fluxo pode ser construída com qualquer gerador de números pseudoaleatórios criptograficamente forte. Por exemplo:

- Geradores de congruência linear
- gerador blum blum shub
- prng com modos de operação de cifra de bloco
- ansi x9.17 prng
- nisT CTr_Drbg

**3. Por que não é desejável reutilizar uma chave de cifra de fluxo?**

se dois textos claros forem encriptados com a mesma chave usando uma cifra de fluxo, então a criptoanálise normalmente é muito simples e a criptografia será quebrada facilmente. Se os dois fluxos de texto cifrado passaram por uma operação XOR, o resultado é o XOR dos textos claros originais.

**4. Que operações primitivas são usadas no RC4?**

1. Inicialização do vetor S:
   - No RC4, há um vetor S (state) que é inicializado de forma específica com base na chave. Isso envolve trocar os valores de dois elementos no vetor S.

2. Troca (Swap) de elementos do vetor S:
   - A atualização do vetor S envolve iterativamente percorrer o vetor S e realizar trocas de elementos com base nos bytes da chave. Isso é feito para criar uma mistura complexa no vetor S, tornando o algoritmo resistente a certos tipos de ataques.

2. Geração de Fluxo Pseudoaletório:
   - O RC4 gera um fluxo pseudoaleatório de bytes que é combinado com o texto claro usando a operação XOR. A geração desse fluxo é realizada por meio da manipulação do vetor S.

3. Operação XOR:
   - A operação de OU exclusivo (XOR) é usada para combinar o fluxo pseudoaleatório gerado pelo RC4 com o texto claro. Cada byte do texto claro é combinado com o byte correspondente do fluxo usando a operação XOR, resultando no texto cifrado.

O algoritmo começa com a inicialização do vetor S com base na chave fornecida e, em seguida, gera um fluxo pseudoaleatório usando as operações de troca, atualização do vetor S e XOR. Esse fluxo é combinado com o texto claro para produzir o texto cifrado. 

**5. Se apanharmos um algoritmo de congruência linear com um componente aditivo de 0:**

**Xn+1 = (aXn) mod m**

**então, podemos mostrar que, se m é primo, e se determinado valor de a produz o período máximo de m − 1, então a^k também produzirá o período máximo, desde que k seja menor que m e que m − 1 não seja divisível por k. Demonstre isso usando X0 = 1 e m = 31, e produzindo as sequências para ak = 3, 3^2, 3^3 e 3^4.**

Neste caso, X0 = 1, a = 3, e m = 31. Primeiro se calcula as sequências para a^k com k = 1, 2, 3, 4 e verificar se elas produzem o período máximo.

a^1 = 3^1 = 3
a^2 = 3^2 = 9
a^3 = 3^3 = 27
a^4 = 3^4 = 81

Agora, se aplica o algoritmo de congruência linear para cada valor de a^k e observaremos a sequência gerada:

1. Para k = 1:
    X1 = (3x1) mod 31 = 3

   A sequência é: 1 -> 3 -> 9 -> 27 -> 19 -> 5 -> 15 -> 7 -> 21 -> 1

2. Para k = 2:
    X1 = (3x1) mod 31 = 3
    X2 = (3x3) mod 31 = 9

   A sequência é: 1 -> 3 -> 9 -> 27 -> 19 -> 5 -> 15 -> 7 -> 21 -> 1

3. Para k = 3:
    X1 = (3x1) mod 31 = 3
    X2 = (3x3) mod 31 = 9
    X3 = (3x9) mod 31 = 27
    
   A sequência é: 1 -> 3 -> 9 -> 27 -> 19 -> 5 -> 15 -> 7 -> 21 -> 1

4. Para k = 4:
    X1 = (3x1) mod 31 = 3
    X2 = (3x3) mod 31 = 9
    X3 = (3x9) mod 31 = 27
    x4 = (3x27) mod 31 = 27
    
   A sequência é: 1 -> 3 -> 9 -> 27 -> 19 -> 5 -> 15 -> 7 -> 21 -> 1

Observamos que, para todos os valores de **a^k**, a sequência produz um ciclo que retorna ao estado inicial após alguns elementos. Isso é consistente com a afirmação de que, se m é primo e a produz o período máximo de **m-1**, então **a^k** também produzirá o período máximo, desde que **k** seja menor que **m** e **m-1** não seja divisível por **k**. Neste caso, **m-1 = 30**, e **k = 4** não é divisível por **30**, portanto, **a^4** produz o período máximo.

**6. (a) Qual é o período máximo que pode ser obtido do seguinte gerador?**
   
**Xn+1 = (aXn) mod 2^4**

O período máximo depende do valor de **a** e da escolha inicial de **X0**. O período máximo será alcançado quando o gerador entrar em um ciclo e começar a repetir sequências.

No caso específico em que **m = 2^4 = 16**, o período máximo possível para um gerador linear congruente é **m** se e somente se:

1. **X0** e **a** são primos entre si.
2. **a - 1** é divisível por todos os fatores primos de **m**.
3. **a - 1** é um múltiplo de 4 se **m** também é um múltiplo de 4.

Para **m = 16**, os fatores primos são **2** e **4**, e **a - 1** deve ser divisível por **2** e **4**.

Então, se escolhermos **a = 5** (que é primo entre si com **16**) e **X0** tal que **X0 mod 4 =! 0** (para garantir que **a - 1** não é múltiplo de 4), então o período máximo será **16**.

Por exemplo, com **X0 = 3**, a sequência seria:

**3, 15, 11, 13, 5, 7, 9, 1, 3, ...**

E ela se repetirá após 16 termos. Se **X0** fosse escolhido de forma diferente, o período máximo ainda seria **16** desde que os critérios mencionados anteriormente fossem atendidos.

**(b) Qual deverá ser o valor de a?**

Primeiro, precisamos garantir que **a** atenda aos critérios mencionados anteriormente:

Para **m = 16**, os fatores primos são **2** e **4**. Além disso, **m** é um múltiplo de 4.

Uma escolha comum para **a** que atende a esses critérios é **a = 5**. Vamos verificar:

1. **X0 = 1** e **a = 5** são primos entre si (não têm fatores primos comuns).
2. **5 - 1 = 4** é divisível por **2** e **4**.
3. **5 - 1 = 4** é um múltiplo de 4.

Assim, **a = 5** é uma escolha adequada que resultará no período máximo para o gerador linear congruente especificado.

**(c) Que restrições são exigidas na semente?**

1. **Coprimalidade com m:** A semente **X0** deve ser coprima com o módulo **m**. Isso significa que **X0** e **m** não devem ter fatores primos em comum, exceto 1. Por exemplo, se **m = 16**, então **X0** não deve ser divisível por 2.

2. **Não pode ser zero:** A semente **X0** não pode ser igual a zero, a menos que o multiplicador **a** seja escolhido de uma forma específica. Se **X0** for zero e **a** for um múltiplo de 2, o gerador ficará preso em um ciclo curto.

3. **Escolha que não gera um ciclo curto:** A semente **X0** deve ser escolhida de modo a não gerar um ciclo curto, o que pode ocorrer se **X0** for zero ou se **X0** for um múltiplo de **m**.

Um exemplo comum é escolher **X0** como um número ímpar (garantindo coprimalidade com **m**) que não seja um múltiplo de **m**.

Dado que **m = 16** no seu caso, um exemplo adequado pode ser escolher **X0 = 1** ou **X0 = 3** (números ímpares que são coprimos com **m**). Esse valor específico dependerá da escolha do multiplicador **a** para garantir a coprimalidade. Se **a = 5**, então **X0 = 1** pode ser uma escolha apropriada.

**7. Que valor de chave RC4 deixará S inalterado durante a inicialização? Ou seja, após a permutação inicial de S, as entradas de S serão quais aos valores de 0 a 255 na ordem crescente.**

O valor da chave RC4 que deixa o vetor de estado **S** inalterado durante a inicialização é uma chave onde cada byte da chave é igual ao seu índice correspondente no vetor **S** antes da permutação inicial.

Para ser mais específico, se a chave tiver comprimento **N** (onde **N** é o tamanho do vetor **S**, que é comumente **256** bytes), e a chave for composta pelos valores **0, 1, 2, ..., N-1** em ordem, então, após a permutação inicial, o vetor **S** será igual a **0, 1, 2, ..., N-1** na ordem crescente.

Por exemplo, para um vetor **S** de tamanho **256**, a chave *80, 1, 2, ..., 255*8 produzirá um vetor **S** que, após a permutação inicial, será **0, 1, 2, ..., 255** na ordem crescente.

**8. O algoritmo Blum Blum Shub é baseado na teoria dos resíduos quadráticos e utiliza três números inteiros para realizar os cálculos: p, q e s.**

**(a) Escolha dois números primos grandes p e q, onde p e q sejam congruentes a 3 mod 4 e não tenham fatores primos comuns. Por exemplo, você pode escolher p = 499 e q = 503.**

p = 499  e q = 503

**(b) Calcule n = p ∗ q. Neste caso, n seria igual a 499 ∗ 503 = 250997.**

n = 499x503 = 250997

**(c) Escolha um número inteiro s entre 1 e n − 1 que seja co-primo com n. Por exemplo, você pode escolher s = 17.**

s = 17

**(d) Calcule o valor inicial x0 = (s^2) mod n. Neste caso, x0 seria igual a (17^2) mod 250997 = 289.**

X0 = (17^2) mod5 250997 = 289

**(e) Agora, vamos gerar uma sequência de números aleatórios usando o algoritmo Blum Blum Shub. Para gerar cada número da sequência, use a seguinte fórmula:**
**xi = (xi−1^2) mod n.**

X1 = (289^2) mod 250997

X2 = (253306^2) mod 250997

X3 = (14107^2) mod 250997

X4 = (23546^2) mod 250997

X5 = (67740^2) mod 250997

X6 = (144593^2) mod 250997

X7 = (79829^2) mod 250997

X8 = (46219^2) mod 250997

X9 = (132936^2) mod 250997

**(f) Execute a fórmula várias vezes para gerar uma sequência de números aleatórios. Por exemplo, você pode executar a fórmula 10 vezes para obter 10 números aleatórios.**

X1 = (289^2) mod 250997 = 253306

X2 = (253306^2) mod 250997 = 14107

X3 = (14107^2) mod 250997 = 23546

X4 = (23546^2) mod 250997 = 67740

X5 = (67740^2) mod 250997 = 144593

X6 = (144593^2) mod 250997 = 79829

X7 = (79829^2) mod 250997 = 46219

X8 = (46219^2) mod 250997 = 132936

X9 = (132936^2) mod 250997 = 9863 

A sequência gerada é: 289, 253306, 14107, 23546, 67740, 144593, 79829, 46219, 132936, 9863.

**Aqui está a sequência de números aleatórios gerados usando o algoritmo Blum Blum Shub com os valores do exemplo:**

**289, 253306, 14107, 23546, 67740, 144593, 79829, 46219, 132936, 9863**

**Qual foi a sua sequência?**

A mesma sequência