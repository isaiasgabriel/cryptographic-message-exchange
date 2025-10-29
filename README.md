# Sistema de Comunicação Segura - Alice e Bob

Implementação de um sistema de comunicação segura que demonstra:
- Hash (SHA-256)
- Criptografia simétrica (AES)
- Criptografia assimétrica (RSA)
- Assinatura digital
- Certificados digitais

## Instalação

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate

# Verificar se está funcionando
which python3
which pip3

# Instalar dependências automaticamente
pip install -r requirements.txt

# Executar o programa
python3 message.py
```

## Verificação da instalação

Para verificar se os pacotes foram instalados corretamente:

```bash
pip list | grep -E "cryptography|colorama"
```

## Desativar ambiente virtual

```bash
deactivate
```