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
    dist_normal = rng.normal(7, 2, (m, n))

    while True:
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

    acima_de_7 = notas > 7
    count_acima_7 = np.count_nonzero(acima_de_7, axis=1)
    
    alunos_aprovados = count_acima_7 >= min_aprovacao
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
	return

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
	return 

'''
===================================================================
5 - Crie uma função que receberá uma array mxn de inteiros e que 
retornará uma array mxn cujos elementos são o fatorial dos elemen-
tos da array de entrada.

Para aplicar o fatorial em cada elemento, não será permitido usar
loops. Tente pesquisar sobre a função "vectorize" do numpy.  
===================================================================
'''

def fatorialArray(array):
	return