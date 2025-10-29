from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
import os
import json
import datetime
from colorama import init, Fore, Style

# Inicializa colorama para cores no terminal
init(autoreset=True)

class AutoridadeCertificadora:
    """Autoridade Certificadora (CA) - Emite e valida certificados"""
    
    def __init__(self):
        print(f"\n{Fore.YELLOW}{'='*70}")
        print(f"{Fore.YELLOW}🏛️  AUTORIDADE CERTIFICADORA (CA) - Inicializando")
        print(f"{Fore.YELLOW}{'='*70}")
        
        # Gera par de chaves RSA da CA
        self.chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.chave_publica = self.chave_privada.public_key()
        print(f"{Fore.GREEN}✅ Par de chaves RSA da CA gerado com sucesso!")
        
    def emitir_certificado(self, nome, chave_publica_usuario):
        """Emite um certificado digital para um usuário"""
        print(f"\n{Fore.CYAN}📜 CA emitindo certificado para: {nome}")
        
        # Cria o certificado
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Paraná"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Dois Vizinhos"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UTFPR"),
            x509.NameAttribute(NameOID.COMMON_NAME, nome),
        ])
        
        certificado = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            chave_publica_usuario
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=365)
        ).sign(self.chave_privada, hashes.SHA256(), default_backend())
        
        print(f"{Fore.GREEN}✅ Certificado digital emitido para {nome}!")
        return certificado
    
    def verificar_certificado(self, certificado):
        """Verifica a validade de um certificado"""
        try:
            # Verifica a assinatura do certificado usando a chave pública da CA
            self.chave_publica.verify(
                certificado.signature,
                certificado.tbs_certificate_bytes,
                padding.PKCS1v15(),
                certificado.signature_hash_algorithm
            )
            return True
        except:
            return False


class Usuario:
    """Classe base para Alice e Bob"""
    
    def __init__(self, nome, ca):
        self.nome = nome
        self.ca = ca
        
        print(f"\n{Fore.MAGENTA}{'='*70}")
        print(f"{Fore.MAGENTA}👤 {nome} - Inicializando")
        print(f"{Fore.MAGENTA}{'='*70}")
        
        # Gera par de chaves RSA
        print(f"{Fore.CYAN}🔑 Gerando par de chaves RSA para {nome}...")
        self.chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.chave_publica = self.chave_privada.public_key()
        print(f"{Fore.GREEN}✅ Par de chaves gerado!")
        
        # Solicita certificado à CA
        self.certificado = ca.emitir_certificado(nome, self.chave_publica)
        
    def calcular_hash(self, mensagem):
        """Calcula o hash SHA-256 de uma mensagem"""
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(mensagem.encode())
        return digest.finalize()


class Alice(Usuario):
    """Alice - Remetente da mensagem"""
    
    def enviar_mensagem(self, mensagem_texto, bob):
        print(f"\n{Fore.YELLOW}{'='*70}")
        print(f"{Fore.YELLOW}📤 FASE 1: ALICE ENVIA MENSAGEM")
        print(f"{Fore.YELLOW}{'='*70}")
        
        print(f"\n{Fore.WHITE}💬 Mensagem original: \"{mensagem_texto}\"")
        
        # 1. Verificar o certificado de Bob
        print(f"\n{Fore.CYAN}🔍 Passo 1: Verificando certificado de Bob...")
        if not self.ca.verificar_certificado(bob.certificado):
            print(f"{Fore.RED}❌ ERRO: Certificado de Bob inválido!")
            return None
        print(f"{Fore.GREEN}✅ Certificado de Bob verificado com sucesso!")
        
        # Extrai a chave pública de Bob do certificado
        chave_publica_bob = bob.certificado.public_key()
        
        # 2. Gerar chave de sessão AES
        print(f"\n{Fore.CYAN}🔑 Passo 2: Gerando chave de sessão AES...")
        chave_sessao = os.urandom(32)  # 256 bits
        print(f"{Fore.GREEN}✅ Chave de sessão gerada: {chave_sessao.hex()[:40]}...")
        
        # 3. Criptografar mensagem com AES
        print(f"\n{Fore.CYAN}🔒 Passo 3: Criptografando mensagem com AES...")
        iv = os.urandom(16)  # Vetor de inicialização
        cipher = Cipher(
            algorithms.AES(chave_sessao),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Padding da mensagem
        mensagem_bytes = mensagem_texto.encode()
        padding_length = 16 - (len(mensagem_bytes) % 16)
        mensagem_padded = mensagem_bytes + bytes([padding_length] * padding_length)
        
        mensagem_criptografada = encryptor.update(mensagem_padded) + encryptor.finalize()
        print(f"{Fore.GREEN}✅ Mensagem criptografada: {mensagem_criptografada.hex()[:40]}...")
        
        # 4. Criptografar chave de sessão com RSA (chave pública de Bob)
        print(f"\n{Fore.CYAN}🔐 Passo 4: Criptografando chave de sessão com RSA...")
        chave_sessao_criptografada = chave_publica_bob.encrypt(
            chave_sessao,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print(f"{Fore.GREEN}✅ Chave de sessão criptografada com chave pública de Bob!")
        
        # 5. Calcular hash da mensagem original
        print(f"\n{Fore.CYAN}# Passo 5: Calculando hash SHA-256 da mensagem...")
        hash_mensagem = self.calcular_hash(mensagem_texto)
        print(f"{Fore.GREEN}✅ Hash calculado: {hash_mensagem.hex()}")
        
        # 6. Assinar o hash com chave privada de Alice
        print(f"\n{Fore.CYAN}✍️  Passo 6: Assinando hash com chave privada de Alice...")
        assinatura = self.chave_privada.sign(
            hash_mensagem,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print(f"{Fore.GREEN}✅ Assinatura digital criada!")
        
        # 7. Montar o pacote
        print(f"\n{Fore.CYAN}📦 Passo 7: Montando pacote seguro...")
        pacote = {
            'mensagem_criptografada': mensagem_criptografada,
            'iv': iv,
            'chave_sessao_criptografada': chave_sessao_criptografada,
            'assinatura': assinatura,
            'certificado_remetente': self.certificado
        }
        
        print(f"{Fore.GREEN}✅ Pacote montado e pronto para envio!")
        print(f"\n{Fore.YELLOW}📨 Pacote contém:")
        print(f"{Fore.WHITE}   • Mensagem criptografada (AES)")
        print(f"{Fore.WHITE}   • Chave de sessão criptografada (RSA)")
        print(f"{Fore.WHITE}   • Assinatura digital")
        print(f"{Fore.WHITE}   • Certificado de Alice")
        
        return pacote


class Bob(Usuario):
    """Bob - Destinatário da mensagem"""
    
    def receber_mensagem(self, pacote):
        print(f"\n{Fore.YELLOW}{'='*70}")
        print(f"{Fore.YELLOW}📥 FASE 2: BOB RECEBE MENSAGEM")
        print(f"{Fore.YELLOW}{'='*70}")
        
        # 1. Verificar certificado de Alice
        print(f"\n{Fore.CYAN}🔍 Passo 1: Verificando certificado de Alice...")
        certificado_alice = pacote['certificado_remetente']
        
        if not self.ca.verificar_certificado(certificado_alice):
            print(f"{Fore.RED}❌ ERRO: Certificado de Alice inválido!")
            return None
        
        print(f"{Fore.GREEN}✅ Certificado de Alice verificado!")
        chave_publica_alice = certificado_alice.public_key()
        
        # 2. Descriptografar chave de sessão
        print(f"\n{Fore.CYAN}🔓 Passo 2: Descriptografando chave de sessão com chave privada de Bob...")
        chave_sessao = self.chave_privada.decrypt(
            pacote['chave_sessao_criptografada'],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print(f"{Fore.GREEN}✅ Chave de sessão recuperada: {chave_sessao.hex()[:40]}...")
        
        # 3. Descriptografar mensagem
        print(f"\n{Fore.CYAN}🔓 Passo 3: Descriptografando mensagem com AES...")
        cipher = Cipher(
            algorithms.AES(chave_sessao),
            modes.CBC(pacote['iv']),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        mensagem_padded = decryptor.update(pacote['mensagem_criptografada']) + decryptor.finalize()
        
        # Remove padding
        padding_length = mensagem_padded[-1]
        mensagem_descriptografada = mensagem_padded[:-padding_length].decode()
        
        print(f"{Fore.GREEN}✅ Mensagem descriptografada: \"{mensagem_descriptografada}\"")
        
        # 4. Verificar integridade e autenticidade
        print(f"\n{Fore.CYAN}🔍 Passo 4: Verificando integridade e autenticidade...")
        
        # Calcular hash local
        print(f"{Fore.CYAN}   # Calculando hash local da mensagem...")
        hash_local = self.calcular_hash(mensagem_descriptografada)
        print(f"{Fore.WHITE}   Hash local: {hash_local.hex()}")
        
        # Verificar assinatura
        print(f"{Fore.CYAN}   🔍 Verificando assinatura de Alice...")
        try:
            chave_publica_alice.verify(
                pacote['assinatura'],
                hash_local,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            print(f"\n{Fore.GREEN}{'='*70}")
            print(f"{Fore.GREEN}✅ VERIFICAÇÃO BEM-SUCEDIDA!")
            print(f"{Fore.GREEN}{'='*70}")
            print(f"{Fore.GREEN}✅ Confidencialidade: Mensagem protegida (AES/RSA)")
            print(f"{Fore.GREEN}✅ Autenticidade: Mensagem veio de Alice (assinatura válida)")
            print(f"{Fore.GREEN}✅ Integridade: Mensagem não foi alterada (hash corresponde)")
            print(f"{Fore.WHITE}\n💬 Mensagem final: \"{mensagem_descriptografada}\"")
            
            return mensagem_descriptografada
            
        except Exception as e:
            print(f"\n{Fore.RED}{'='*70}")
            print(f"{Fore.RED}❌ FALHA DE SEGURANÇA!")
            print(f"{Fore.RED}{'='*70}")
            print(f"{Fore.RED}❌ A assinatura não corresponde!")
            print(f"{Fore.RED}❌ Mensagem foi adulterada ou enviada por impostor!")
            return None


def main():
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}🔐 SISTEMA DE COMUNICAÇÃO SEGURA - ALICE E BOB")
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.WHITE}Implementa: Hash (SHA-256), AES, RSA, Assinatura e Certificado Digital")
    
    # FASE 0: PREPARAÇÃO
    print(f"\n{Fore.YELLOW}{'='*70}")
    print(f"{Fore.YELLOW}⚙️  FASE 0: PREPARAÇÃO DO SISTEMA")
    print(f"{Fore.YELLOW}{'='*70}")
    
    # Criar Autoridade Certificadora
    ca = AutoridadeCertificadora()
    
    # Criar Alice e Bob
    alice = Alice("Alice", ca)
    bob = Bob("Bob", ca)
    
    print(f"\n{Fore.GREEN}✅ Fase 0 concluída! Sistema preparado.")
    print(f"{Fore.WHITE}   • CA, Alice e Bob possuem seus pares de chaves RSA")
    print(f"{Fore.WHITE}   • Certificados digitais foram emitidos pela CA")
    print(f"{Fore.WHITE}   • Alice e Bob podem trocar mensagens com segurança")
    
    # Mensagem a ser enviada
    mensagem = "Encontro às 15h"
    
    # FASE 1: Alice envia mensagem
    pacote = alice.enviar_mensagem(mensagem, bob)
    
    if pacote:
        # FASE 2: Bob recebe mensagem
        mensagem_recebida = bob.receber_mensagem(pacote)
        
        # Resultado final
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}📊 RESULTADO FINAL")
        print(f"{Fore.CYAN}{'='*70}")
        
        if mensagem_recebida:
            print(f"{Fore.GREEN}✅ Comunicação segura estabelecida com sucesso!")
            print(f"{Fore.WHITE}   Mensagem enviada: \"{mensagem}\"")
            print(f"{Fore.WHITE}   Mensagem recebida: \"{mensagem_recebida}\"")
            print(f"{Fore.GREEN}   Status: VERIFICADO E AUTÊNTICO ✓")
        else:
            print(f"{Fore.RED}❌ Falha na comunicação segura!")
            print(f"{Fore.RED}   A mensagem não pôde ser verificada.")


if __name__ == "__main__":
    main()