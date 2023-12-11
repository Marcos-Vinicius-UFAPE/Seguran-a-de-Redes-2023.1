**1. Para cada um dos seguintes recursos, determine um nível de impacto baixo, moderado ou alto à perda de confidencialidade, disponibilidade e integridade, respectivamente. Justifique suas respostas.**
   
**(a) uma organização gerenciando informações públicas em seu servidor web.**

O impacto à confidencialidade é baixo, pois as informações já são públicas e acessíveis.
A disponibilidade é moderada, pois a interrupção do servidor pode afetar o acesso às informações.
A integridade também é moderada, pois a alteração não autorizada das informações pode afetar a confiança do público na organização.

**(b) uma organização de aplicação da lei gerindo informações de investigação extremamente sensíveis.**

O impacto à confidencialidade é alto, pois a divulgação dessas informações pode comprometer casos em andamento e colocar vidas em risco.
A disponibilidade também é alta, pois qualquer interrupção no acesso a essas informações pode prejudicar investigações em andamento.
A integridade também é alta, pois a manipulação não autorizada das informações pode afetar a validade das evidências e a justiça dos casos.

**(c) uma organização financeira gerindo informações administrativas rotineiras (sem informações relacionadas à privacidade).**

O impacto à confidencialidade é baixo, pois as informações não são sensíveis.
A disponibilidade é moderada, pois qualquer interrupção no acesso a essas informações pode afetar as operações administrativas.
A integridade também é moderada, pois a manipulação não autorizada das informações pode afetar a precisão dos registros financeiros.

**(d) um sistema de informação utilizado para grandes aquisições em uma organização voltada a contratações que contém dados sensíveis da fase de pré-solicitação e dados administrativos rotineiros. avalie o impacto de haver dois conjuntos de dados separadamente e o sistema de informação único.**

O impacto à confidencialidade é moderado para os dados administrativos rotineiros, pois essas informações geralmente não são altamente sensíveis ou sigilosas. E é alto para os dados sensíveis da fase de pré-solicitação porque esses dados são considerados críticos e confidenciais para o processo de aquisição da organização.
A disponibilidade é moderada, pois a interrupção do sistema pode afetar as operações de aquisição.
A integridade é moderada para os dados administrativos rotineiros e alta para os dados sensíveis, pois a manipulação não autorizada dessas informações pode afetar tanto a precisão dos registros administrativos quanto a integridade do processo de aquisição.

**(e) uma indústria de energia contém um sistema SCada (controle supervisório e aquisição de dados, do acrônimo em inglês para supervisory control and data acquisition) controlando a distribuição da energia elétrica para uma grande instalação militar. o sistema SCada contém tanto sensores de dados em tempo real quanto informações das rotinas administrativas. avalie o impacto de haver dois conjuntos de dados separadamente e o sistema de informação único.**

O impacto à confidencialidade é moderado para as informações das rotinas administrativas, pois essas informações geralmente não são consideradas altamente sensíveis ou críticas para a organização. E é alto para os dados em tempo real, pois essas informações são críticas e confidenciais para o processo de aquisição da organização.
A disponibilidade é alta, pois qualquer interrupção no sistema pode afetar a distribuição de energia na instalação militar.
A integridade é alta tanto para os dados em tempo real quanto para as informações administrativas, pois a manipulação não autorizada dessas informações pode afetar a segurança da instalação e a confiabilidade do sistema de energia.

**2. Responda, explique com exemplos, as questões abaixo:**

**(a) Quais são os elementos essenciais de uma cifra simétrica? Explique-as.**
Os elementos essenciais de uma cifra simétrica são:

   1. Chave: É um valor secreto ou compartilhado que é usado para criptografar e descriptografar os dados. A mesma chave é usada para ambos os processos.

   2. Algoritmo de Criptografia: É o conjunto de regras e operações matemáticas que são aplicadas aos dados para transformá-los em uma forma ilegível durante a criptografia e para revertê-la durante a descriptografia.

Exemplo: Um exemplo de cifra simétrica é o AES (Advanced Encryption Standard). Nesse caso, a chave é compartilhada entre o remetente e o destinatário, e o algoritmo AES é usado para criptografar e descriptografar os dados.

**(b) Quais são as duas funções básicas usadas nos algoritmos de encriptação? Explique-as.**

As duas funções básicas usadas nos algoritmos de criptografia são:

   1. Função de Criptografia: É usada para transformar os dados em uma forma ilegível durante o processo de criptografia.

   2. Função de Descriptografia: É usada para reverter o processo de criptografia e transformar os dados criptografados de volta à sua forma original legível durante o processo de descriptografia.

Exemplo: No algoritmo RSA, uma função de criptografia é usada para criptografar os dados usando a chave pública do destinatário, enquanto uma função de descriptografia é usada para descriptografar os dados usando a chave privada correspondente.

**(c) Quantas chaves são necessárias para duas pessoas se comunicarem por meio de uma cifra? Explique-as, demonstrando, você pode se utilizar de gráficos ou desenhos.**

Para que duas pessoas se comuniquem por meio de uma cifra, é necessária a utilização de duas chaves: uma chave para criptografar os dados na extremidade do remetente e outra chave para descriptografar os dados na extremidade do destinatário.

Exemplo gráfico:

![Grafico](https://i.imgur.com/fTtj1uP.png)

**(d) Quais são as duas técnicas gerais para atacar uma cifra? Explique-as.**

As duas técnicas gerais para atacar uma cifra são:

   1. Ataque de Força Bruta: Nesse tipo de ataque, o invasor tenta todas as combinações possíveis de chaves até encontrar a chave correta. É um método demorado e exige muita capacidade computacional.

   2. Ataque de Criptoanálise: Nesse tipo de ataque, o invasor procura por fraquezas no algoritmo de criptografia ou nas chaves utilizadas para tentar encontrar uma forma de descriptografar os dados sem conhecer a chave correta.

**(e) Defina resumidamente a cifra de César; a cifra de Hill; a cifra de Feistel (por que é importante estudá-la?); e, a diferença entre DES, Rijndael e AES.**

Definições resumidas:

   - Cifra de César: É um tipo de cifra de substituição em que cada letra do texto original é substituída por outra letra, deslocando um número fixo de posições no alfabeto.

   - Cifra de Hill: É um método de criptografia que utiliza matrizes para transformar blocos de caracteres em texto cifrado.

   - Cifra de Feistel: É uma estrutura de criptografia simétrica que divide o texto em blocos e aplica várias rodadas de substituição e permutação para produzir o texto cifrado.

   - Diferença entre DES, Rijndael e AES: O DES (Data Encryption Standard) é um algoritmo de criptografia simétrica que usa uma chave de 56 bits. Rijndael é um algoritmo de criptografia de bloco que pode ter diferentes tamanhos de chave e tamanho de bloco. AES (Advanced Encryption Standard) é uma versão específica do algoritmo Rijndael com tamanho de chave fixo de 128 bits e é amplamente utilizado como padrão de criptografia atualmente.

**3. Quando o barco de patrulha norte-americano PT-109, sob o comando do tenente John f. Kennedy, foi afundado por um destróier japonês, uma mensagem foi recebida na estação sem fio australiana em código playfair:**

**KXJEY UREBE ZWEHE WRYTU HEYFS**
**KREHE GOYFI WTTTU OLKSY CAJPO**
**BOTEI ZONTX BYBNT GONEY CUZWR**
**GDSON SXBOU YWRHE BAAHY USEDQ**

**a chave usada foi “royal new zealand navy”. decripte a mensagem. traduza TT para tt.**

1. Removemos os espaços da mensagem criptografada: KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ

2. Substimos "TT" por "tt" na mensagem criptografada para obter: KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWttTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ

3. Dividimos a mensagem criptografada em pares de letras: KX JE YU RE BE ZW EH EW RY TU HE YF SK RE HE GO YF IW tt TU OL KS YC AJ PO BO TE IZ ON TX BY BN TG ON EY CU ZW RG DS ON SX BO UY WR HE BA AH YU SE DQ

4. Usamos a tabela Playfair com a chave "royalnewzealandnavy" para descriptografar cada par de letras.

![Tabela](https://i.imgur.com/XrleCgD.png)

**KX JE YU RE BE ZW EH EW RY TU HE YF**
PT BO AT ON EO WE NI NE LO ST IN AC


**SK RE HE GO YF I W TX XT TU OL KS YC AJ PO**
TI ON IN BL AC KE TT ST RA IT TW OM IL


**BO TE IZ ON TX BY BN TG ON EY CU ZW RG**
ES SW ME RE SU CO VE XC RE WO FT WE LV


**DS ON SX BO UY WR HE BA AH YU SE DQ**
EX RE QU ES TA NY IN FO RM AT IO NX

Resultando na mensagem:
PT BOAT ONE OWE NINE LOST IN ACTION IN BLACKETT STRAIT TWO MILES SW MERESU COVE X CREW OF TWELVE X REQUEST ANY INFORMATION

traduzindo seria:
"PT-Boat 109 perdida em ação no Estreito de Blackett, a duas milhas a sudoeste da Enseada Meresu. Tripulação de doze pessoas. Solicito qualquer informação.”

**5. Responda, resumidamente, as questões a seguir:**

**(a) Qual é a diferença entre uma cifra de bloco e uma cifra de fluxo?**

Uma cifra em fluxo é uma cifra que processa os elementos da entrada (bytes, usualmente)
continuamente, produzindo a saída de um elemento d e cada vez, enquanto prossegue.

Uma cifra de bloco processa a entrada de um bloco de elementos (bytes) de cada vez, medido por sua quantidade de bits, produzindo um bloco de saída para cada bloco de entrada. O processamento por fluxo é mais rápido do que por bloco.

**(b) O que é uma cifra de produto?**

Uma cifra de produto é um tipo de cifra que combina dois ou mais elementos individuais para criar uma operação criptográfica mais complexa. Esses elementos podem ser subchaves, sub-blocos de dados ou funções criptográficas. O objetivo de uma cifra de produto é aumentar a segurança e a resistência a ataques, tornando a criptografia mais difícil de ser revertida sem a chave correta.

**(c) Qual é a diferença entre difusão e confusão? Explique.**

Difusão e confusão são duas técnicas criptográficas usadas para aumentar a segurança de um algoritmo de criptografia.
- Difusão: Garante que a influência de um bit de entrada seja espalhada por todo o texto cifrado. Isso ajuda a tornar o padrão de criptografia menos previsível e dificulta a extração de informações sobre a chave.
- Confusão: Torna a relação entre o texto cifrado e a chave tão complexa quanto possível. Ele garante que mesmo mudanças pequenas na chave ou no texto original resultem em mudanças significativas no texto cifrado.

**(d) Quais parâmetros e escolhas de projeto determinam o algoritmo real de uma cifra de Feistel?**

Os parâmetros e escolhas de projeto que determinam o algoritmo real de uma cifra de Feistel são:
- Número de rodadas: Determina quantas vezes a função de Feistel será aplicada.
- Tamanho dos blocos: Define o tamanho dos blocos de dados que serão manipulados.
- Chaves de sub-rodada: Define como as chaves serão geradas para cada rodada.
- Funções de transformação: Define as funções utilizadas para transformar os blocos de dados em cada rodada.

**(e) Explique o efeito avalanche.**

O efeito avalanche refere-se à propriedade desejável de uma cifra criptográfica, em que uma pequena alteração nos dados de entrada ou na chave deve resultar em uma grande mudança no texto cifrado. Em outras palavras, um único bit alterado no texto original ou na chave deve causar uma modificação significativa e imprevisível na saída cifrada. O efeito avalanche é importante para garantir que pequenas mudanças não permitam que um adversário extraia informações sobre a chave ou sobre o texto original.


**6. Encontre o inverso multiplicativo de cada elemento diferente de zero em Z5.**

**Em Z5, o conjunto de inteiros módulo 5, para encontrar o inverso multiplicativo de cada elemento diferente de zero (ou seja, encontrar o elemento que, quando multiplicado pelo elemento original, resulta em 1), se usa a seguinte regra:**

o inverso multiplicativo b de a é aquele número que satisfaz a * b ≡ 1 (mod 5).

1. Para a = 1, o inverso multiplicativo b é 1, porque 1 * 1 ≡ 1 (mod 5).

2. Para a = 2, o inverso multiplicativo b é 3, porque 2 * 3 ≡ 1 (mod 5).

3. Para a = 3, o inverso multiplicativo b é 2, porque 3 * 2 ≡ 1 (mod 5).

4. Para a = 4, o inverso multiplicativo b é 4, porque 4 * 4 ≡ 1 (mod 5).

**7. Para a aritmética de polinômios com coeficientes em Z10, realize os seguintes cálculos:**
   
(a) (7x + 2) − (x² + 5)**
**
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


**8. Use a chave 1010 0111 0011 1011 para encriptar o texto claro "ok"conforme expresso em ASCII, ou seja, 0110 1111 0110 1011. Os projetistas do S-AES obtiveram o texto cifrado 0000 0111 0011 1000. E você?**

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

**9. Compare AES com DES. Para cada um dos seguintes elementos do DES, indique o elemento comparável no AES ou explique por que ele não é necessário no AES.**

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

**10. Calcule a saída da transformação MixColumns para a seguinte sequência de bytes de entrada "67 89 AB CD". Aplique a transformação InvMixColumns ao resultado obtido para verificar seus cálculos. Altere o primeiro byte da entrada de "67"para "77", realize a transformação MixColumns novamente para a nova entrada e determine quantos bits mudaram na saída.**

**Nota: você pode realizar todos os cálculos à mão ou escrever um programa que dê suporte a eles. Se escolher escrever um programa, ele deverá ser feito inteiramente por você; nesta tarefa, não use bibliotecas ou código fonte de domínio público (você pode se guiar pelos exemplos Sage disponibilizados).**

Na operação MixColumns, cada byte de uma coluna é gerado como um novo valor somando todos os quatro bytes dessa coluna.

Portanto, para a operação MixColumns,

entrada = 67 89 AB CD

![Calculo1](https://i.imgur.com/UAQVTWZ.png)

Verificação com a inverse mix column matrix nos dá:

![Calculo2](https://i.imgur.com/EDBXtnC.png)

Agora, alterando o primeiro bit na entrada, portanto,

entrada = 77 89 AB CD

![Calculo3](https://i.imgur.com/UenGKkK.png)

O número de bits alterados na saída é 5, quando o primeiro bit é alterado na entrada.




