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

class CertificateAuthority:
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
    
    def exibir_chaves(self):
        """Exibe as chaves da CA em formato PEM"""
        print(f"\n{Fore.CYAN}🔑 Chave Privada da CA (PEM):")
        chave_privada_pem = self.chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        print(f"{Fore.WHITE}{chave_privada_pem.decode()}")
        
        print(f"{Fore.CYAN}🔓 Chave Pública da CA (PEM):")
        chave_publica_pem = self.chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(f"{Fore.WHITE}{chave_publica_pem.decode()}")
        
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
            datetime.datetime.now(datetime.UTC)
        ).not_valid_after(
            datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=365)
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


class User:
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
        print(f"{Fore.GREEN}✅ Par de chaves RSA geradas!")
        
        # Solicita certificado à CA
        self.certificado = ca.emitir_certificado(nome, self.chave_publica)
    
    def exibir_chaves(self):
        """Exibe as chaves do usuário em formato PEM"""
        print(f"\n{Fore.CYAN}🔑 Chave Privada de {self.nome} (PEM):")
        chave_privada_pem = self.chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        print(f"{Fore.WHITE}{chave_privada_pem.decode()}")
        
        print(f"{Fore.CYAN}🔓 Chave Pública de {self.nome} (PEM):")
        chave_publica_pem = self.chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(f"{Fore.WHITE}{chave_publica_pem.decode()}")
        
    def calcular_hash(self, mensagem):
        """Calcula o hash SHA-256 de uma mensagem"""
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(mensagem.encode())
        return digest.finalize()
    
    def enviar_mensagem(self, mensagem_texto, destinatario):
        """Envia uma mensagem criptografada para outro usuário"""
        print(f"\n{Fore.YELLOW}{'='*70}")
        print(f"{Fore.YELLOW}📤 FASE 1: {self.nome.upper()} ENVIA MENSAGEM")
        print(f"{Fore.YELLOW}{'='*70}")
        
        print(f"\n{Fore.WHITE}💬 Mensagem original: \"{mensagem_texto}\"")
        
        # 1. Verificar o certificado do destinatário
        print(f"\n{Fore.CYAN}🔍 Passo 1: Verificando certificado de {destinatario.nome}...")
        if not self.ca.verificar_certificado(destinatario.certificado):
            print(f"{Fore.RED}❌ ERRO: Certificado de {destinatario.nome} inválido!")
            return None
        print(f"{Fore.GREEN}✅ Certificado de {destinatario.nome} verificado com sucesso!")
        
        # Extrai a chave pública do destinatário do certificado
        chave_publica_destinatario = destinatario.certificado.public_key()
        
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
        
        # 4. Criptografar chave de sessão com RSA (chave pública do destinatário)
        print(f"\n{Fore.CYAN}🔐 Passo 4: Criptografando chave de sessão com RSA...")
        chave_sessao_criptografada = chave_publica_destinatario.encrypt(
            chave_sessao,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print(f"{Fore.GREEN}✅ Chave de sessão criptografada com chave pública de {destinatario.nome}!")
        
        # 5. Calcular hash da mensagem original
        print(f"\n{Fore.CYAN}# Passo 5: Calculando hash SHA-256 da mensagem...")
        hash_mensagem = self.calcular_hash(mensagem_texto)
        print(f"{Fore.GREEN}✅ Hash calculado: {hash_mensagem.hex()}")
        
        # 6. Assinar o hash com chave privada do remetente
        print(f"\n{Fore.CYAN}✍️  Passo 6: Assinando hash com chave privada de {self.nome}...")
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
        print(f"{Fore.WHITE}   • Certificado de {self.nome}")
        
        # Exibir conteúdo do pacote
        print(f"\n{Fore.CYAN}📋 Visualização do Pacote Montado:")
        print(f"{Fore.YELLOW}{'─'*70}")
        
        print(f"\n{Fore.CYAN}🔒 Mensagem Criptografada (AES-CBC):")
        print(f"{Fore.WHITE}   Tamanho: {len(mensagem_criptografada)} bytes")
        print(f"{Fore.WHITE}   Hex: {mensagem_criptografada.hex()}")
        
        print(f"\n{Fore.CYAN}🎲 IV (Vetor de Inicialização):")
        print(f"{Fore.WHITE}   Tamanho: {len(iv)} bytes")
        print(f"{Fore.WHITE}   Hex: {iv.hex()}")
        
        print(f"\n{Fore.CYAN}🔐 Chave de Sessão Criptografada (RSA-OAEP):")
        print(f"{Fore.WHITE}   Tamanho: {len(chave_sessao_criptografada)} bytes")
        print(f"{Fore.WHITE}   Hex: {chave_sessao_criptografada.hex()}")
        
        print(f"\n{Fore.CYAN}✍️  Assinatura Digital (RSA-PSS):")
        print(f"{Fore.WHITE}   Tamanho: {len(assinatura)} bytes")
        print(f"{Fore.WHITE}   Hex: {assinatura.hex()}")
        
        print(f"\n{Fore.CYAN}📜 Certificado do Remetente ({self.nome}):")
        certificado_pem = self.certificado.public_bytes(serialization.Encoding.PEM)
        print(f"{Fore.WHITE}{certificado_pem.decode()}")
        
        print(f"{Fore.YELLOW}{'─'*70}")
        
        return pacote

    def receber_mensagem(self, pacote):
        """Recebe e descriptografa uma mensagem"""
        print(f"\n{Fore.YELLOW}{'='*70}")
        print(f"{Fore.YELLOW}📥 FASE 2: {self.nome.upper()} RECEBE MENSAGEM")
        print(f"{Fore.YELLOW}{'='*70}")
        
        # ============================================================
        # PASSO 1: Verificar Certificado do Remetente
        # ============================================================
        print(f"\n{Fore.CYAN}{'─'*70}")
        print(f"{Fore.CYAN}🔍 PASSO 1: VERIFICANDO CERTIFICADO DO REMETENTE")
        print(f"{Fore.CYAN}{'─'*70}")
        
        certificado_remetente = pacote['certificado_remetente']
        
        print(f"{Fore.WHITE}📋 O que {self.nome} está fazendo:")
        print(f"{Fore.WHITE}   1. Pega o certificado do pacote recebido")
        print(f"{Fore.WHITE}   2. Usa a chave PÚBLICA da CA para verificar assinatura")
        print(f"{Fore.WHITE}   3. Se válido → certificado foi emitido pela CA confiável")
        
        print(f"\n{Fore.MAGENTA}🔬 Demonstração Técnica:")
        print(f"{Fore.WHITE}   Algoritmo: RSA (verificação de assinatura)")
        print(f"{Fore.WHITE}   Usando: Chave Pública da CA")
        
        if not self.ca.verificar_certificado(certificado_remetente):
            print(f"{Fore.RED}❌ ERRO: Certificado do remetente inválido!")
            return None
        
        # Extrai o nome do remetente do certificado
        nome_remetente = certificado_remetente.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
        print(f"\n{Fore.GREEN}✅ Certificado VÁLIDO!")
        print(f"{Fore.GREEN}   → Remetente identificado: {nome_remetente}")
        print(f"{Fore.GREEN}   → Certificado foi assinado pela CA")
        print(f"{Fore.GREEN}   → Podemos confiar na chave pública de {nome_remetente}")
        
        chave_publica_remetente = certificado_remetente.public_key()
        
        # ============================================================
        # PASSO 2: Descriptografar Chave de Sessão AES
        # ============================================================
        print(f"\n{Fore.CYAN}{'─'*70}")
        print(f"{Fore.CYAN}🔓 PASSO 2: DESCRIPTOGRAFANDO CHAVE DE SESSÃO AES")
        print(f"{Fore.CYAN}{'─'*70}")
        
        print(f"{Fore.WHITE}📋 O que {self.nome} está fazendo:")
        print(f"{Fore.WHITE}   1. Pega chave AES criptografada do pacote")
        print(f"{Fore.WHITE}   2. Usa sua chave PRIVADA RSA para descriptografar")
        print(f"{Fore.WHITE}   3. Recupera a chave AES original")
        
        print(f"\n{Fore.MAGENTA}🔬 Demonstração Técnica:")
        print(f"{Fore.WHITE}   Algoritmo: RSA-OAEP")
        print(f"{Fore.WHITE}   Chave criptografada (256 bytes):")
        print(f"{Fore.WHITE}   {pacote['chave_sessao_criptografada'].hex()[:60]}...")
        print(f"{Fore.WHITE}   Usando: Chave PRIVADA de {self.nome} (só {self.nome} tem!)")
        
        chave_sessao = self.chave_privada.decrypt(
            pacote['chave_sessao_criptografada'],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        print(f"\n{Fore.GREEN}✅ Chave AES RECUPERADA!")
        print(f"{Fore.GREEN}   → Tamanho: {len(chave_sessao)} bytes (256 bits)")
        print(f"{Fore.GREEN}   → Chave: {chave_sessao.hex()[:40]}...")
        print(f"{Fore.GREEN}   → Agora {self.nome} pode descriptografar a mensagem!")
        
        # ============================================================
        # PASSO 3: Descriptografar Mensagem com AES
        # ============================================================
        print(f"\n{Fore.CYAN}{'─'*70}")
        print(f"{Fore.CYAN}🔓 PASSO 3: DESCRIPTOGRAFANDO MENSAGEM COM AES")
        print(f"{Fore.CYAN}{'─'*70}")
        
        print(f"{Fore.WHITE}📋 O que {self.nome} está fazendo:")
        print(f"{Fore.WHITE}   1. Usa a chave AES recuperada no passo 2")
        print(f"{Fore.WHITE}   2. Usa o IV (Vetor de Inicialização) do pacote")
        print(f"{Fore.WHITE}   3. Descriptografa a mensagem com AES-CBC")
        print(f"{Fore.WHITE}   4. Remove o padding")
        
        print(f"\n{Fore.MAGENTA}🔬 Demonstração Técnica:")
        print(f"{Fore.WHITE}   Algoritmo: AES-256-CBC")
        print(f"{Fore.WHITE}   Mensagem criptografada: {pacote['mensagem_criptografada'].hex()[:40]}...")
        print(f"{Fore.WHITE}   IV: {pacote['iv'].hex()}")
        print(f"{Fore.WHITE}   Chave AES: {chave_sessao.hex()[:40]}...")
        
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
        
        print(f"\n{Fore.GREEN}✅ Mensagem DESCRIPTOGRAFADA!")
        print(f"{Fore.GREEN}   → Mensagem original: \"{mensagem_descriptografada}\"")
        print(f"{Fore.GREEN}   → Mas espere! Ainda precisa verificar autenticidade...")
        
        # ============================================================
        # PASSO 4: Verificar Integridade e Autenticidade
        # ============================================================
        print(f"\n{Fore.CYAN}{'─'*70}")
        print(f"{Fore.CYAN}🔍 PASSO 4: VERIFICANDO INTEGRIDADE E AUTENTICIDADE")
        print(f"{Fore.CYAN}{'─'*70}")
        
        print(f"{Fore.WHITE}📋 O que {self.nome} está fazendo:")
        print(f"{Fore.WHITE}   1. Calcula hash SHA-256 da mensagem descriptografada")
        print(f"{Fore.WHITE}   2. Pega a assinatura do pacote (criada por {nome_remetente})")
        print(f"{Fore.WHITE}   3. Usa chave PÚBLICA de {nome_remetente} para verificar")
        print(f"{Fore.WHITE}   4. Compara hash da assinatura com hash local")
        
        # Sub-passo 4.1: Calcular hash local
        print(f"\n{Fore.MAGENTA}🔬 Passo 4.1: Calculando Hash Local")
        print(f"{Fore.WHITE}   Algoritmo: SHA-256")
        print(f"{Fore.WHITE}   Mensagem: \"{mensagem_descriptografada}\"")
        
        hash_local = self.calcular_hash(mensagem_descriptografada)
        
        print(f"{Fore.WHITE}   Hash calculado: {hash_local.hex()}")
        
        # Sub-passo 4.2: Verificar assinatura
        print(f"\n{Fore.MAGENTA}🔬 Passo 4.2: Verificando Assinatura Digital")
        print(f"{Fore.WHITE}   Algoritmo: RSA-PSS (verificação)")
        print(f"{Fore.WHITE}   Assinatura recebida: {pacote['assinatura'].hex()[:60]}...")
        print(f"{Fore.WHITE}   Hash local calculado: {hash_local.hex()}")
        print(f"{Fore.WHITE}   Usando: Chave PÚBLICA de {nome_remetente}")
        
        print(f"\n{Fore.YELLOW}⚙️  Verificando...")
        print(f"{Fore.WHITE}   → RSA descriptografa a assinatura com chave pública")
        print(f"{Fore.WHITE}   → Extrai o hash que estava assinado")
        print(f"{Fore.WHITE}   → Compara com o hash local")
        
        try:
            chave_publica_remetente.verify(
                pacote['assinatura'],
                hash_local,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            print(f"\n{Fore.CYAN}{'─'*70}")
            print(f"{Fore.CYAN}💬 MENSAGEM FINAL VERIFICADA:")
            print(f"{Fore.WHITE}   \"{mensagem_descriptografada}\"")
            print(f"{Fore.CYAN}{'─'*70}")
            
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
    print(f"{Fore.CYAN}🔐 SISTEMA DE COMUNICAÇÃO SEGURA")
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.WHITE}Implementa: Hash (SHA-256), AES, RSA, Assinatura e Certificado Digital")
    
    # FASE 0: PREPARAÇÃO
    print(f"\n{Fore.YELLOW}{'='*70}")
    print(f"{Fore.YELLOW}⚙️  FASE 0: PREPARAÇÃO DO SISTEMA")
    print(f"{Fore.YELLOW}{'='*70}")
    
    # Criar Autoridade Certificadora
    ca = CertificateAuthority()
    ca.exibir_chaves()
    
    # Criar Alice e Bob
    alice = User("Alice", ca)
    alice.exibir_chaves()

    bob = User("Bob", ca)
    bob.exibir_chaves()
    
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