import sys

# MEMORIA
MEMORIA = []

# REGISTRADORES UC
PC = 0
IR = 0
MAR = 0

# REGISTRADORES ULA
MBR = '00000000000000000000'
AC = 0
MQ = 0

# VARIAVEIS AUXILIARES
INIT_PC = 0  # Armazena o endereco inicial das instrucoes.

# CICLO DA INSTRUCAO
def busca():
    global PC, MAR, MBR, MEMORIA
    MAR = PC
    MBR = MEMORIA[MAR]

def decodificacao():
    global MBR, IR, MAR, PC

    if '(' in MBR and ')' in MBR: # Se tiver parênteses no MBR.
        # Pega tudo que tiver antes do '(', e colocar no IR.
        opcode = MBR.split('(')[0] 
        IR = opcode.strip()
        
        # Pega tudo que estiver dentro do '(', ')', e coloca no MAR.
        endereco = int(MBR.split("(")[1].split(")")[0])
        MAR = endereco
    else:
        # Caso contrário se não tiver parênteses, não tem endereço, logo é uma instrução sem endereço associado.
        IR = MBR.strip()
        MAR = "NONE" 

def busca_dos_operandos():
    global MBR, MAR, MEMORIA

    if isinstance(MAR, int):  # Verifica se MAR é um número inteiro.
        MBR = MEMORIA[MAR]
    else:
        print("Instrução sem endereço associado")

def execucao():
    global IR, MAR, PC, AC, MEMORIA, MBR, MQ

    # Printando registradores a cada interação de instrução
    print(f"IR: {IR}")
    print(f"AC: {AC}")
    print(f"MAR: {MAR}")
    print(f"PC depois do JUMP: {PC}\n")

    if IR == "JUMP M":  # JUMP M(X)
        endereco = int(MAR)
        PC = endereco - 1
    elif IR == "JUMP +M": # JUMP +M(X)
        if int(AC) >= 0:  # Verifica se o AC é positivo
            endereco = int(MAR)
            PC = endereco - 1
    elif IR == "LOAD M": # LOAD M(X) 
        AC = MBR
    elif IR == "LOAD |M": # LOAD |M(X)|
        MBR = int(MBR)
        AC = abs(MBR)
    elif IR == "LOAD MQ": # LOAD MQ
        AC = MQ
    elif IR == "LOAD MQ,M": # LOAD MQ, M(X)
        MQ = int(MBR)
    elif IR == "LOAD -M": # LOAD -M(X)
        AC = -MBR
    elif IR == "LOAD -|M": # LOAD -|M(X)|
        MBR = int(MBR)
        AC = -abs(MBR)
    elif IR == "SUB M": # SUB M(X)
        valor_mbr = int(MBR)
        AC = int(AC) - valor_mbr
    elif IR == "ADD M": # ADD M(X)
        AC = int(AC) + int(MBR)    
    elif IR == "MUL M": # MUL M(X)
        multiplicando = int(MEMORIA[MAR])
        multiplicador = MQ

        # Multiplicação considerando 40 bits
        produto = multiplicando * multiplicador
        produto_binario = bin(produto)[2:].zfill(80)

        AC = int(produto_binario[:40], 2)
        MQ = int(produto_binario[40:], 2)
    elif IR == "DIV M": # DIV M(X)
        dividendo = int(AC)
        divisor = int(MEMORIA[MAR])
        # Quociente
        MQ = dividendo // divisor
        # Resto
        AC = dividendo % divisor
    elif IR == "ADD |M": # ADD |M(X)|  
        AC = int(AC) + abs(int(MBR))
    elif IR == "SUB |M": # SUB |M(X)|
        valor_mbr = int(MBR)
        AC = int(AC) - abs(valor_mbr)
    elif IR == "LSH": # LSH
        AC = int(AC) * 2  
    elif IR == "RSH": # RSH
        AC = int(AC) // 2
    elif IR == "STOR M": # STOR M(X) 
        MBR = AC
        MBR = int(MBR)
        MEMORIA[MAR] = MBR

# PROCESSADOR
def processador():
    global PC
    while PC < len(MEMORIA):  # Executa enquanto houver instruções na memória
        print(f"PC: {PC}")
        busca()
        decodificacao()
        busca_dos_operandos()
        execucao()
        PC += 1

# FUNCOES AUXILIARES
def carga_memoria(nome_arquivo):
    with open(nome_arquivo, "r") as fin:
        linhas = fin.readlines()

    conteudo_memoria = [linha.strip() for linha in linhas]
    return conteudo_memoria

def inicia_PC(endereco):
    global PC
    global INIT_PC
    PC = endereco
    INIT_PC = endereco

def print_memoria_dados(linha_inicio): # Função para printar todos os dados da memória no txt
    global MEMORIA

    print("***** MEMORIA *****\n")
    for i, valor in enumerate(MEMORIA[:linha_inicio]):
        print(f"{i}\t{valor}")

def print_instrucoes(instrucoes): # Função para printar todas as instruções da memória no txt
    print("\n***** INSTRUCOES *****\n")
    for instrucao in instrucoes:
        print(instrucao)

# INICIO
nome_arquivo = sys.argv[1]
linha_inicio = int(sys.argv[2])

MEMORIA = carga_memoria(nome_arquivo)
inicia_PC(linha_inicio)

processador()

print_memoria_dados(linha_inicio)
print_instrucoes(MEMORIA[linha_inicio:])

print("\n======================\n")
print("   MEMORIA COMPLETA")
print("\n======================\n")

print(MEMORIA, "\n")