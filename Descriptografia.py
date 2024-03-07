
#Declarando funcões 

# Funçaõ de descriptografia

def InputMensagemCifradaHex():
    while True:
        MensagemCifradaHex = input("Insira a frase criptografada em hexadecimal: ")
        if IsHexadecimal(MensagemCifradaHex):
            return MensagemCifradaHex
        else:
            print("O texto inserido não é um valor hexadecimal válido. Tente novamente.")

def IsHexadecimal(texto):
    try:
        bytes.fromhex(texto)
        return True
    except ValueError:
        return False

# No seu loop principal, você pode chamar a função InputMensagemCifradaHex() para obter o texto criptografado em hexadecimal.
# Substitua esta linha:
# MensagemCifradaHex = input("Insira a frase criptografada em hexadecimal: ")

def Descriptografar(Textoriptografado, Chave):
    Descriptografado = []
    for aux in range(len(Textoriptografado)):
        Descriptografado.append(Textoriptografado[aux] ^ Chave[aux % len(Chave)])
    return bytes(Descriptografado)

# Aqui eu verifico o valor da Chave 'string' e mostro seu valro em hexadecimal

def BuscarChave(nome_chave):
    if nome_chave in Chaves:
        return Chaves[nome_chave]
    try:
        return bytes.fromhex(nome_chave)
    except ValueError:
        return None

# As Chaves são mapeadas usando um dicionario python.

Chaves = {}

# Aqui carrega o arquivo gerado no codigo de criptografia.

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

#Fim do meu declare.

# Aqui inicia meu programa.

while True:
    print("\nOpções:")
    print("1. Descriptografar")
    print("2. Verificar Chave")
    print("3. Sair")

    Opcao = input("Escolha uma opção: ")

    if Opcao == '1':
        ChaveNome = input("Nome da Chave ou Chave hexadecimal: ")
        Chave = BuscarChave(ChaveNome)

        if Chave:
            MensagemCifradaHex = InputMensagemCifradaHex()
            MensagemCifrada = bytes.fromhex(MensagemCifradaHex)
            MensagemDecifrada = Descriptografar(MensagemCifrada, Chave)
            MensagemDecifradaStr = MensagemDecifrada.decode('utf-8', errors='ignore')
            print("Frase descriptografada:", MensagemDecifradaStr)
        else:
            print("Chave não encontrada ou inválida.")
    elif Opcao == '2':
        ChaveNome = input("Digite o nome da Chave para verificar: ")
        if ChaveNome in Chaves:
            ChaveBytes = Chaves[ChaveNome]
            print(f"Chave associada a {ChaveNome}: {ChaveBytes.hex()}")
        else:
            print("Chave não encontrada.")
    elif Opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")




