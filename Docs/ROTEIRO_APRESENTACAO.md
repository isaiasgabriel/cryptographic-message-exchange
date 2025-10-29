# 🎤 Roteiro de Apresentação - Trabalho Prático 1
## Sistema de Comunicação Segura entre Usuários

**Disciplina**: SA28S - Segurança e Auditoria em Sistemas  
**Professor**: Erinaldo Pereira  
**UTFPR - Campus Dois Vizinhos**

---

## 📋 Estrutura da Apresentação (15-20 minutos)

1. Introdução e Contexto (2 min)
2. Problema e Objetivos (2 min)
3. Fundamentação Teórica (3 min)
4. Arquitetura do Sistema (3 min)
5. Demonstração Prática (5-7 min)
6. Resultados e Conclusões (2 min)
7. Perguntas (3 min)

---

## 🎬 PARTE 1: INTRODUÇÃO E CONTEXTO (2 min)

### **[SLIDE 1: Título]**

**FALA:**
> "Bom dia/Boa tarde. Hoje vamos apresentar o Trabalho Prático 1 da disciplina de Segurança e Auditoria em Sistemas, que consiste em um sistema de comunicação segura entre usuários, simulando a troca de mensagens entre Alice e Bob."

### **[SLIDE 2: Contexto]**

**FALA:**
> "No mundo digital atual, a troca de mensagens pela internet é constante. Mas como garantir que uma mensagem enviada seja:
> - **Confidencial**: Só o destinatário possa ler
> - **Autêntica**: Realmente veio de quem diz ser
> - **Íntegra**: Não foi alterada no caminho
> 
> Este trabalho demonstra como implementar essas garantias na prática usando criptografia moderna."

---

## 🎯 PARTE 2: PROBLEMA E OBJETIVOS (2 min)

### **[SLIDE 3: Cenário do Problema]**

**FALA:**
> "Imagine que Alice quer enviar a mensagem 'Encontro às 15h' para Bob pela internet. Vários problemas podem acontecer:
> 
> **Problema 1 - Espionagem**: Um hacker intercepta e lê a mensagem.  
> **Problema 2 - Adulteração**: O hacker muda para 'Encontro às 18h'.  
> **Problema 3 - Personificação**: O hacker se passa por Alice e envia mensagem falsa.
> 
> Precisamos resolver esses três problemas simultaneamente."

### **[SLIDE 4: Objetivos]**

**FALA:**
> "Nossos objetivos são:
> 1. Implementar um sistema que proteja a **confidencialidade** usando criptografia
> 2. Garantir **integridade** através de funções hash
> 3. Assegurar **autenticidade** com assinaturas digitais
> 4. Validar identidades usando certificados digitais
> 5. Demonstrar que o sistema detecta qualquer tentativa de adulteração."

---

## 📚 PARTE 3: FUNDAMENTAÇÃO TEÓRICA (3 min)

### **[SLIDE 5: Os 5 Algoritmos Usados]**

**FALA:**
> "Nosso sistema combina **cinco algoritmos criptográficos**, cada um com uma função específica. Vou explicar cada um:"

### **1. SHA-256 (Hash)**

**FALA:**
> "Primeiro, o **SHA-256**. É uma função hash que transforma qualquer mensagem em um código de 256 bits, uma 'impressão digital'.
> 
> **Função no sistema**: Criar um resumo da mensagem para detectar alterações.
> 
> **Por que usar**: Se alguém mudar um único caractere da mensagem, o hash fica completamente diferente. É como uma impressão digital única da mensagem."

### **2. AES-256 (Criptografia Simétrica)**

**FALA:**
 "Segundo, o **AES-256**. É um algoritmo de criptografia simétrica, que usa a mesma chave para criptografar e descriptografar.
 
 **Função no sistema**: Criptografar o conteúdo da mensagem rapidamente.
 
 **Por que usar**: AES é extremamente rápido, ideal para criptografar mensagens de qualquer tamanho. Mas há um problema: como compartilhar a chave com segurança? É aí que entra o RSA."

### **3. RSA-2048 (Criptografia Assimétrica)**

**FALA:**
> "Terceiro, o **RSA**. É criptografia assimétrica: usa duas chaves diferentes - uma pública e uma privada.
> 
> **Função no sistema**: Proteger a chave AES durante a transmissão.
> 
> **Como funciona**: Alice criptografa a chave AES com a chave **pública** de Bob. Só a chave **privada** de Bob pode descriptografar. Assim, a chave AES viaja segura pela internet."

### **4. RSA-PSS (Assinatura Digital)**

**FALA:**
> "Quarto, **assinatura digital RSA-PSS**. É o processo inverso: Alice usa sua chave **privada** para assinar o hash da mensagem.
> 
> **Função no sistema**: Provar que Alice realmente enviou aquela mensagem.
> 
> **Como funciona**: Bob usa a chave **pública** de Alice para verificar a assinatura. Se for válida, prova que:
> - A mensagem veio de Alice (autenticidade)
> - A mensagem não foi alterada (integridade)"

### **5. X.509 (Certificado Digital)**

**FALA:**
> "Quinto, **certificado digital X.509**. É um documento que liga uma chave pública a uma identidade.
> 
> **Função no sistema**: Garantir que a chave pública realmente pertence a quem diz ser.
> 
> **Como funciona**: Uma Autoridade Certificadora (CA) confiável assina o certificado dizendo: 'Esta chave pública pertence a Bob'. Assim, Alice tem certeza de que não está usando a chave de um impostor."

---

## 🏗️ PARTE 4: ARQUITETURA DO SISTEMA (3 min)

### **[SLIDE 6: Diagrama de Classes]**

**FALA:**
> "Nosso sistema tem três classes principais:
> 
> **CertificateAuthority (CA)**: A autoridade certificadora que emite e valida certificados.
> 
> **User**: Representa Alice e Bob. Cada usuário tem seu par de chaves RSA e pode enviar e receber mensagens.
> 
> A CA é compartilhada por todos os usuários, estabelecendo confiança no sistema."

### **[SLIDE 7: Fluxo - FASE 0: Preparação]**

**FALA:**
> "Antes de trocar mensagens, há uma fase de preparação:
> 
> **Passo 1**: A CA gera seu par de chaves RSA.
> 
> **Passo 2**: Alice gera seu par de chaves RSA e pede certificado à CA.
> 
> **Passo 3**: Bob faz o mesmo.
> 
> Agora todos têm certificados confiáveis e podem se comunicar com segurança."

### **[SLIDE 8: Fluxo - FASE 1: Alice Envia Mensagem]**

**FALA:**
> "Quando Alice quer enviar 'Encontro às 15h' para Bob, acontecem **7 passos**:
> 
> **Passo 1**: Alice verifica o certificado de Bob com a CA. ✅
> 
> **Passo 2**: Alice gera uma chave AES aleatória de 256 bits.
> 
> **Passo 3**: Alice criptografa a mensagem com AES. Agora está ilegível.
> 
> **Passo 4**: Alice criptografa a chave AES com a chave pública de Bob (RSA).
> 
> **Passo 5**: Alice calcula o hash SHA-256 da mensagem original.
> 
> **Passo 6**: Alice assina o hash com sua chave privada (assinatura digital).
> 
> **Passo 7**: Alice monta um pacote contendo: mensagem criptografada, chave AES criptografada, assinatura e seu certificado. Este pacote é enviado para Bob."

### **[SLIDE 9: Fluxo - FASE 2: Bob Recebe Mensagem]**

**FALA:**
> "Quando Bob recebe o pacote, ele executa **4 passos de verificação**:
> 
> **Passo 1**: Bob verifica o certificado de Alice com a CA. Confirma que é realmente Alice.
> 
> **Passo 2**: Bob usa sua chave privada RSA para descriptografar a chave AES. Só ele consegue fazer isso.
> 
> **Passo 3**: Bob usa a chave AES para descriptografar a mensagem. Recupera 'Encontro às 15h'.
> 
> **Passo 4**: Bob verifica a autenticidade:
> - Calcula o hash da mensagem descriptografada
> - Usa a chave pública de Alice para verificar a assinatura
> - Compara os hashes
> 
> Se os hashes forem iguais, Bob tem certeza de que:
> - A mensagem veio de Alice (autenticidade)
> - Não foi alterada (integridade)
> - Só ele conseguiu ler (confidencialidade)"

---

## 💻 PARTE 5: DEMONSTRAÇÃO PRÁTICA (5-7 min)

### **[SLIDE 10: Ambiente de Execução]**

**FALA:**
> "Agora vamos ver o sistema funcionando. Implementamos em Python usando a biblioteca `cryptography`, que é padrão da indústria e usada em sistemas reais."

### **[DEMO 1: Preparação do Sistema]**

**[Executar: `python3 message.py`]**

**FALA:**
> "Observem a FASE 0 - Preparação do Sistema:
> 
> A CA está sendo criada e gera seu par de chaves RSA de 2048 bits.
> 
> Agora Alice é inicializada: gera suas chaves RSA e recebe certificado da CA.
> 
> Bob faz o mesmo processo.
> 
> *[Opcional: mostrar as chaves PEM]*
> Aqui podemos ver as chaves em formato PEM. A chave privada é extensa e deve ser mantida em segredo. A chave pública pode ser compartilhada."

### **[DEMO 2: Envio da Mensagem]**

**FALA:**
> "Agora entramos na FASE 1 - Alice envia a mensagem 'Encontro às 15h':
> 
> **Passo 1**: Alice verifica o certificado de Bob. ✅ Válido!
> 
> **Passo 2**: Chave AES gerada. Vejam os primeiros bytes em hexadecimal.
> 
> **Passo 3**: Mensagem criptografada com AES. O texto 'Encontro às 15h' virou este código incompreensível.
> 
> **Passo 4**: A chave AES foi criptografada com RSA. Agora tem 256 bytes.
> 
> **Passo 5**: Hash SHA-256 calculado. Essa é a 'impressão digital' da mensagem.
> 
> **Passo 6**: Hash assinado digitalmente por Alice.
> 
> **Passo 7**: Pacote montado. Vejam a visualização completa do pacote:
> - Mensagem criptografada: 32 bytes
> - IV: 16 bytes
> - Chave AES criptografada: 256 bytes
> - Assinatura: 256 bytes
> - Certificado de Alice: completo em formato X.509"

### **[DEMO 3: Recebimento e Verificação]**

**FALA:**
> "FASE 2 - Bob recebe e processa a mensagem:
> 
> **Passo 1**: Bob verifica o certificado. ✅ É de Alice!
> 
> Observem os detalhes técnicos:
> - Algoritmo usado: RSA para verificação
> - Chave usada: Pública da CA
> 
> **Passo 2**: Bob descriptografa a chave AES com sua chave privada.
> 
> Vejam: a chave foi recuperada! Os primeiros bytes correspondem à chave que Alice gerou.
> 
> **Passo 3**: Bob descriptografa a mensagem com AES.
> 
> Mensagem recuperada: 'Encontro às 15h'. ✅
> 
> Mas atenção: ainda não terminamos! Precisamos verificar se é autêntica.
> 
> **Passo 4**: Verificação de integridade e autenticidade:
> 
> 4.1 - Bob calcula o hash da mensagem. Vejam o hash.
> 
> 4.2 - Bob verifica a assinatura usando a chave pública de Alice.
> 
> O sistema descriptografa a assinatura, extrai o hash que Alice assinou, e compara com o hash local.
> 
> ✅ **VERIFICAÇÃO BEM-SUCEDIDA!**
> 
> O sistema confirmou:
> 1️⃣ Confidencialidade: Mensagem estava protegida
> 2️⃣ Autenticidade: Veio de Alice
> 3️⃣ Integridade: Não foi alterada"

### **[DEMO 4: Simulação de Ataque (Opcional)]**

**FALA (se houver tempo):**
> "Para demonstrar a segurança, podemos simular um ataque. Se alterássemos um único byte da mensagem criptografada ou da assinatura, o sistema detectaria imediatamente na verificação do Passo 4, mostrando 'FALHA DE SEGURANÇA'."

---

## 📊 PARTE 6: RESULTADOS E CONCLUSÕES (2 min)

### **[SLIDE 11: Resultados Obtidos]**

**FALA:**
> "Nosso sistema alcançou todos os objetivos propostos:
> 
> ✅ **Confidencialidade**: Implementada com AES-256-CBC + RSA-OAEP
> - Mensagem protegida durante transmissão
> - Chave de sessão única para cada mensagem
> 
> ✅ **Integridade**: Garantida com SHA-256 + Assinatura Digital
> - Qualquer alteração é detectada
> - Hash funciona como impressão digital
> 
> ✅ **Autenticidade**: Assegurada com RSA-PSS + Certificados X.509
> - Impossível falsificar remetente
> - CA valida identidades
> 
> ✅ **Detecção de Adulteração**: Sistema acusa erro quando:
> - Certificado é inválido
> - Assinatura não corresponde
> - Mensagem foi alterada"

### **[SLIDE 12: Tecnologias Utilizadas]**

**FALA:**
> "Implementamos usando:
> - **Linguagem**: Python 3
> - **Biblioteca**: `cryptography` (padrão da indústria)
> - **Padrões**: Seguimos as melhores práticas de segurança:
>   - RSA 2048 bits (recomendação atual)
>   - AES 256 bits (padrão forte)
>   - SHA-256 (resistente a colisões)
>   - Padding OAEP e PSS (seguros contra ataques)
>   - IV aleatório (evita padrões)"

### **[SLIDE 13: Conclusões]**

**FALA:**
> "Conclusões:
> 
> 1. **Criptografia moderna resolve problemas complexos** de segurança combinando diferentes algoritmos, cada um com sua especialidade.
> 
> 2. **Não existe 'bala de prata'**: Precisamos de hash para integridade, criptografia simétrica para velocidade, assimétrica para troca de chaves, assinatura para autenticidade, e certificados para confiança.
> 
> 3. **Estes conceitos são usados diariamente**: HTTPS, WhatsApp, VPNs, e-mail seguro, todos usam esses mesmos princípios.
> 
> 4. **Segurança é em camadas**: Cada algoritmo resolve um problema específico, e juntos formam um sistema robusto."

### **[SLIDE 14: Aplicações Reais]**

**FALA:**
> "Este sistema não é apenas acadêmico. Os mesmos conceitos são usados em:
> 
> - **HTTPS/TLS**: Navegação web segura
> - **PGP/GPG**: E-mail criptografado
> - **Signal/WhatsApp**: Mensagens instantâneas
> - **VPN**: Redes privadas virtuais
> - **SSH**: Acesso remoto seguro
> - **Blockchain**: Assinaturas de transações"

---

## ❓ PARTE 7: PERGUNTAS (3 min)

### **[SLIDE 15: Obrigado]**

**FALA:**
> "Isso conclui nossa apresentação. Estamos abertos a perguntas."

---

## 🎯 POSSÍVEIS PERGUNTAS E RESPOSTAS

### **P1: "Por que usar AES E RSA? Por que não só RSA?"**

**R:**
> "Excelente pergunta! RSA é muito lento para criptografar mensagens grandes. AES é cerca de 1000 vezes mais rápido. Por isso usamos criptografia híbrida: AES para a mensagem (rápido) e RSA apenas para proteger a chave AES (pequena)."

### **P2: "O que acontece se a chave privada de Bob for roubada?"**

**R:**
> "Se a chave privada de Bob for comprometida, o atacante poderá descriptografar mensagens futuras enviadas para Bob. Por isso, chaves privadas devem ser:
> - Armazenadas com segurança
> - Protegidas por senha
> - Renovadas periodicamente
> - Nunca compartilhadas"

### **P3: "A CA não vira um ponto único de falha?"**

**R:**
> "Sim, é um ponto crítico! Por isso:
> - CAs reais têm segurança física e lógica extrema
> - Usam HSMs (Hardware Security Modules)
> - Têm auditorias constantes
> - Certificados têm validade limitada
> - Existe hierarquia de CAs (raiz, intermediárias)"

### **P4: "Quantum computing vai quebrar esse sistema?"**

**R:**
> "Computadores quânticos podem quebrar RSA no futuro. Por isso já existem pesquisas em criptografia pós-quântica (PQC). O NIST está padronizando novos algoritmos resistentes a quantum. Mas AES-256 continua seguro mesmo contra computadores quânticos."

### **P5: "Por que não assinar a mensagem criptografada em vez do hash?"**

**R:**
> "Duas razões:
> 1. **Eficiência**: Assinar é lento. Hash de 32 bytes é muito mais rápido que assinar a mensagem inteira.
> 2. **Padrão**: Assina-se o hash da mensagem **original**, não da criptografada, para validar a integridade do texto plano."

### **P6: "Como saber se a CA é confiável?"**

**R:**
> "Na vida real:
> - Navegadores vêm com lista de CAs confiáveis pré-instaladas
> - CAs passam por auditorias rigorosas
> - Certificados podem ser revogados (CRL/OCSP)
> - Usuários podem verificar 'fingerprint' do certificado
> 
> Em nosso sistema, simulamos uma CA local para fins educacionais."

### **P7: "Qual o tamanho ideal de chave RSA?"**

**R:**
> "Atualmente:
> - **2048 bits**: Padrão mínimo recomendado (usamos este)
> - **3072 bits**: Mais seguro, uso crescente
> - **4096 bits**: Muito seguro, mas mais lento
> 
> Chaves abaixo de 2048 bits são consideradas inseguras."

---

## 📝 DICAS PARA A APRESENTAÇÃO

### **Antes da Apresentação:**
1. ✅ Teste o código 2-3 vezes
2. ✅ Verifique se Python e dependências estão instalados
3. ✅ Prepare backup em vídeo (caso algo falhe)
4. ✅ Cronometre para não ultrapassar tempo
5. ✅ Ensaie transições entre slides e demo

### **Durante a Apresentação:**
1. ✅ Fale olhando para a plateia, não para a tela
2. ✅ Use ponteiro ou mouse para destacar elementos importantes
3. ✅ Controle a velocidade: nem rápido demais, nem lento
4. ✅ Faça pausas após conceitos importantes
5. ✅ Mostre entusiasmo pelo trabalho

### **Na Demonstração:**
1. ✅ Aumente o zoom do terminal (fonte grande)
2. ✅ Vá pausando e explicando cada seção
3. ✅ Destaque os números hexadecimais importantes
4. ✅ Mostre a transformação: texto → criptografado → texto
5. ✅ Tenha print screens prontos (plano B)

### **Linguagem Corporal:**
1. ✅ Postura ereta e confiante
2. ✅ Gestos naturais para enfatizar pontos
3. ✅ Contato visual com diferentes pessoas
4. ✅ Sorria (mostra confiança)
5. ✅ Movimente-se um pouco (não fique estático)

---

## ⏱️ CONTROLE DE TEMPO

| Parte | Tempo | Checkpoint |
|-------|-------|------------|
| Introdução | 2 min | Contexto explicado |
| Problema e Objetivos | 2 min | Cenário claro |
| Fundamentação | 3 min | 5 algoritmos explicados |
| Arquitetura | 3 min | Fluxo entendido |
| **Demonstração** | 5-7 min | **Sistema rodando** |
| Resultados | 2 min | Objetivos alcançados |
| Perguntas | 3 min | Dúvidas esclarecidas |
| **TOTAL** | **17-22 min** | ✅ |

---

## 🎬 FRASE DE ENCERRAMENTO

**FALA FINAL:**
> "Para concluir: implementamos um sistema completo de comunicação segura que demonstra na prática como a criptografia moderna protege nossas comunicações diárias. Combinando hash, criptografia simétrica e assimétrica, assinaturas digitais e certificados, conseguimos garantir confidencialidade, integridade e autenticidade das mensagens. Muito obrigado pela atenção!"

---

## 📚 MATERIAL DE APOIO

**Arquivos do Projeto:**
- `message.py`: Código principal
- `requirements.txt`: Dependências
- `README.md`: Documentação
- `EXPLICACAO_FLUXO.md`: Teoria detalhada

**Para Estudar Antes:**
- Revisar conceitos de criptografia simétrica vs assimétrica
- Entender o que é hash e suas propriedades
- Conhecer o funcionamento básico de RSA
- Compreender o papel de certificados digitais

---

## ✅ CHECKLIST PRÉ-APRESENTAÇÃO

- [ ] Código testado e funcionando
- [ ] Slides preparados
- [ ] Terminal configurado (fonte grande, cores)
- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Tempo cronometrado (ensaio)
- [ ] Perguntas frequentes estudadas
- [ ] Plano B preparado (prints/vídeo)
- [ ] Chegada com 15min antecedência
- [ ] Postura e confiança ✨

**BOA APRESENTAÇÃO! 🎉**

