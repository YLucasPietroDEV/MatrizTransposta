# Define uma função para criar uma matriz com o número de linhas e colunas especificado
def criar_matriz(rows, cols):
    matriz = []  # Inicializa uma lista vazia para representar a matriz
    for i in range(rows):  # Itera sobre o número de linhas
        linha = []  # Inicializa uma lista vazia para representar uma linha da matriz
        for j in range(cols):  # Itera sobre o número de colunas
            # Solicita ao usuário para inserir um valor para a posição (i, j) da matriz e converte para inteiro
            valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))  
            linha.append(valor)  # Adiciona o valor à linha atual da matriz
        matriz.append(linha)  # Adiciona a linha à matriz
    return matriz  # Retorna a matriz criada

# Define uma função para calcular a transposição de uma matriz
def transpor_matriz(matriz):
    transposta = []  # Inicializa uma lista vazia para representar a matriz transposta
    for i in range(len(matriz[0])):  # Itera sobre o número de colunas da matriz original
        linha_transposta = []  # Inicializa uma lista vazia para representar uma linha da matriz transposta
        for linha in matriz:  # Itera sobre cada linha da matriz original
            linha_transposta.append(linha[i])  # Adiciona o elemento na posição (i, j) à linha transposta
        transposta.append(linha_transposta)  # Adiciona a linha transposta à matriz transposta
    return transposta  # Retorna a matriz transposta

# Define uma função para imprimir uma matriz
def imprimir_matriz(matriz):
    for linha in matriz:  # Itera sobre cada linha da matriz
        print(linha)  # Imprime a linha

# Solicita ao usuário para inserir o número de linhas e colunas da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Cria a matriz com base no número de linhas e colunas inserido pelo usuário
matriz = criar_matriz(linhas, colunas)

# Imprime a matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Calcula e imprime a transposta da matriz
print("Transposta da matriz:")
transposta = transpor_matriz(matriz)
imprimir_matriz(transposta)
