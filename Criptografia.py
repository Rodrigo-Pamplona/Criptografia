import random
import string

#Declarando funções 

# Função para criptografar

def criptografar(Texto, Chave):
    Criptografado = []
    for aux in range(len(Texto)):
        Criptografado.append(Texto[aux] ^ Chave[aux % len(Chave)])
    return bytes(Criptografado)

# Função para gerar uma Chave aleatoria e associar com uma Chave 'string'

def CriarChaveAleatoria(NomeChave):
    RandomKey = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    Chaves[NomeChave] = RandomKey.encode('utf-8')
    SalvarChaves()

# Função que gera e salva as Chaves em um arquivo '.txt'

def SalvarChaves():
    with open("Chaves.txt", "w") as Arquivo:
        for ChaveNome, Chave in Chaves.items():
            Arquivo.write(f"{ChaveNome}:{Chave.hex()}\n")

# Função para verificar a Chave

def BuscarChave(NomeChave):
    if NomeChave in Chaves:
        return Chaves[NomeChave]
    try:
        return bytes.fromhex(NomeChave)
    except ValueError:
        return None

# Dicionario criado para armazenar as Chaves

Chaves = {}

# Abrindo o arquivo para verificar se a Chave existe
try:
    with open("Chaves.txt", "r") as Arquivo:
        Linhas = Arquivo.readlines()
        for Linha in Linhas:
            Partes = Linha.strip().split(":")
            if len(Partes) == 2:
                ChaveNome, Chave = Partes
                Chaves[ChaveNome] = bytes.fromhex(Chave)
except FileNotFoundError:
    pass

# fim do meu declare

# Aqui começa o programa

while True:
    print("\nOpções:")
    print("1. Criptografar")
    print("2. Criar Chave Aleatória")
    print("3. Sair")

    Opcao = input("Escolha uma opção: ")

    if Opcao == '1':
        ChaveNome = input("Nome da Chave ou Chave hexadecimal: ")
        Chave = BuscarChave(ChaveNome)

        if Chave:
            Mensagem = input("Insira a frase que deseja criptografar: ")
            if Mensagem:
                MensagemBytes = Mensagem.encode('utf-8')
                MensagemCifrada = criptografar(MensagemBytes, Chave)
                print("Frase criptografada:", MensagemCifrada.hex())
            else:
                print("Nenhuma frase inserida. Operação de criptografia cancelada.")
        else:
            print("Chave não encontrada ou inválida.")
    elif Opcao == '2':
        ChaveNome = input("Nome da nova Chave: ")
        if ChaveNome not in Chaves:
            CriarChaveAleatoria(ChaveNome)
            print("Chave aleatória gerada e associada a", ChaveNome)
        else:
            print("Já existe uma Chave com esse nome.")
    elif Opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
