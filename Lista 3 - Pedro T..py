import numpy as np
from numpy.random import default_rng

'''
===================================================================
1 - Usando apenas o conceito de "máscaras" (usar uma array de boo-
leanas para selecionar elementos de outra array), crie uma função
que receba um argumento m e n e retorne uma array mxn com valores
gerados aleatoriamente.

Você deve gerar uma array com uma distribuição normal de média 7 
e desvio padrão 2, e após disso, você deve implementar um limite
de valores: os elementos da array devem ser, no máximo, 10, e no mí-
nimo, 0. 
===================================================================
''' 

def normalComLimite(m,n):
    rng = default_rng()

    # Array m x n com uma distribuição normal de média 7 e desvio padrão 2
    dist_normal = rng.normal(7, 2, (m, n))

    while True:
        # Array de booleanos indicando elementos fora dos limites
        fora_do_limite = (dist_normal > 10) | (dist_normal < 0)
        num_fora_lim = np.count_nonzero(fora_do_limite)

        if num_fora_lim == 0:
            return dist_normal

        # Gera novos números para substituir aqueles fora do limite
        dist_normal[fora_do_limite] = rng.normal(7, 2, num_fora_lim)

# print(normalComLimite(5,5))

'''
===================================================================
2 - Novamente usando o conceito de máscaras, crie uma função que 
irá receber uma array mxn que representa notas de alunos em uma 
disciplina, onde cada linha representa um aluno e cada coluna a
nota de uma prova, que vale 10. A função deverá retornar uma array 
mx1 de booleanas, cujo valor de cada linha deverá indicar True se o 
aluno daquele índice tirou acima de 7 em ao menos metade das provas,
e False caso contrário.
===================================================================
'''

def alunosAprovados(notas):
    # Obtém metade do número de colunas (provas)
    min_aprovacao = notas.shape[1] / 2

    # Obtém um array de booleanos indicando notas acima de 7
    acima_de_7 = notas > 7

    # Obtém o número de notas acima de 7 por linha
    count_acima_7 = np.count_nonzero(acima_de_7, axis=1)
    alunos_aprovados = count_acima_7 >= min_aprovacao

    # Altera o formato para ter apenas uma coluna
    return alunos_aprovados.reshape(-1, 1)

# print(alunosAprovados(np.array([[8,9,1],[1,2,1],[1,2,1],[1,2,9],[10,10,10]])))


'''
===================================================================
3 - Usando apenas o conceito de broadcasting numpy (ou seja, sem 
usar outras bibliotecas), crie uma função que receba uma array 1xn 
e retorne uma array 1xn que é a "normalização Z-score" dela.  
===================================================================
'''

def normalizarZScore(array):
    media = array.mean()
    desvio_padrao = array.std()

    # Array de cada elemento subtraído pela média e dividido pelo desvio padrão
    return (array - media) / desvio_padrao

# print(normalizarZScore(np.array([0,1,2,3,4,5,6,7,8,9,10])))

'''
===================================================================
4 - Crie uma função que receberá uma array mxn que representa notas 
de alunos da mesma forma que na questão 2, e retorne uma array mx1 
de booleanas, cujo valor de cada linha deverá indicar True se o a-
luno daquele índice deverá ficar de recuperação, ou False caso não.

Um aluno deverá ficar de recuperação se a média das notas dele for
menor que 7 mas maior que 5.
===================================================================
'''

def recuperacao(array):
    # Obtém a média de cada linha
    medias = array.mean(axis=1)

    # Obtém um array de booleanos indicando os alunos de recuperação
    recup = (medias < 7) & (medias > 5)

    # Altera o formato para ter apenas uma coluna
    return recup.reshape(-1, 1)

# print(recuperacao(np.array([[5,6,7],[7,8,9],[1,2,3],[6,7,8]])))

'''
===================================================================
5 - Crie uma função que receberá uma array mxn de inteiros e que 
retornará uma array mxn cujos elementos são o fatorial dos elemen-
tos da array de entrada.

Para aplicar o fatorial em cada elemento, não será permitido usar
loops. Tente pesquisar sobre a função "vectorize" do numpy.  
===================================================================
'''

def fatorial(num):
    if num <= 1:
        return 1
    return num * fatorial(num - 1)

# Gera uma função que aplica fatorial(num) a cada elemento de um array
fatorialArray = np.vectorize(fatorial)

# print(fatorialArray(np.array([[1,2,3],[4,5,6],[7,8,9]])))