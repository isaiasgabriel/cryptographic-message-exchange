# 🔐 Explicação do Fluxo de Assinaturas e Criptografia

## 📋 Visão Geral dos Algoritmos Usados

Este sistema usa **4 algoritmos criptográficos diferentes**, cada um com uma função específica:

| Algoritmo | Tipo | Uso Principal | Onde é usado |
|-----------|------|---------------|--------------|
| **RSA** | Assimétrico | Criptografia de chave + Assinatura | Proteger chave AES + Assinar hash |
| **AES** | Simétrico | Criptografia rápida | Criptografar mensagem |
| **SHA-256** | Hash | Resumo de dados | Criar "impressão digital" da mensagem |
| **X.509** | Certificado | Identidade | Provar quem é quem |

---

## 🎯 Por que tantos algoritmos?

Cada um resolve um problema específico:

### 1. **RSA** - Lento mas versátil
- ✅ Pode criptografar com chave pública, descriptografar com privada
- ✅ Pode assinar com chave privada, verificar com pública
- ❌ Muito lento para mensagens grandes
- 🎯 **Solução**: Use apenas para dados pequenos (chaves e assinaturas)

### 2. **AES** - Rápido mas precisa de chave compartilhada
- ✅ Muito rápido para criptografar grandes quantidades de dados
- ❌ Problema: Como compartilhar a chave com segurança?
- 🎯 **Solução**: Use RSA para enviar a chave AES!

### 3. **SHA-256** - Cria "impressão digital"
- ✅ Transforma qualquer mensagem em hash de tamanho fixo (32 bytes)
- ✅ Impossível reverter (não dá pra descobrir a mensagem pelo hash)
- ✅ Qualquer alteração mínima gera hash totalmente diferente
- 🎯 **Solução**: Use para verificar integridade sem enviar a mensagem toda

### 4. **X.509** - Certificado de identidade
- ✅ Liga uma chave pública a uma identidade (nome)
- ✅ Assinado pela CA (autoridade confiável)
- 🎯 **Solução**: Evita ataques "man-in-the-middle"

---

## 📤 FLUXO COMPLETO: Alice envia mensagem para Bob

### **PREPARAÇÃO (Fase 0) - Acontece uma vez**

```
┌─────────────────────────────────────────────────────────────┐
│ 🏛️  AUTORIDADE CERTIFICADORA (CA)                           │
├─────────────────────────────────────────────────────────────┤
│ 1. CA gera seu próprio par RSA:                             │
│    • Chave Privada CA (guarda em segredo)                   │
│    • Chave Pública CA (todo mundo conhece)                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 👤 ALICE                                                    │
├─────────────────────────────────────────────────────────────┤
│ 1. Alice gera seu par RSA:                                  │
│    • Chave Privada Alice (só ela tem)                       │
│    • Chave Pública Alice                                    │
│                                                             │
│ 2. Alice pede certificado à CA:                             │
│    CA cria documento:                                       │
│    ┌──────────────────────────────────────┐                 │
│    │ CERTIFICADO DE ALICE                 │                 │
│    │ • Nome: Alice                        │                 │
│    │ • Chave Pública: [chave de Alice]    │                 │
│    │ • Assinado por: CA ✍️                │                 │
│    └──────────────────────────────────────┘                 │
│    (CA assina com sua Chave Privada)                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 👤 BOB (faz o mesmo)                                        │
├─────────────────────────────────────────────────────────────┤
│ 1. Bob gera seu par RSA                                     │
│ 2. Bob recebe certificado da CA                             │
└─────────────────────────────────────────────────────────────┘
```

---

### **FASE 1: Alice Envia Mensagem "Encontro às 15h"**

#### **Passo 1: Verificar identidade de Bob** 🔍
```
Alice tem certificado de Bob
    ↓
Usa Chave Pública da CA para verificar assinatura
    ↓
✅ Assinatura válida = Bob é realmente Bob
```

**Algoritmo usado**: RSA (verificação de assinatura)

---

#### **Passo 2: Gerar chave de sessão AES** 🔑
```
Alice gera chave aleatória de 32 bytes
Exemplo: a3f7c9e1... (256 bits)
```

**Algoritmo usado**: AES-256

**Por quê?** AES é rápido para criptografar a mensagem completa.

---

#### **Passo 3: Criptografar a mensagem com AES** 🔒
```
Mensagem original:   "Encontro às 15h"
        ↓
    [AES-CBC com chave de sessão + IV]
        ↓
Texto criptografado: 9ca662772487fe25bef6651fc0cdfe69...
```

**Algoritmos usados**: 
- **AES-256-CBC**: Criptografia simétrica
- **IV** (Vetor de Inicialização): Aleatoriedade extra

**Por quê IV?** Mesmo mensagem idêntica terá texto cifrado diferente a cada vez.

---

#### **Passo 4: Criptografar chave AES com RSA** 🔐
```
Problema: Como Bob vai saber a chave AES?
Solução: Criptografar com a chave PÚBLICA de Bob!

Chave AES (32 bytes): a3f7c9e1...
        ↓
    [RSA-OAEP com Chave Pública de Bob]
        ↓
Chave AES criptografada (256 bytes): 3eccf0caa763eb8e...
```

**Algoritmo usado**: RSA-OAEP (Optimal Asymmetric Encryption Padding)

**Por quê OAEP?** Adiciona padding seguro para evitar ataques.

**Importante**: Só Bob pode descriptografar (só ele tem a chave privada de Bob)!

---

#### **Passo 5: Calcular hash da mensagem** #️⃣
```
Mensagem: "Encontro às 15h"
        ↓
    [SHA-256]
        ↓
Hash: 0691cf24352a2018a46187aa6c56e662682cb9d5bc955321e1e3f539d7941521
```

**Algoritmo usado**: SHA-256

**Por quê?** 
- Hash de 32 bytes é muito menor que a mensagem
- Qualquer alteração na mensagem → hash completamente diferente

---

#### **Passo 6: Assinar o hash** ✍️
```
Problema: Como Bob sabe que foi ALICE quem enviou?
Solução: Alice assina o hash com sua chave PRIVADA!

Hash: 0691cf24352a2018a46187aa6c56e662...
        ↓
    [RSA-PSS com Chave Privada de Alice]
        ↓
Assinatura: 1c28da342ec6e497d0d38f02ebe1ca5f...
```

**Algoritmo usado**: RSA-PSS (Probabilistic Signature Scheme)

**Por quê PSS?** Adiciona salt aleatório para segurança extra.

**Importante**: 
- Só Alice pode criar esta assinatura (só ela tem chave privada de Alice)
- Qualquer um pode VERIFICAR usando chave pública de Alice

---

#### **Passo 7: Montar o pacote** 📦
```
┌──────────────────────────────────────────────────────────┐
│ PACOTE FINAL                                             │
├──────────────────────────────────────────────────────────┤
│ 1. Mensagem criptografada (AES)                          │
│    → 9ca662772487fe25bef6651fc0cdfe69...                 │
│                                                          │
│ 2. IV (necessário para descriptografar AES)              │
│    → e3eda069b3a69eb4c7c6f278bb23fb90                    │
│                                                          │
│ 3. Chave AES criptografada (RSA com chave pública Bob)   │
│    → 3eccf0caa763eb8e57f266578b8bfbe6...                 │
│                                                          │
│ 4. Assinatura do hash (RSA com chave privada Alice)      │
│    → 1c28da342ec6e497d0d38f02ebe1ca5f...                 │
│                                                          │
│ 5. Certificado de Alice (prova identidade)               │
│    → [Certificado X.509 assinado pela CA]                │
└──────────────────────────────────────────────────────────┘
```

---

## 📥 FASE 2: Bob Recebe o Pacote

#### **Passo 1: Verificar certificado de Alice** 🔍
```
Bob pega certificado do pacote
    ↓
Usa Chave Pública da CA
    ↓
Verifica assinatura do certificado
    ↓
✅ Certificado válido = mensagem é de Alice
```

**Algoritmo usado**: RSA (verificação)

---

#### **Passo 2: Descriptografar chave AES** 🔓
```
Chave AES criptografada: 3eccf0caa763eb8e...
        ↓
    [RSA-OAEP com Chave PRIVADA de Bob]
        ↓
Chave AES recuperada: a3f7c9e1...
```

**Algoritmo usado**: RSA-OAEP

**Importante**: Só Bob consegue fazer isso (só ele tem chave privada de Bob)!

---

#### **Passo 3: Descriptografar mensagem** 🔓
```
Mensagem criptografada: 9ca662772487fe25...
        ↓
    [AES-CBC com chave de sessão + IV]
        ↓
Mensagem original: "Encontro às 15h"
```

**Algoritmo usado**: AES-256-CBC

---

#### **Passo 4: Verificar integridade e autenticidade** ✅

##### **4.1: Calcular hash local**
```
Mensagem descriptografada: "Encontro às 15h"
        ↓
    [SHA-256]
        ↓
Hash local: 0691cf24352a2018a46187aa6c56e662...
```

##### **4.2: Verificar assinatura**
```
Bob tem:
  • Assinatura (do pacote)
  • Hash local (calculado agora)
  • Chave Pública de Alice (do certificado)

        ↓
    [RSA-PSS: verificar assinatura]
        ↓
    Compara hash da assinatura com hash local
        ↓
✅ Hashes iguais = mensagem autêntica e íntegra!
```

**Algoritmo usado**: RSA-PSS (verificação)

**O que isso prova?**
- ✅ Mensagem veio de Alice (só ela poderia assinar com chave privada dela)
- ✅ Mensagem não foi alterada (hash continua igual)

---

## 🎯 Resumo: Quem faz o quê?

### **AES (Criptografia Simétrica)**
```
┌─────────────────────────────────────┐
│ Protege o CONTEÚDO da mensagem      │
│ • Rápido                            │
│ • Mesma chave para cifrar/decifrar  │
└─────────────────────────────────────┘
```

### **RSA (Criptografia Assimétrica)**
```
┌─────────────────────────────────────┐
│ Duas funções:                       │
│                                     │
│ 1. CRIPTOGRAFAR chave AES           │
│    • Cifra: chave pública           │
│    • Decifra: chave privada         │
│                                     │
│ 2. ASSINAR/VERIFICAR                │
│    • Assinar: chave privada         │
│    • Verificar: chave pública       │
└─────────────────────────────────────┘
```

### **SHA-256 (Hash)**
```
┌─────────────────────────────────────┐
│ Cria "impressão digital"            │
│ • Tamanho fixo (32 bytes)           │
│ • Irreversível                      │
│ • Detecta alterações                │
└─────────────────────────────────────┘
```

### **X.509 (Certificado)**
```
┌─────────────────────────────────────┐
│ Prova identidade                    │
│ • Liga chave pública → pessoa       │
│ • Assinado pela CA                  │
│ • Evita impostor                    │
└─────────────────────────────────────┘
```

---

## 🛡️ Propriedades de Segurança Alcançadas

### 1. **Confidencialidade** 🔒
- Mensagem criptografada com AES
- Chave AES criptografada com RSA
- **Só Bob pode ler** (precisa da chave privada dele)

### 2. **Autenticidade** ✍️
- Assinatura digital com chave privada de Alice
- **Prova que foi Alice quem enviou**

### 3. **Integridade** ✅
- Hash SHA-256 da mensagem
- Assinado digitalmente
- **Qualquer alteração é detectada**

### 4. **Não-repúdio** 📝
- Alice não pode negar que enviou
- **Assinatura digital é prova**

---

## 🔄 Fluxo Simplificado (Analogia)

Imagine que Alice quer enviar uma **carta secreta** para Bob:

### **Fase de Preparação**
```
🏛️  Cartório (CA):
    "Eu certifico que esta chave pertence a Bob" ✍️

👤 Alice e Bob vão ao cartório e pegam certificados
```

### **Alice Enviando**
```
1. 📝 Alice escreve: "Encontro às 15h"

2. 🔐 Coloca em cofre trancado com cadeado AES
   (Rápido de trancar)

3. 🔑 Pega a chave do cadeado AES
   Coloca dentro de outro cofre trancado com chave pública de Bob
   (Só Bob pode abrir com sua chave privada)

4. 📋 Tira foto da carta (hash)
   Assina a foto com sua assinatura pessoal
   (Prova que é ela e que não foi alterado)

5. 📜 Anexa seu certificado do cartório
   (Prova que a assinatura é dela mesmo)

6. 📦 Envia tudo para Bob
```

### **Bob Recebendo**
```
1. 🔍 Verifica certificado de Alice no cartório
   ✅ "Sim, essa assinatura é de Alice"

2. 🔓 Abre cofre da chave AES
   (Usa sua chave privada - só ele tem)

3. 🔓 Usa chave AES para abrir cofre da mensagem
   Lê: "Encontro às 15h"

4. 📋 Tira foto da carta recebida (hash)
   Compara com a foto assinada por Alice
   ✅ "Idênticas! Não foi alterado!"

5. ✅ Mensagem autêntica, íntegra e confidencial!
```

---

## ❓ Perguntas Frequentes

### **P: Por que não usar só RSA?**
**R:** RSA é muito lento para mensagens grandes. AES é 1000x mais rápido!

### **P: Por que assinar o hash e não a mensagem?**
**R:** Hash é pequeno (32 bytes). Assinar é mais rápido e eficiente.

### **P: O que acontece se um hacker interceptar o pacote?**
**R:** 
- ❌ Não consegue ler (mensagem criptografada com AES)
- ❌ Não consegue pegar chave AES (criptografada com chave pública de Bob)
- ❌ Não consegue alterar (hash + assinatura detectam)
- ❌ Não consegue se passar por Alice (não tem chave privada dela)

### **P: Alguém pode se passar por Bob?**
**R:** Não! Só o Bob real consegue descriptografar a chave AES (precisa da chave privada de Bob).

### **P: A CA pode ler as mensagens?**
**R:** Não! A CA só certifica identidades. Ela não participa da criptografia das mensagens.

---

## 🎓 Conclusão

Este sistema combina o **melhor de cada algoritmo**:

- **AES**: Velocidade (criptografia de dados)
- **RSA**: Flexibilidade (troca de chaves + assinatura)  
- **SHA-256**: Integridade (detecta alterações)
- **X.509**: Confiança (prova de identidade)

Juntos, eles criam um sistema de comunicação **seguro, autêntico e confiável**! 🔐✨

