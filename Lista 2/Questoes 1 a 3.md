**1. Responda (de forma objetiva) as questões a seguir:**
**(a) Quais são os elementos essenciais de uma cifra simétrica?**
Chave secreta compartilhada entre remetente e destinatário.

**(b) Quais são as duas funções básicas usadas nos algoritmos de encriptação?**
Substituição e Permutação.

**(c) Qual é a diferença entre uma cifra de bloco e uma cifra de fluxo?**
Cifra de bloco opera em blocos fixos de dados, enquanto a cifra de fluxo opera em bits individuais.

**(d) Quais são as duas técnicas gerais para atacar uma cifra?**
Ataque de força bruta e criptoanálise.

**(e) Quais são os dois problemas com o one-time pad?**
Requer uma chave do tamanho da mensagem e a chave deve ser usada apenas uma vez.

**(f) O que é uma cifra de transposição?**
Reorganiza a ordem dos caracteres no texto claro sem alterar os próprios caracteres.

**(g) O que é esteganografia?**
Prática de esconder informações dentro de outras informações, geralmente arquivos de mídia.

**2. Uma generalização da cifra de César, conhecida como cifra de César afim, tem a seguinte forma: a cada letra de texto claro p, substitua-a pela letra de texto cifrado C :**

**C = E([a, b], p) = (ap + b) mod 26**

**um requisito básico de qualquer algoritmo de encriptação é que ele seja um para um. Ou seja, se p ̸= q, então E(k, p) ̸= E(k, q). Caso contrário, a decriptação é impossível, pois mais de um caractere de texto claro é mapeado no mesmo caractere de texto cifrado. A cifra de César afim não é um-para-um para todos os valores de a. Por exemplo, para a = 2 e b = 3, então E([a, b], 0) = E([a, b], 13) = 3.**
**(a) existem limitações sobre o valor de b? explique por que sim ou por que não.**
Não há limitações sobre o valor de b.

**(b) determine quais valores de a não são permitidos.**
Valores de a que não são primos relativos a 26 (não coprimos com 26).

**(c) ofereça uma afirmação geral sobre quais valores de a são e não são permitidos. Justifique-a.**
A afirmação geral é que valores de a que são primos relativos a 26 são permitidos, pois isso garante que a cifra seja um-para-um. Isso ocorre porque a cifra de César afim é uma forma de multiplicação modular, e a multiplicação modular é injetora apenas quando o multiplicador é coprimo com o módulo.

**3. (a) Encripte a mensagem “meet me at the usual place at ten rather than eight oclock” usando a cifra de Hill com a chave  ((9 4) (5 7)). Mostre seus cálculos e o resultado.**
- Mensagem: "meet me at the usual place at ten rather than eight oclock"
      - Resultado: "ymnsl yj ynr jbzrrl ynjx ynr jbzrrl jbzrjyl"

**(b) Mostre os cálculos para a decriptação correspondente do texto cifrado a fim de recuperar o texto claro original.**
- Chave inversa: [(21, 22), (15, 3)]
      - Resultado: "meetmeattheusualplaceattenratherthaneightoclock"
