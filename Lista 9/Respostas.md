Vamos abordar cada uma das questões passo a passo:

### 1. Quais são os principais elementos de um criptossistema de chave pública?

Um criptossistema de chave pública, também conhecido como criptografia assimétrica, envolve principalmente os seguintes elementos:

- **Chave Pública**: Uma chave que pode ser compartilhada livremente e é usada para criptografar mensagens.
- **Chave Privada**: Uma chave mantida em segredo pelo proprietário e usada para descriptografar mensagens.
- **Algoritmos de Criptografia e Descriptografia**: Métodos matemáticos utilizados para transformar a mensagem em uma forma criptografada e voltar para a forma legível, respectivamente.
- **Mensagens**: Informações que precisam ser protegidas durante a transmissão.
- **Infraestrutura de Chave Pública (PKI)**: Um conjunto de roles, políticas e procedimentos necessários para criar, gerenciar, distribuir, usar, armazenar e revogar chaves digitais.

### 2. Quais são os papéis da chave pública e da privada? Descreva-os com detalhes e com exemplos.

- **Chave Pública**: Usada para criptografar mensagens. Por exemplo, se Alice quer enviar uma mensagem segura para Bob, ela usará a chave pública de Bob para criptografar a mensagem. Qualquer um pode ter acesso à chave pública de Bob e usá-la para enviar mensagens a ele, mas apenas Bob pode descriptografá-las.
  
- **Chave Privada**: Usada para descriptografar mensagens. Continuando o exemplo, somente Bob, que possui a chave privada correspondente, pode descriptografar a mensagem criptografada com sua chave pública. A chave privada nunca deve ser compartilhada.

### 3. Quais requisitos os criptossistemas de chave pública precisam cumprir para serem considerados como um algoritmo seguro?

Para ser considerado seguro, um criptossistema de chave pública deve satisfazer vários requisitos:

- **Complexidade Computacional**: Deve ser computacionalmente inviável para um atacante recuperar a chave privada a partir da chave pública.
- **Funções Trapdoor**: O sistema deve usar funções matemáticas que são fáceis de computar em uma direção, mas difíceis de reverter sem informação adicional (a chave privada).
- **Resistência a Ataques**: O sistema deve ser resistente a ataques conhecidos, como ataques de força bruta, ataques de texto claro escolhido, entre outros.
- **Gerenciamento de Chaves Robusto**: Deve haver um método seguro de geração, distribuição e armazenamento de chaves.

### 4. Descreva, em termos gerais, um procedimento eficiente para se escolher um número primo.

Para escolher um número primo eficientemente, pode-se usar o seguinte procedimento:

- **Teste de Primalidade**: Use um teste de primalidade como o Teste de Miller-Rabin que é probabilístico, ou o Teste de Primalidade AKS que é determinístico.
- **Seleção Aleatória**: Escolha um número aleatório dentro do intervalo desejado e aplique o teste de primalidade.
- **Iteração**: Se o número não for primo, selecione outro número aleatoriamente e repita o teste até que um número primo seja encontrado.

### 5. PAntes da descoberta de quaisquer esquemas de chave pública específicas, como RSA, uma prova de existência foi desenvolvida, cuja finalidade era demonstrar que a encriptação de chave pública é possível em teoria. Considere as funções f1(x1) = z1; f2(x2, y2) = z2; f3(x3, y3) = z3, onde todos os valores são inteiros com 1 ≤ xi, yi, zi ≤ N. A função f1, pode ser representada por um vetor M1 de tamanho N, em que a k-ésima entrada é o valor de f1(k). De modo semelhante, f2 e f3 podem ser representados pelas matrizes M2 e M3 de tamanho N × N. A intenção é indicar o processo de encriptação/decriptação por pesquisas de tabela para aquelas com valores muito grandes de N. Essas tabelas seriam impraticavelmente grandes, mas, a princípio, poderiam ser construídas. O esquema funciona da seguinte forma: construa M1 com uma permutação aleatória de todos os inteiros entre 1 e N; ou seja, cada inteiro aparece exatamente uma vez em M1. Construa M2, de modo que cada linha contenha uma permutação aleatória dos primeiros N inteiros. Finalmente, preencha M3 para satisfazer a seguinte condição:

#### f3(f2(f1(k), p), k) = p para todo k, p com 1 ≤ k, p ≤ N

### Resumindo,
#### 1. M1 toma uma entrada k e produz uma saída x.
#### 2. M2 toma as entradas x e p, dando a saída z.
#### 3. M3 toma as entradas z e k e produz p.

### As três tabelas, uma vez construídas, se tornam públicas.
##### a) Deverá ficar claro que é possível construir M3 para satisfazer a condição anterior. Como um exemplo, preencha M3 para o caso simples a seguir:

###### Convenção: o i-ésimo elemento de M1 corresponde a k = i. A i-ésima linha de M2 diz respeito ax = i; a j-ésima coluna de M2 equivale a p = j. A i-ésima linha de M3 indica z = i; a j-ésima coluna de MB relaciona-se a k = j.

#### a) Descreva o uso desse conjunto de tabelas para realizar a encriptação e decriptação entre dois usuários.

- **Encriptação**: Para criptografar uma mensagem `p` com a chave `k`, o remetente encontra `x` usando `M1` (com `k` como índice), depois encontra `z` usando `M2` (com `x` como índice da linha e `p` como índice da coluna), e envia `z` ao destinatário.
  
- **Decriptação**: O destinatário recebe `z` e, conhecendo `k`, usa `M3` para encontrar `p` (com `z` como índice da linha e `k` como índice da coluna), recuperando assim a mensagem original.

#### b) Demonstre que esse é um esquema seguro

Para demonstrar a segurança, seria necessário mostrar que, sem o conhecimento da chave privada (neste caso, o método de construção de `M3`), seria impraticável para um atacante recuperar `p` de `z`. No entanto, a segurança deste esquema simplificado não é comparável à dos algoritmos de criptografia de chave pública reais e não deve ser considerada segura para uso prático.

### 6. Realize a encriptação e decriptação usando o algoritmo RSA, como na Figura 9.5, para o seguinte:

#### (a) p = 3; q = 11, e = 7; M = 5

**Criptografia**:
1. n = p * q = 3 * 11 = 33
2. φ(n) = (p - 1) * (q - 1) = 2 * 10 = 20
3. e = 7 (dado que é coprimo com φ(n))
4. C = M^e mod n = 5^7 mod 33

Usando a exponenciação rápida, temos C = 78125 mod 33 = 14 (o resultado da criptografia).

**Descriptografia**:
1. Calcule d tal que e * d mod φ(n) = 1. Pode-se encontrar que d = 3, pois 7 * 3 = 21, e 21 mod 20 = 1.
2. Descriptografe o texto C = 14 com M = C^d mod n = 14^3 mod 33

Novamente, usando a exponenciação rápida, M = 2744 mod 33 = 5 (o resultado da descriptografia).

#### (b) p = 5; q = 11, e = 3; M = 9

**Criptografia**:
1. n = p * q = 5 * 11 = 55
2. φ(n) = (p - 1) * (q - 1) = 4 * 10 = 40
3. e = 3
4. C = M^e mod n = 9^3 mod 55 = 729 mod 55 = 14

**Descriptografia**:
1. d tal que e * d mod φ(n) = 1. Encontramos que d = 27, pois 3 * 27 = 81, e 81 mod 40 = 1.
2. M = C^d mod n = 14^27 mod 55

#### (c) p = 7; q = 11, e = 17; M = 8

**Criptografia**:
1. n = p * q = 7 * 11 = 77
2. φ(n) = (p - 1) * (q - 1) = 6 * 10 = 60
3. e = 17
4. C = M^e mod n = 8^17 mod 77

**Descriptografia**:
1. d = 53, pois 17 * 53 = 901, e 901 mod 60 = 1.
2. M = C^d mod n = C^53 mod 77

#### (d) p = 11; q = 13, e = 11; M = 7

**Criptografia**:
1. n = p * q = 11 * 13 = 143
2. φ(n) = (p - 1) * (q - 1) = 10 * 12 = 120
3. e = 11
4. C = M^e mod n = 7^11 mod 143

**Descriptografia**:
1. d = 11, pois e = 11 é um número primo, e escolhendo d = e, temos que e * d mod φ(n) = 1.
2. M = C^d mod n = C^11 mod 143

#### (e) p = 17; q = 31, e = 7; M = 2

**Criptografia**:
1. n = p * q = 17 * 31 = 527
2. φ(n) = (p - 1) * (q - 1) = 16 * 30 = 480
3. e = 7
4. C = M^e mod n = 2^7 mod 527 = 128 mod 527 = 128

**Descriptografia**:
1. d = 343, pois 7 * 343 = 2401, e 2401 mod 480 = 1.
2. M = C^d mod n = 128^343 mod 527

### 7. Em um sistema de chave pública usando RSA, você intercepta o texto cifrado C = 10 enviado a um usuário cuja chave pública é e = 5, n = 35. Qual é o texto claro M?

M ≡ C^d (mod n)

Onde d é o inverso multiplicativo de e módulo φ(n). Para o RSA, como escolhemos p e q como primos distintos, a função totiente de Euler φ(n) é dada por φ(n) = (p-1) * (q-1).

Se n = 35, então é o produto de p = 5 e q = 7. Assim, podemos calcular φ(n) = (7-1) * (5-1) = 6 * 4 = 24. Agora, precisamos encontrar o inverso multiplicativo de e = 5 módulo 24.

5 * d ≡ 1 (mod 24)

Calculando o inverso multiplicativo de 5 módulo 24, obtemos d = 5, pois 5 * 5 ≡ 1 (mod 24).

Agora podemos descriptografar o texto cifrado C = 10:

M ≡ 10^5 (mod 35)

Calculando 10^5 (mod 35), obtemos M = 25.