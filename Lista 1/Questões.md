**1. O que é a arquitetura de segurança OSI?**
A arquitetura de segurança OSI (Open Systems Interconnection) é uma estrutura conceitual que descreve os processos de segurança em uma rede de comunicação.Ela é composta por sete camadas que definem funções e protocolos de segurança em cada camada para garantir a proteção dos dados e comunicações.

**2. Qual é a diferença entre ameaças à segurança passivas e ativas?**
- Ameaças passivas são aquelas em que um atacante monitora as comunicações, como interceptação de dados, sem modificar ativamente os dados.
   - Ameaças ativas envolvem ações que um atacante realiza para modificar, interromper ou interferir ativamente nas comunicações, como ataques de injeção de pacotes ou ataques de negação de serviço (DoS).

**3. Liste e defina resumidamente as categorias de ataques passivos e ativos à segurança.**
   - Ataques passivos: Monitoramento não autorizado, análise de tráfego, escuta clandestina.
   - Ataques ativos: Ataques de injeção, ataques de negação de serviço, interceptação e modificação de dados.

**4. Liste e defina resumidamente as categorias dos serviços de segurança.**
   - Autenticação: Garante que a entidade de comunicação seja quem diz ser.
   - Confidencialidade: Protege informações contra acesso não autorizado.
   - Integridade: Garante que os dados não foram alterados durante a transmissão.
   - Não repúdio: Impede que uma entidade negue a autenticidade de uma comunicação.

**5. liste e defina resumidamente as categorias dos mecanismos de segurança.**
   - Criptografia: Usada para proteger a confidencialidade dos dados.
   - Controle de acesso: Regula quem pode acessar recursos ou informações.
   - Assinaturas digitais: Usadas para garantir a autenticidade e a integridade dos dados.
   - Firewalls: Controlam o tráfego de rede para proteger contra ameaças.

**6. Considere um caixa eletrônico, ATM no qual os usuários fornecem um cartão e um número de identificação pessoal (senha). Dê exemplos de requisitos de confidencialidade, integridade e disponibilidade associados com esse sistema e, em cada caso, indique o grau de importância desses requisitos.**
   - Confidencialidade: Os dados do usuário, como número de identificação pessoal (PIN), devem ser mantidos em sigilo para evitar acesso não autorizado.
   - Integridade: Garantir que as transações não sejam alteradas durante a comunicação e processamento.
   - Disponibilidade: Assegurar que os caixas eletrônicos estejam sempre operacionais para atender às necessidades dos usuários. A disponibilidade é crítica em serviços financeiros.

**7. Para responder as letras abaixo, por favor, consulte o livro-texto da disciplina:**
**(a) Desenhe uma matriz similar ao Quadro 1.4 que mostre o relacionamento entre serviços de segurança e ataques.**
Serviços\Mecanismos | Cod | Ass digital | Ctrl acesso | Troca de autenticação | Preenchimento de tráfego | Controle de roteamento | Notorização |
--------------------| --- | ----------- | ----------- | --------------------- | ------------------------ | ---------------------- | ----------- |
Autenticação de entidade pareada | S | S |  |  | S |  |  |  |
Autenticação de entidade pareada | S | S |  |  |  |  |  |  |
Controle de acesso |  |  | S |  |  |  |  |  |
Confidencialidade | S |  |  |  |  |  | S |  |
Confidencialidade do fluxo de tráfego | S |  |  |  |  | S | S |  |
Integridade dos dados | S | S |  | S |  |  |  |  |
Responsabilização |  | S |  | S |  |  |  | S |
Disponibilidade |  |  |  | S | S |  |  |  |

**(b) Desenhe uma matriz similar ao Quadro 1.4 que mostre o relacionamento entre mecanismos de segurança e ataques.**
Serviços\Mecanismos | Cod | Ass digital | Ctrl acesso | Troca de autenticação | Preenchimento de tráfego | Controle de roteamento | Notorização |
--------------------| --- | ----------- | ----------- | --------------------- | ------------------------ | ---------------------- | ----------- |
Autenticação de entidade pareada | S | S |  |  | S |  |  |  |
Autenticação de entidade pareada | S | S |  |  |  |  |  |  |
Controle de acesso |  |  | S |  |  |  |  |  |
Confidencialidade | S |  |  |  |  |  | S |  |
Confidencialidade do fluxo de tráfego | S |  |  |  |  | S | S |  |
Integridade dos dados | S | S |  | S |  |  |  |  |
Responsabilização |  | S |  | S |  |  |  |  |
Disponibilidade |  |  |  | S | S |  |  | S |

