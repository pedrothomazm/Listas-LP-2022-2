import numpy as np
from numpy.random import default_rng

'''
===================================================================
1 - Crie uma função usando numpy que caso receba uma matriz 
bidimensional numpy retorna um vetor unidimensional. Se a entrada é
um vetor unidimensional retorne uma matriz diagonal com os 
elementos do vetor. Caso contrário levante uma exceção ValueError.
===================================================================
''' 

def diagonalEspecial(D):
    if D.ndim == 1:
        return np.diag(D)
    
    if D.ndim == 2:
        return D.flatten()
    
    raise ValueError('A entrada deve ser unidimensional ou bidimensional.')

# print(diagonalEspecial(np.array([[1,2,3,4,5],[6,7,8,9,0]])))

'''
===================================================================
2 - Crie uma função para simular o jogo pedra papel tesoura usando 
números aleatórios do numpy.
- Suponha que tirar pedra, papel ou tesoura possui a mesma 
probabilidade de acontecer.
- A entrada corresponde ao número de vezes que o experimento deve
acontecer.
- A função deve retornar um dicionário com a quantidade de vezes
que cada evento aconteceu (ex: {'papel':1,'pedra':3,'tesoura':2})
===================================================================
'''

def jokenpo(n):
    rng = default_rng()

    valores, contagem = np.unique(rng.integers(0, 3, n), return_counts=True)

    for i in range(3):
        if valores.size <= i or valores[i] != i:
            valores = np.insert(valores, i, i)
            contagem = np.insert(contagem, i, 0)
    
    jogadas = ['papel', 'pedra', 'tesoura']
    
    return dict(zip(jogadas, contagem))

    # # Solução alternativa cuja distribuição é menos uniforme:
    # # Gera 2 inteiros de 0 a n
    # random_nums = rng.integers(0, n, 2, endpoint=True)

    # # Insere 0 e n à lista
    # random_nums = np.insert(random_nums, [0, 2], [0, n])

    # # Ordena
    # random_nums.sort()

    # # Obtém uma lista das diferenças dos valores adjacentes
    # # Essa lista é composta de inteiros aleatórios não negativos cuja soma é n
    # random_counts = np.ediff1d(random_nums)

    # jogadas = ['papel', 'pedra', 'tesoura']

    # return dict(zip(jogadas, random_counts))

# print(jokenpo(10))

'''
===================================================================
3 - Crie uma função para expandir uma matriz numpy. Dada uma matriz
A de dimensão mxn, retorne A com dimensão kxk onde k = max(m,n).
Completando com zeros até que A possua a dimensão kxk. 
===================================================================
'''

def expandir(A):
    m, n = A.shape
    k = max(m, n)
    # Adiciona k-m linhas de zeros abaixo e k-n colunas à direita
    return np.pad(A, ((0, k - m), (0, k - n)))

# print(expandir(np.array([[1,2],[3,4],[5,6],[7,8]])))

'''
===================================================================
4 - Crie uma função numpy que dada uma matriz A de dimensão mxn. 
Retorne um vetor um vetor coluna mx1 onde cada entrada i 
corresponde ao menor valor da linha i.
===================================================================
'''

def minimos(A):
    # Obtém os mínimos de cada linha e transforma o resultado em vetor coluna
	return A.min(1).reshape(A.shape[0], 1)

# print(minimos(np.array([[1,2],[3,4],[5,6],[7,8]])))

'''
===================================================================
5 - Sabemos que uma multiplicação de matrizes não é comutativa. 
Mas, em alguns casos é possível verificar que A*B = B*A. Crie uma 
função que dada duas matrizes ela retorna verdadeiro se A*B=B*A e
retorna falso caso contrário. Observe que quando A e B não são 
matrizes quadradas a função deve retornar falso, independente do 
tamanho de A e B.
===================================================================
'''

def AB_igual_BA(A,B):
    if A.shape != B.shape:
        return False
    
    return np.array_equal(np.matmul(A, B), np.matmul(B, A))

# print(AB_igual_BA(np.array([[1,2],[3,5]]), np.array([[1,2],[3,4]])))

'''
===================================================================
6 - Crie uma função que recebe uma lista de vetores numpy, retorne 
o vetor que possuiu a menor norma vetorial. 
Desafio opcional: tente resolver essa questão com uma só linha de 
código, recomendo utilizar map e função lambda. Confira a seguir:
https://medium.com/horadecodar/express%C3%B5es-lambda-em-python-com-map-reduce-e-filter-a391368ae886
https://cs.stanford.edu/people/nick/py/python-map-lambda.html
===================================================================
'''

def menorNorma(l):
	return min(l, key = np.linalg.norm)

# print(menorNorma([np.array([1,2]),np.array([3,4]),np.array([5,6]),np.array([7,8])]))

'''
===================================================================
7 - Desafio, vamos estimar o valor de pi por meio do Método de 
Monte Carlo. Considere um círculo de raio r=1 centrado na origem 
que está inscrito num quadrado de lado l=2 (veja a figura pi.png).
Vamos estimar o valor de pi comparando a razão da quantidade de 
pontos P_c que "caíram" dentro do círculo (matematicamente P_c
representa o número de pontos em que a distância euclidiana deles
a origem é menor do que r) em relação ao total de pontos P com a
razão da área do círculo em relação ao quadrado, observe:
pi*r^2/l^2 ~= P_c/P
Isto é, utilizando os valores de r^2=1 e l^2=4 estime o valor de pi:
pi/4 ~= P_c/P 
A função que vocês devem implementar deve:
- Receber n como o número de pontos que serão gerados.
- Gerar com numpy n coordenadas x aleatórias.
- Gerar com numpy n coordenas y aleatórias.
- Calcular a quantidade P_c de pontos que caíram dentro do círculo, 
isto é, calcular a distância do ponto I=(x_i,y_i) à origem (0,0) e
contar quantos estão mais próximos da origem do que o raio do círculo
(r=1).
- Retornar o valor de Pi de acordo com a expressão pi = (4*P_c)/P.
Obs: para saber mais sobre o Método de Monte Carlo acesse:
https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Monte_Carlo
===================================================================
'''

def piMonteCarlo(n):
    rng = default_rng()

    # Gera n pontos aleatórios com coordenadas de -1 a 1
    pontos = rng.uniform(-1, 1, (n, 2))

    # Calcula quantos pontos estão dentro do círculo
    pontos_dentro = np.count_nonzero(np.linalg.norm(pontos, axis = 1) < 1)
    
    return 4 * pontos_dentro / n

# print(piMonteCarlo(31415))