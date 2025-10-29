# 📊 Estrutura dos Slides - Apresentação

## Sugestão de Slides para PowerPoint/Google Slides

---

### **SLIDE 1: Título**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│     SISTEMA DE COMUNICAÇÃO SEGURA                   │
│        ENTRE USUÁRIOS                               │
│                                                     │
│     Trabalho Prático 1                              │
│     SA28S - Segurança e Auditoria em Sistemas       │
│                                                     │
│     [Seus nomes]                                    │
│     Prof. Erinaldo Pereira                          │
│     UTFPR - Campus Dois Vizinhos                    │
│                                                     │
│     [Data]                                          │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Logo UTFPR, ícone de cadeado

---

### **SLIDE 2: Contexto**
```
┌─────────────────────────────────────────────────────┐
│  POR QUE COMUNICAÇÃO SEGURA?                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  💬 Bilhões de mensagens trocadas diariamente       │
│                                                     │
│  ❓ Como garantir:                                  │
│     🔒 Confidencialidade                            │
│     ✍️  Autenticidade                               │
│     ✅ Integridade                                  │
│                                                     │
│  🎯 Solução: CRIPTOGRAFIA                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Ícones, cores (verde para seguro)

---

### **SLIDE 3: Cenário do Problema**
```
┌─────────────────────────────────────────────────────┐
│  ALICE QUER ENVIAR MENSAGEM PARA BOB                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Alice: "Encontro às 15h" ────────> Bob             │
│           │                                         │
│           │                                         │
│           └──> 👿 HACKER (Intercepta)               │
│                                                     │
│  ⚠️  PROBLEMAS:                                     │
│                                                     │
│  🕵️  Espionagem      → Lê a mensagem                │
│  ✏️  Adulteração     → Muda para "18h"              │
│  🎭 Personificação   → Se passa por Alice           │
│                                                     │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Diagrama Alice → Hacker → Bob

---

### **SLIDE 4: Objetivos**
```
┌─────────────────────────────────────────────────────┐
│  OBJETIVOS DO TRABALHO                              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ✅ Implementar Criptografia Híbrida                │
│     (AES + RSA)                                     │
│                                                     │
│  ✅ Garantir Integridade                            │
│     (SHA-256)                                       │
│                                                     │
│  ✅ Assegurar Autenticidade                         │
│     (Assinatura Digital)                            │
│                                                     │
│  ✅ Validar Identidades                             │
│     (Certificados X.509)                            │
│                                                     │
│  ✅ Detectar Adulterações                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 5: Os 5 Algoritmos**
```
┌─────────────────────────────────────────────────────┐
│  ALGORITMOS CRIPTOGRÁFICOS UTILIZADOS               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  #️⃣  SHA-256          → Integridade                │
│     Hash criptográfico                              │
│                                                     │
│  🔐 AES-256-CBC       → Confidencialidade           │
│     Criptografia Simétrica (Rápida)                 │
│                                                     │
│  🔑 RSA-2048-OAEP     → Troca de Chaves             │
│     Criptografia Assimétrica                        │
│                                                     │
│  ✍️  RSA-PSS          → Autenticidade               │
│     Assinatura Digital                              │
│                                                     │
│  📜 X.509             → Identidade                  │
│     Certificado Digital                             │
│                                                     │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Ícone para cada algoritmo

---

### **SLIDE 6: SHA-256 - Hash**
```
┌─────────────────────────────────────────────────────┐
│  SHA-256 - FUNÇÃO HASH                              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Entrada:  "Encontro às 15h"                        │
│      ↓                                              │
│  [SHA-256]                                          │
│      ↓                                              │
│  Saída:   0691cf24352a2018a46187aa...               │
│           (256 bits)                                │
│                                                     │
│  ✅ Propriedades:                                    │
│     • Tamanho fixo (32 bytes)                       │
│     • Unidirecional (não dá pra reverter)           │
│     • Qualquer mudança = hash diferente             │
│                                                     │
│  🎯 Função: Detectar alterações                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Diagrama de fluxo

---

### **SLIDE 7: AES - Criptografia Simétrica**
```
┌─────────────────────────────────────────────────────┐
│  AES-256 - CRIPTOGRAFIA SIMÉTRICA                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Mensagem: "Encontro às 15h"                        │
│     +                                               │
│  Chave: a3f7c9e1... (256 bits)                      │
│     ↓                                               │
│  [AES Criptografar]                                 │
│     ↓                                               │
│  Texto cifrado: 9ca662772487fe25...                 │
│                                                     │
│  ═══════════════════════════════                    │
│                                                     │
│  Texto cifrado: 9ca662772487fe25...                 │
│     +                                               │
│  Mesma Chave: a3f7c9e1...                           │
│     ↓                                               │
│  [AES Descriptografar]                              │
│     ↓                                               │
│  Mensagem: "Encontro às 15h"                        │
│                                                     │
│  🎯 Função: Criptografar mensagem (RÁPIDO!)         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 8: RSA - Criptografia Assimétrica**
```
┌─────────────────────────────────────────────────────┐
│  RSA - CRIPTOGRAFIA ASSIMÉTRICA                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Chave AES                                          │
│     ↓                                               │
│  [Cifrar com Chave PÚBLICA de Bob]                 │
│     ↓                                               │
│  Chave AES Criptografada                            │
│                                                     │
│  ═══════ INTERNET ═══════                           │
│                                                     │
│  Chave AES Criptografada                            │
│     ↓                                               │
│  [Decifrar com Chave PRIVADA de Bob]               │
│     ↓                                               │
│  Chave AES (recuperada)                             │
│                                                     │
│  ✅ Só Bob pode descriptografar!                    │
│                                                     │
│  🎯 Função: Proteger chave AES                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```
**Elementos visuais**: Cadeado aberto/fechado

---

### **SLIDE 9: Assinatura Digital**
```
┌─────────────────────────────────────────────────────┐
│  ASSINATURA DIGITAL RSA-PSS                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ALICE ASSINA:                                      │
│                                                     │
│  Hash da mensagem                                   │
│     ↓                                               │
│  [Assinar com Chave PRIVADA de Alice]              │
│     ↓                                               │
│  Assinatura Digital                                 │
│                                                     │
│  ═══════════════════════════════                    │
│                                                     │
│  BOB VERIFICA:                                      │
│                                                     │
│  Assinatura + Hash local                            │
│     ↓                                               │
│  [Verificar com Chave PÚBLICA de Alice]            │
│     ↓                                               │
│  ✅ Válida = Autêntica e Íntegra                    │
│  ❌ Inválida = Adulterada ou Falsa                  │
│                                                     │
│  🎯 Função: Provar autoria e integridade            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 10: Certificado Digital**
```
┌─────────────────────────────────────────────────────┐
│  CERTIFICADO DIGITAL X.509                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────┐               │
│  │ CERTIFICADO DE BOB              │               │
│  │─────────────────────────────────│               │
│  │ Nome: Bob                        │               │
│  │ Organização: UTFPR               │               │
│  │ Chave Pública: [chave de Bob]   │               │
│  │ Validade: 1 ano                  │               │
│  │                                  │               │
│  │ Assinado por: CA ✍️               │               │
│  └─────────────────────────────────┘               │
│                                                     │
│  👥 CA = Autoridade Certificadora Confiável         │
│                                                     │
│  ✅ Alice verifica assinatura da CA                 │
│  ✅ Confirma: "Esta é a chave de Bob"               │
│                                                     │
│  🎯 Função: Evitar impostor                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 11: Arquitetura - Classes**
```
┌─────────────────────────────────────────────────────┐
│  ARQUITETURA DO SISTEMA                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────────────────┐                      │
│  │  CertificateAuthority    │                      │
│  │  (CA)                     │                      │
│  │  • Emite certificados     │                      │
│  │  • Valida certificados    │                      │
│  └────────────┬─────────────┘                      │
│               │                                     │
│          Usa  │  Usa                                │
│               │                                     │
│    ┌──────────┴──────────┐                         │
│    │                     │                         │
│  ┌─▼─────────┐    ┌─────▼──┐                      │
│  │   Alice    │    │   Bob   │                      │
│  │   (User)   │    │  (User) │                      │
│  │ • Enviar   │    │ • Receber│                     │
│  │ • Receber  │    │ • Enviar │                     │
│  └────────────┘    └─────────┘                      │
│                                                     │
│  Linguagem: Python 3                                │
│  Biblioteca: cryptography                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 12: FASE 0 - Preparação**
```
┌─────────────────────────────────────────────────────┐
│  FASE 0: PREPARAÇÃO DO SISTEMA                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1️⃣  CA gera seu par de chaves RSA                  │
│     • Chave Privada CA (secreta)                    │
│     • Chave Pública CA (conhecida)                  │
│                                                     │
│  2️⃣  Alice gera seu par RSA                         │
│     • Solicita certificado à CA                     │
│     • CA emite certificado assinado                 │
│                                                     │
│  3️⃣  Bob gera seu par RSA                           │
│     • Solicita certificado à CA                     │
│     • CA emite certificado assinado                 │
│                                                     │
│  ✅ Todos têm certificados confiáveis!              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 13: FASE 1 - Alice Envia (7 Passos)**
```
┌─────────────────────────────────────────────────────┐
│  FASE 1: ALICE ENVIA MENSAGEM (7 PASSOS)            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. Verifica certificado de Bob        [RSA]       │
│  2. Gera chave AES aleatória            [AES]       │
│  3. Criptografa mensagem                [AES]       │
│  4. Criptografa chave AES               [RSA]       │
│  5. Calcula hash da mensagem            [SHA-256]   │
│  6. Assina o hash                       [RSA-PSS]   │
│  7. Monta pacote completo               [PKG]       │
│                                                     │
│  📦 PACOTE:                                          │
│     • Mensagem criptografada                        │
│     • IV                                            │
│     • Chave AES criptografada                       │
│     • Assinatura digital                            │
│     • Certificado de Alice                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 14: FASE 2 - Bob Recebe (4 Passos)**
```
┌─────────────────────────────────────────────────────┐
│  FASE 2: BOB RECEBE MENSAGEM (4 PASSOS)             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. Verifica certificado de Alice                   │
│     ✅ Confirma identidade                          │
│                                                     │
│  2. Descriptografa chave AES                        │
│     🔑 Usa sua chave privada RSA                    │
│                                                     │
│  3. Descriptografa mensagem                         │
│     🔓 Usa chave AES + IV                           │
│                                                     │
│  4. Verifica autenticidade                          │
│     4.1 Calcula hash local                          │
│     4.2 Verifica assinatura                         │
│     ✅ Hashes iguais = Válido!                      │
│                                                     │
│  🎉 MENSAGEM AUTÊNTICA E ÍNTEGRA!                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 15: Demonstração Prática**
```
┌─────────────────────────────────────────────────────┐
│  DEMONSTRAÇÃO PRÁTICA                               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  💻 Vamos executar o sistema!                       │
│                                                     │
│  🎬 O que veremos:                                   │
│                                                     │
│     • Preparação (CA, Alice, Bob)                   │
│     • Envio da mensagem                             │
│     • Visualização do pacote                        │
│     • Recebimento e verificação                     │
│     • Confirmação de segurança                      │
│                                                     │
│  [ESPAÇO PARA TERMINAL / SCREENSHOT]                │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 16: Resultados Obtidos**
```
┌─────────────────────────────────────────────────────┐
│  RESULTADOS OBTIDOS                                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ✅ CONFIDENCIALIDADE                               │
│     → AES-256-CBC + RSA-OAEP                        │
│     → Só Bob pode ler                               │
│                                                     │
│  ✅ INTEGRIDADE                                     │
│     → SHA-256 + Assinatura Digital                  │
│     → Detecta qualquer alteração                    │
│                                                     │
│  ✅ AUTENTICIDADE                                   │
│     → RSA-PSS + Certificado X.509                   │
│     → Prova que veio de Alice                       │
│                                                     │
│  ✅ DETECÇÃO DE ADULTERAÇÃO                         │
│     → Sistema acusa erro imediatamente              │
│                                                     │
│  🎯 Todos os objetivos alcançados!                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 17: Tecnologias**
```
┌─────────────────────────────────────────────────────┐
│  TECNOLOGIAS UTILIZADAS                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  🐍 Python 3                                         │
│     Linguagem de programação                        │
│                                                     │
│  📦 cryptography                                     │
│     Biblioteca padrão da indústria                  │
│                                                     │
│  🔐 Padrões de Segurança:                            │
│     • RSA 2048 bits                                 │
│     • AES 256 bits                                  │
│     • SHA-256                                       │
│     • Padding OAEP e PSS                            │
│     • IV aleatório                                  │
│                                                     │
│  ✅ Segue melhores práticas atuais                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 18: Aplicações Reais**
```
┌─────────────────────────────────────────────────────┐
│  APLICAÇÕES NO MUNDO REAL                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  🌐 HTTPS/TLS                                        │
│     Navegação web segura                            │
│                                                     │
│  💬 WhatsApp, Signal                                 │
│     Mensagens instantâneas                          │
│                                                     │
│  📧 PGP/GPG                                          │
│     E-mail criptografado                            │
│                                                     │
│  🔒 VPN                                              │
│     Redes privadas virtuais                         │
│                                                     │
│  🖥️  SSH                                             │
│     Acesso remoto seguro                            │
│                                                     │
│  ⛓️  Blockchain                                      │
│     Assinaturas de transações                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 19: Conclusões**
```
┌─────────────────────────────────────────────────────┐
│  CONCLUSÕES                                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1️⃣  Criptografia moderna combina                   │
│     múltiplos algoritmos                            │
│                                                     │
│  2️⃣  Cada algoritmo resolve um                      │
│     problema específico                             │
│                                                     │
│  3️⃣  Juntos formam sistema robusto                  │
│     e seguro                                        │
│                                                     │
│  4️⃣  Conceitos aplicados diariamente                │
│     (HTTPS, apps, VPN...)                           │
│                                                     │
│  5️⃣  Segurança é em camadas                         │
│     (Defense in Depth)                              │
│                                                     │
│  ✨ Sistema atende todos os requisitos!             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### **SLIDE 20: Obrigado / Perguntas**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│                                                     │
│              MUITO OBRIGADO!                        │
│                                                     │
│                     🔐                              │
│                                                     │
│              Perguntas?                             │
│                                                     │
│                                                     │
│     [Seus nomes e contatos]                         │
│     [GitHub do projeto]                             │
│                                                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎨 DICAS DE DESIGN

### **Paleta de Cores Sugerida:**
- **Azul escuro**: Títulos e destaques (#1E3A8A)
- **Verde**: Sucesso e válido (#10B981)
- **Vermelho**: Erro e inválido (#EF4444)
- **Amarelo**: Avisos e atenção (#F59E0B)
- **Cinza**: Texto regular (#6B7280)
- **Branco/Claro**: Fundo (#FFFFFF)

### **Fontes:**
- **Títulos**: Arial Bold ou Calibri Bold (28-36pt)
- **Subtítulos**: Arial ou Calibri (20-24pt)
- **Texto**: Arial ou Calibri (16-18pt)
- **Código**: Consolas ou Courier New (14-16pt)

### **Ícones:**
Usar emojis ou ícones profissionais:
- 🔒 🔐 🔑 🔓 - Segurança/Criptografia
- ✅ ❌ ⚠️ - Status
- 📧 📦 📜 - Documentos
- 👤 👥 🏛️ - Pessoas/Autoridade
- 💬 📱 🌐 - Comunicação

### **Animações (se houver tempo):**
- Entrada: Fade In ou Wipe
- Transição: Smooth/Dissolve
- Não exagerar: Máximo 2-3 efeitos por slide

---

## 📝 EXTRAS PARA OS SLIDES

### **Slide Extra: Comparação Antes/Depois**
```
┌─────────────────────────────────────────────────────┐
│  SEM CRIPTOGRAFIA vs COM CRIPTOGRAFIA               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ❌ SEM:                    ✅ COM:                  │
│                                                     │
│  Texto visível              Texto ilegível          │
│  Qualquer um lê             Só destinatário lê      │
│  Fácil alterar              Alteração detectada     │
│  Sem garantia origem        Origem provada          │
│  Impostor possível          Impostor impossível     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### **Slide Extra: Por que Híbrido?**
```
┌─────────────────────────────────────────────────────┐
│  POR QUE CRIPTOGRAFIA HÍBRIDA?                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  PROBLEMA: RSA é lento (~1000x)                     │
│                                                     │
│  SOLUÇÃO:                                           │
│                                                     │
│  AES             ←  Mensagem (grande)               │
│  (Rápido)            "Encontro às 15h..."           │
│                                                     │
│  RSA             ←  Chave AES (32 bytes)            │
│  (Seguro)            a3f7c9e1...                    │
│                                                     │
│  💡 Melhor dos dois mundos!                         │
│     Velocidade (AES) + Segurança (RSA)              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ CHECKLIST PARA OS SLIDES

- [ ] Todos os slides numerados
- [ ] Logo UTFPR em rodapé
- [ ] Fontes legíveis (mínimo 16pt)
- [ ] Cores contrastantes
- [ ] Máximo 7 linhas por slide
- [ ] Imagens/diagramas em alta resolução
- [ ] Animações moderadas
- [ ] Verificação ortográfica
- [ ] Backup em PDF
- [ ] Testado no projetor

**SUCESSO NA APRESENTAÇÃO! 🎉**

