**1. Qual foi o conjunto original de critérios usados pelo NIST para avaliar as cifras AES candidatas?**

Os critérios originais incluíam:

1. Segurança Criptográfica: A cifra deve resistir a todos os ataques conhecidos, e a sua estrutura deve ser bem fundamentada criptograficamente.

2. Desempenho: A cifra deve ser eficiente em termos de velocidade e uso de recursos computacionais.

3. Facilidade de Implementação: A cifra deve ser implementável em uma variedade de ambientes e plataformas.

4. Adoção Internacional: A cifra deve ser adequada para uso em sistemas de informação governamentais e não governamentais em todo o mundo.

5. Algoritmo Público: A cifra deve ser publicada e estar disponível para análise pública.

6. Propriedade Intelectual: A cifra não deve estar sujeita a restrições de patentes que impeçam sua adoção ou implementação sem a necessidade de pagamento de royalties.

7. Segurança em Larga Escala: A cifra deve ser segura em uma ampla variedade de ambientes e aplicações.

8. Avaliação Formal: Os candidatos seriam submetidos a uma avaliação formal conduzida por especialistas em criptografia.


**2. Qual foi o conjunto final de critérios usados pelo NIST para avaliar as cifras AES candidatas?**

Os critérios finais para a escolha do AES incluíram:

1. Segurança Criptográfica: A cifra deve resistir a todos os ataques conhecidos e demonstrar uma segurança robusta.

2. Desempenho Computacional: A cifra deve ter um desempenho eficiente em uma variedade de ambientes e plataformas.

3. Facilidade de Implementação e Uso: A cifra deve ser implementável e utilizável em uma variedade de aplicativos e ambientes.

4. Adoção Internacional: A cifra deve ser adequada para uso em sistemas de informação governamentais e não governamentais em todo o mundo.

5. Flexibilidade: A cifra deve ser aplicável em uma variedade de aplicações e ambientes de segurança.

6. Confiabilidade: A cifra deve ser confiável em diferentes contextos e ao longo do tempo.

7. Capacidade de Avaliação e Teste: Deve ser possível avaliar e testar a cifra de maneira eficaz.

8. Capacidade de Implementação Independente: A cifra não deve depender fortemente de componentes específicos de implementação, como tabelas de pré-computação.

**3. Qual é a diferença entre Rijndael e AES?**
   
Rijndael é um algoritmo de cifragem simétrica desenvolvido pelos criptógrafos belgas Vincent Rijmen e Joan Daemen. Foi originalmente proposto como candidato para o Padrão de Criptografia Avançada (AES) durante o processo de seleção do NIST. Rijndael suporta blocos e chaves de tamanhos variados, e durante o processo de seleção, o NIST escolheu uma variação específica do Rijndael para ser o AES.

AES, por sua vez, refere-se ao padrão de cifragem simétrica que foi adotado pelo NIST em 2001. O algoritmo escolhido para ser o AES é, na verdade, uma instância específica do Rijndael com um tamanho de bloco de 128 bits e tamanhos de chave de 128, 192 ou 256 bits. Portanto, enquanto Rijndael é o algoritmo subjacente, AES se refere à sua implementação específica conforme padronizada pelo NIST.

Rijndael é o algoritmo criptográfico desenvolvido pelos criptógrafos belgas, enquanto AES é o padrão que adotou uma configuração específica do Rijndael como a cifra simétrica padrão.

**4. Responda:**

**(a) Qual é a finalidade do array Estado?**

O array Estado, no contexto do AES (Advanced Encryption Standard), é uma matriz bidimensional que armazena os dados durante as operações de cifragem e decifragem. O Estado é composto por blocos de 4x4 bytes (16 bytes no total). Cada elemento do Estado representa um byte de dados. As operações criptográficas do AES são realizadas nas colunas do Estado, e a manipulação dos dados ocorre nessa estrutura.

**(b) Como é construída a S-box?**

A S-box (Substitution Box) é uma tabela de substituição não linear usada pelo AES. Ela é construída aplicando transformações matemáticas específicas aos elementos do corpo finito GF(2^8). A construção envolve operações como inversão multiplicativa, substituições afins e permutações. A S-box é usada na etapa SubBytes durante a cifragem e decifragem para fornecer não linearidade às operações.

**(c) Descreva rapidamente o estágio SubBytes, ShiftRows, MixColumns, AddRoundKey, e o algoritmo de expansão de chave.**

SubBytes: Nesta etapa, cada byte do Estado é substituído por um valor correspondente da S-box. Isso introduz não linearidade na transformação.

ShiftRows: Os bytes nas linhas do Estado são deslocados circularmente. Isso proporciona difusão e confusão nos dados.

MixColumns: Nesta fase, cada coluna do Estado é multiplicada por uma matriz fixa, proporcionando uma operação de mistura. Isso ajuda a espalhar a informação por todo o bloco de dados.

AddRoundKey: Cada byte do Estado é combinado com um byte da chave daquela rodada por meio de uma operação de OU exclusivo (XOR). Isso adiciona a chave de rodada atual ao Estado.

Algoritmo de Expansão de Chave: A chave original é expandida em um conjunto de chaves de rodadas usando o algoritmo de expansão de chave. Isso envolve a geração de novas palavras-chave com base na chave original, utilizando operações como rotações e substituições.

**5. Quantos bytes em Estado são afetados por ShiftRows?**

O ShiftRows afeta todos os bytes no array Estado, mas o deslocamento é realizado de maneira diferente em cada linha. O ShiftRows opera nas linhas da matriz Estado da seguinte maneira:

- Na primeira linha, nenhum deslocamento é feito (0 bytes deslocados).
- Na segunda linha, os bytes são deslocados circularmente para a esquerda em 1 posição.
- Na terceira linha, os bytes são deslocados circularmente para a esquerda em 2 posições.
- Na quarta linha, os bytes são deslocados circularmente para a esquerda em 3 posições.

Dessa forma, enquanto todos os bytes são afetados, o número de posições deslocadas varia para cada linha.

**6. Use a chave 1010 0111 0011 1011 para encriptar o texto claro "ok"conforme expresso em ASCII, ou seja, 0110 1111 0110 1011. Os projetistas do S-AES obtiveram o texto cifrado 0000 0111 0011 1000. E você?**

Expansão de Chave:

W0 = 1010 0111
W1 = 0011 1011
W2 = 0001 1100
W3 = 0010 0111
W4 = 0111 0110
W5 = 0101 0001

Round 0:
After Add round key: 1100 1000 0101 0000

Round 1:
Após Substituição de Nibbles: 1100 0110 0001 1001
Após Shift rows: 1100 1001 0001 0110
Após Mix columns: 1110 1100 1010 0010
Após Add round key: 1110 1100 1010 0010

Round 2:
Após Substituição de Nibbles: 1111 0000 1000 0101
Após Shift rows: 0111 0001 0110 1001
Após Add round key: 0000 0111 0011 1000

**7. Compare AES com DES. Para cada um dos seguintes elementos do DES, indique o elemento comparável no AES ou explique por que ele não é necessário no AES.**

**(a) XOR do material da subchave com a entrada da função f.**

No AES, a operação de combinação com a chave é realizada diretamente por meio da etapa AddRoundKey, onde cada byte do Estado é combinado com um byte correspondente da chave de rodada utilizando uma operação XOR.

Em resumo, embora existam algumas semelhanças nas operações básicas de difusão e confusão, as implementações específicas dessas operações são diferentes entre o DES e o AES. O AES é mais avançado e eficaz em termos de segurança, especialmente em relação ao tamanho da chave e à complexidade das operações.

**(b) XOR da saída da função f com a metade esquerda do bloco.**

No AES, não há uma operação exatamente equivalente a esta. A etapa que mais se assemelha é a AddRoundKey, onde a saída da função MixColumns é combinada com a chave de rodada.

**(c) função f.**

A função f no DES envolve uma série de operações, incluindo expansão, permutações e substituições. No AES, as funções SubBytes, ShiftRows, MixColumns e AddRoundKey fornecem funções semelhantes, proporcionando confusão, difusão e combinação com a chave.

**(d) permutação P.**

Não há uma permutação exata equivalente à P do DES no AES. No AES, a difusão e a confusão são obtidas principalmente por meio das etapas SubBytes, ShiftRows e MixColumns.

**(e) troca de metades do bloco.**

No AES, não há uma etapa específica de troca de metades do bloco, como ocorre no DES. A difusão e a confusão nos dados são obtidas por meio das etapas SubBytes, ShiftRows e MixColumns.

**8. (1 ponto-extra) Calcule a saída da transformação MixColumns para a seguinte sequência de bytes de entrada "67 89 AB CD". Aplique a transformação InvMixColumns ao resultado obtido para verificar seus cálculos. Altere o primeiro byte da entrada de "67"para "77", realize a transformação MixColumns novamente para a nova entrada e determine quantos bits mudaram na saída.**

Nota: você pode realizar todos os cálculos à mão ou escrever um programa que dê suporte a eles. Se escolher escrever um programa, ele deverá ser feito inteiramente por você; nesta tarefa, não use bibliotecas ou código fonte de domínio público (você pode se guiar pelos exemplos Sage disponibilizados).

Na operação MixColumns, cada byte de uma coluna é gerado como um novo valor somando todos os quatro bytes dessa coluna.

Portanto, para a operação MixColumns,

entrada = 67 89 AB CD

[2 3 1 1] * [67] = [67*2 + 89*3 + AB + CD] = [CE + 80 + AB + CD] = [28]
[1 2 3 1]   [89]   [67 + 89*2 + AB*3 + CD]   [67 + 09 + E6 + CD]   [45]
[1 1 2 3]   [AB]   [67 + 89 + AB*2 + CD*3]   [67 + 89 + 4D + 4C]   [EF]
[3 1 1 2]   [CD]   [67*3 + 89 + AB + CD*2]   [A9 + 89 + AB + 81]   [0A]

Verificação com a inverse mix column matrix nos dá:

[E B D 9] * [28] = [28*E + 45*B + EF*D + 0A*9] = [AB + DI + 47 + 5A] = [67]
[9 E B D]   [45]   [28*9 + 45*E + EF*B + 0A*D]   [73 + 9B + 13 + 72]   [89]
[D 9 E B]   [EF]   [28*D + 45*9 + EF*E + 0A*B]   [D3 + 5B + 6D + 4E]   [AB]
[B D 9 E]   [0A]   [28*B + 45*D + EF*9 + 0A*E]   [23 + 54 + D6 + 6C]   [CD]

Agora, alterando o primeiro bit na entrada, portanto,

entrada = 77 89 AB CD

[2 3 1 1] * [77] = [77*2 + 89*3 + AB + CD] = [EE + 80 + AB + CD] = [08]
[1 2 3 1]   [89]   [77 + 89*2 + AB*3 + CD]   [77 + 09 + E6 + CD]   [55]
[1 1 2 3]   [AB]   [77 + 89 + AB*2 + CD*3]   [77 + 89 + 4D + 4C]   [FF]
[3 1 1 2]   [CD]   [77*3 + 89 + AB + CD*2]   [C7 + 89 + AB + 81]   [3A]

O número de bits alterados na saída é 5, quando o primeiro bit é alterado na entrada.