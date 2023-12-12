**1. O que é encriptação tripla?**

É uma técnica de encripitação múltipla para tratar de uma potêncial vulnerabilidade do DES a um ataque por força bruta. Onde se usa uma encriptação múltipla com DES e múltiplas chaves. A encriptação tripla mais aceita é a Triple DES com três chaves e possui um tamanho de chave efetivo de 168 bits, que são 3 chaves de 64 bits, embora apenas 56 bits de cada chave são efetivamente usados, os outros 8 bits são usados para verificar paridade.

**2. O que é ataque meet-in-the-middle?**

É um algoritmo de força bruta para realizar um ataque ao esquema de encriptação múltipla DES duplo. O algoritmo a partir de um Par conhecido (P, C), primeiro encripta P para todos os 2⁵56 valores possíveis e os armazena em uma tabela, depois ele decripta C para todos os 2⁵6 valores possíveis. À medida que cada decriptação é produzida, ele compara o resultado com a tabela, em busca de uma ocorrência. Se houver uma correspondência, então ele confronta as duas chaves resultantes com um novo par de texto claro/texto cifrado conhecido. Se as duas chaves
à produzirem o texto cifrado esperado, e aceita elas como as corretas.  

**3. Quantas chaves são usadas na encriptação tripla?**

Duas ou três chaves. Existe o triple DES com duas chaves e o triple DES com três chaves

**4. Por que a parte do meio do 3DES é decriptação, em vez de encriptação?**

Não existe significado criptográfico no uso da decriptação para o segundo estágio. Sua única vantagem é que está relacionado à retrocompatibilidade com implementações existentes do DES, permitindo que o 3DES seja usado em sistemas que originalmente só suportavam DES.

**5. Por que alguns modos de operação de cifra de bloco só utilizam a encriptação, enquanto outros empregam encriptação e decriptação?**

Alguns modos de operação utilizam apenas uma função de criptografia porque ela é usada para gerar algo para ser aplicado em um XOR com o texto simples. Não há necessidade de descriptografar os bytes gerados. Para descriptografar o texto cifrado, você só precisa da mesma sequência de bytes.

Outros modos (por exemplo, CBC) criptografam diretamente valores secretos (ou seja, o texto simples), o que significa que a descriptografia é necessária para descobrir qual era o valor secreto.

**6. Você deseja construir um dispositivo de hardware para realizar encriptação de bloco no modo cipher block chaining (CBC) usando um algoritmo mais forte do que DES. 3DES é um bom candidato. A Figura 1 mostra duas possibilidades, ambas acompanhando a definição do CBC. Qual das duas você escolheria:**

**(a) Por segurança?**

Um loop de 3 fases pode se beneficiar da capacidade de processar blocos grandes com uma chave antes de alternar. Se os IVs (Vetores de Inicialização) forem ocultos, o processo de determinação no loop de 3 fases requer mais bits, portanto, em ataques de força bruta, o loop de 3 fases é mais seguro do que o loop de 1 fase.

**(b) Por desempenho?**

Um loop possui pelo menos dois XORs por bloco. O loop de 3 fases tem a capacidade de operar em blocos grandes com uma única chave, onde a escolha do modo espera que as diferenças de desempenho sejam menores do que as diferenças de variação natural no estilo de programação. Quando se trata de hardware, o loop de 3 fases é significativamente mais rápido em comparação com o loop de 1 fase devido ao pipelining.