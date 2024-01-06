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
INIT_PC = 0  # armazena o endereco inicial das instrucoes

# CICLO DA INSTRUCAO
def busca():
    global PC, MAR, MBR, MEMORIA
    MAR = PC
    MBR = MEMORIA[MAR]

def decodificacao():
    global MBR, IR, MAR, PC

    enderecos_identificados = identificarEnderecos()

    instrucao = MEMORIA[PC]

    if '(' in instrucao and ')' in instrucao:
        instrucao_completa = instrucao.split('(')[0]
        IR = instrucao_completa.strip()
        
        endereco = int(instrucao.split("(")[1].split(")")[0])
        MAR = endereco
    else:
        IR = instrucao.strip()
        MAR = "NONE" 

def busca_dos_operandos():
    global MBR, MAR, MEMORIA

    if isinstance(MAR, int):  # Verifica se MAR é um número inteiro
        MBR = MEMORIA[MAR]
    else:
        print("Instrução sem endereço associado")

def execucao():
    global IR, MAR, PC, AC, MEMORIA, MBR, MQ

    print(f"IR: {IR}")
    print(f"AC: {AC}")
    print(f"MAR: {MAR}")
    print(f"PC after JUMP: {PC}\n")

    if IR == "JUMP M":  # JUMP M(X)
        print(MAR)
        endereco = int(MAR)
        print(endereco)
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

def print_memoria_dados(linha_inicio):
    global MEMORIA

    print("***** MEMORIA *****\n")
    for i, valor in enumerate(MEMORIA[:linha_inicio]):
        print(f"{i}\t{valor}")

def print_instrucoes(instrucoes):
    print("\n***** INSTRUCOES *****\n")
    for instrucao in instrucoes:
        print(instrucao)
   
def identificarEnderecos():
    global MEMORIA
    enderecos_identificados = []

    for instrucao in MEMORIA:
        if isinstance(instrucao, str):  # Verifica se é uma string
            partes = instrucao.split()
            for parte in partes[1:]:
                parte_limpa = parte.replace(" ", "")  # Remover espaços em branco
                # Se a parte contiver informações sobre um endereço, vamos identificá-lo
                if any(separador in parte_limpa for separador in ('M(', '|M(', '-M(', 'MQ,M(')):
                    endereco = parte_limpa.split('(')[-1].split(')')[0].split(',')[0].split(':')[0]
                    enderecos_identificados.append(endereco)
                elif '+M' in parte_limpa:  # Verifica a instrução JUMP +M(X)
                    endereco = parte_limpa.split('+M(')[-1].split(')')[0]
                    enderecos_identificados.append(endereco)
                elif 'MQ' in parte_limpa:
                    endereco = 'nulo'    
                    
    return enderecos_identificados

# INICIO
nome_arquivo = sys.argv[1]
linha_inicio = int(sys.argv[2])

MEMORIA = carga_memoria(nome_arquivo)
inicia_PC(linha_inicio)

print("\n", MEMORIA, "\n")

processador()

print("\n", MEMORIA, "\n")

print_memoria_dados(linha_inicio)
print_instrucoes(MEMORIA[linha_inicio:])
