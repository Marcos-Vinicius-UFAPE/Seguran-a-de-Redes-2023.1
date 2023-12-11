**1. Responda os questionamentos a seguir:**
**(a) Por que é importante estudar a cifra de Feistel?**
A cifra de Feistel é uma estrutura fundamental em criptografia simétrica, sendo utilizada em diversos algoritmos de cifragem, como o DES (Data Encryption Standard). O estudo da cifra de Feistel ajuda a compreender princípios importantes de construção de cifras simétricas, como difusão e confusão, e fornece insights sobre a segurança e eficiência desses algoritmos.

**(b) Qual é a diferença entre uma cifra de bloco e uma cifra de fluxo?**
Uma cifra de bloco opera sobre blocos fixos de dados, cifrando cada bloco separadamente. Exemplos incluem DES e AES. Por outro lado, uma cifra de fluxo opera bit a bit ou byte a byte, cifrando os dados conforme são transmitidos. Exemplos incluem RC4. A principal diferença é a forma como tratam os dados de entrada.

(c) Por que não é prático usar uma cifra de substituição reversível qualquer do tipo mostrado na Tabela 3.1?
Cifras de substituição reversíveis simples, como as mostradas na Tabela 3.1, não oferecem boa segurança devido à falta de difusão e confusão. Pequenas mudanças nos dados de entrada geralmente resultam em mudanças previsíveis nos dados de saída, o que facilita a análise criptoanalítica. Além disso, não conseguem resistir a ataques de frequência de letras ou padrões comuns.

**(d) O que é uma cifra de produto?**
Uma cifra de produto é um tipo de cifra simétrica que opera multiplicando os dados de entrada por uma chave. Isso é geralmente feito através de operações bitwise, como XOR e AND. A multiplicação adiciona uma camada de complexidade à operação de cifragem.

**(e) Qual é a diferença entre difusão e confusão?**
Difusão refere-se à dispersão de informações no texto cifrado em resposta a mudanças nos dados de entrada. Confusão refere-se a tornar a relação entre a chave e o texto cifrado tão complexa quanto possível. Em resumo, difusão espalha os efeitos das mudanças nos dados de entrada, enquanto confusão torna a relação entre a chave e o texto cifrado difícil de entender.

**(f) Que parâmetros e escolhas de projeto determinam o algoritmo real de uma cifra de Feistel?**
Os principais parâmetros incluem o número de rodadas, o tamanho dos blocos, a escolha das funções de substituição e permutação, e a geração de subchaves. O número de rodadas afeta a segurança, enquanto o tamanho dos blocos influencia o tamanho do texto cifrado. As funções de substituição e permutação, juntamente com a geração de subchaves, afetam diretamente a confusão e difusão na cifra.

**(g) Explique o efeito avalanche.**
O efeito avalanche refere-se à propriedade desejável em algoritmos criptográficos onde uma pequena mudança nos dados de entrada ou na chave resulta em mudanças significativas nos dados de saída. Em outras palavras, uma alteração mínima em qualquer parte dos dados de entrada ou da chave deve afetar drasticamente o texto cifrado, aumentando assim a segurança do algoritmo contra análises criptoanalíticas. O objetivo é criar um efeito dominó, onde pequenas alterações se propagam e causam grandes alterações no resultado cifrado.


**2. Qual(is) dos recursos abaixo estão presentes no projeto da rede de Feistel? Explique.**
**(a) Tamanho do bloco e da chave;**
**(b) Função da rodada;**
**(c) Gerador de sub-chaves;**
**(d) Todas as alternativas.**

Resposta: letra d - Todas as alternativas

(a) Tamanho do bloco e da chave:
   - O tamanho do bloco e da chave é uma parte crucial do projeto da rede de Feistel. Esses parâmetros determinam o tamanho dos blocos de dados que serão processados pela cifra e a quantidade de bits na chave usada para a cifragem. O tamanho do bloco afeta a quantidade de dados que podem ser cifrados de uma vez, enquanto o tamanho da chave influencia diretamente a segurança do algoritmo.

(b) Função da rodada:
   - A função da rodada é um componente central do projeto da rede de Feistel. Essa função é aplicada repetidamente em cada rodada do processo de cifragem e decifragem. Ela realiza operações como substituição, permutação e outras transformações nos dados, contribuindo para a difusão e confusão necessárias para a segurança da cifra.

(c) Gerador de sub-chaves:
   - O gerador de sub-chaves é responsável por gerar as chaves individuais usadas em cada rodada da cifra de Feistel. Essas sub-chaves são derivadas a partir da chave principal e são cruciais para a segurança do algoritmo. A maneira como as sub-chaves são geradas e usadas influencia diretamente na segurança e eficácia da cifra.

Todos os elementos mencionados (tamanho do bloco e da chave, função da rodada e gerador de sub-chaves) são componentes essenciais no projeto de uma rede de Feistel.

**3. Qual é o tamanho do texto claro no Data Encryption Standard (DES)? Explique.**
**(a) 57;**
**(b) 48;**
**(c) 32;**
**(d) 64.**

Resposta: letra d - 64

O tamanho do bloco de texto claro no Data Encryption Standard (DES) é de 64 bits. O DES é um algoritmo de cifra de bloco, e cada bloco de texto claro que entra no algoritmo tem 64 bits de tamanho. Este tamanho inclui os bits de dados e também bits de paridade, embora apenas 56 bits sejam usados efetivamente para a cifragem e decifragem, e os bits de paridade são utilizados para detecção de erros.

**4. A cifra de Feistel do algoritmo de encriptação utilizada no Data Encryption Standard (DES) utiliza quantos S-boxes? Explique.**
**(a) 8;**
**(b) 7;**
**(c) 6;**
**(d) 5.**

Resposta: letra a - 8

A cifra de Feistel no algoritmo de encriptação utilizado no Data Encryption Standard (DES) utiliza 8 S-boxes (Substitution boxes). Essas S-boxes são componentes cruciais na transformação dos dados durante o processo de cifragem. Cada S-box substitui um bloco de bits de entrada por um bloco de bits de saída, contribuindo para a confusão e difusão no algoritmo. No caso do DES, cada S-box tem uma entrada de 6 bits e uma saída de 4 bits. Portanto, a cifra de Feistel no DES envolve o uso de 8 S-boxes.

**5. O Data Encryption Standard possui uma chave de 56 bits, o que torna possível um espaço de 2^56 chaves possíveis. Essa sentença trata de ataque de. . . Explique.**
**(a) Tempo;**
**(b) Matemático;**
**(c) Força-Bruta;**
**(d) DoS.**

Resposta: letra a - Força-Bruta

A sentença "O Data Encryption Standard possui uma chave de 56 bits, o que torna possível um espaço de \(2^{56}\) chaves possíveis" refere-se à vulnerabilidade do DES a ataques de força-bruta. Um ataque de força-bruta envolve a tentativa sistemática de todas as possíveis combinações de chaves até encontrar a chave correta que descriptografa com sucesso os dados cifrados.

No caso do DES, com uma chave de 56 bits, há um espaço de \(2^{56}\) chaves possíveis. Isso significa que um atacante poderia, teoricamente, testar todas essas chaves até encontrar a correta. Com avanços na capacidade de processamento e técnicas de ataque, uma chave de 56 bits não é mais considerada suficientemente segura, e o DES não é recomendado para uso em ambientes que requerem alta segurança.

**1. Considere uma cifra de Feistel composta de 16 rodadas com tamanho de bloco de 128 bits e tamanho de chave de 128 bits. Suponha que, para determinado k, o algoritmo de escalonamento de chave defina valores as oito primeiras chaves de rodada, k1, k2, . . . , k8, e depois estabeleça**

**k9 = k8, k10 = k7, k11 = k6, . . . , k16 = k1**

**Admita que você tenha um texto cifrado S. Explique como, com acesso a um oráculo de encriptação, você pode decriptar c e determinar m usando apenas uma única consulta a ele. Isso mostra que tal cifra é vulnerável a um ataque de texto claro escolhido. (Um oráculo de encriptação pode ser imaginado como um dispositivo que, dado um texto claro, retorna o texto cifrado correspondente. Os detalhes internos do dispositivo não são conhecidos, e você não pode abri-lo. Você só consegue obter informações do oráculo fazendo consultas a ele e observando suas respostas.)**

A situação descrita revela uma vulnerabilidade séria na cifra de Feistel proposta, demonstrando a vulnerabilidade a um ataque de texto claro escolhido e a debilidade na escolha das chaves de rodada.

Dado que as chaves de rodada são determinadas de maneira invertida após a oitava rodada (k9 = k8, k10 = k7, ..., k16 = k1), se tivermos acesso a um oráculo de encriptação, podemos realizar um ataque de criptoanálise diferencial.

O ataque de criptoanálise diferencial envolve a observação de como pequenas mudanças no texto claro afetam o texto cifrado. No caso descrito, podemos realizar os seguintes passos:

1. Escolher dois textos claros diferentes \(M_0\) e \(M_1\) que diferem apenas em um único bit na posição i (por exemplo, mudando o bit i de 0 para 1).
2. Encriptar \(M_0\) e \(M_1\) usando o oráculo de encriptação, resultando em \(C_0\) e \(C_1\).
3. Calcular a diferença \(C_0 \oplus C_1\). Esta diferença deve depender dos bits da chave de rodada associada à posição i.
4. Com base na diferença calculada, inferir informações sobre a chave de rodada associada.

Devido à natureza da escolha das chaves de rodada na cifra de Feistel, a diferença \(C_0 \oplus C_1\) nos fornecerá informações diretamente sobre a chave de rodada associada. Se a diferença for constante ou previsível, poderemos determinar a chave de rodada. Com essa chave de rodada conhecida, podemos desfazer as operações nas rodadas subsequentes e decifrar o texto cifrado.

Portanto, a cifra de Feistel descrita é vulnerável a um ataque de texto claro escolhido, e a escolha das chaves de rodada na forma indicada permite que um atacante descubra a chave de rodada com apenas uma consulta ao oráculo de encriptação. Essa vulnerabilidade compromete significativamente a segurança da cifra.