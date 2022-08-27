import statistics
import re

'''
===================================================================
1 - Crie uma função que receberá diversas alturas através de inputs 
(em algum loop) e retornará a média delas. Essa função deve ser pro-
tegida contra entrada de valores inválidos.
===================================================================
'''

def media_alturas():
    print('Insira todas as alturas e então digite "Parar".')

    alturas = []
    # Loop infinito com break no meio quando a condição de parada for atingida
    while True:
        num_entrada = len(alturas) + 1
        entrada = input(f'{num_entrada}: ')

        # Detecta se o loop deve parar
        if entrada == 'Parar':
            break

        try:
            altura = float(entrada)

            # Detectção de valores inválidos que não geram exceções
            if altura <= 0:
                print('Valor inválido')
                continue

            alturas.append(altura)
        except ValueError:
            print('Valor inválido')
    
    media = statistics.mean(alturas)

    return media

'''
===================================================================
2 - Crie uma função que receberá um path para um arquivo .txt, irá
abrí-o em modo read, e caso o arquivo não exista, irá criá-lo.
===================================================================
'''

def ler_txt(path):
    try:
        # Tenta abrir o arquivo
        arquivo = open(path, 'r')
    except FileNotFoundError:
        # No caso de não ser encontrado, o arquivo é criado
        arquivo = open(path, 'x')
    finally:
        # Sempre fecha o arquivo como uma boa prática de programação
        arquivo.close()

'''
===================================================================
3 - Crie uma função que receberá duas listas de números e retornará
uma nova lista que é uma soma das duas listas. 

Ela deve ser protegida contra entrada de valores inválidos e, caso
as listas sejam de tamanhos diferentes, deve ser retornado uma men-
sagem ao usuário.

Exemplo 1:
[1, 3, 4, 6]
[2, 8, 11, 1]

Output:
[3, 11, 15, 7]


Exemplo 2:
[1, 5]
[4, 2, 8]

Output:
"Tamanhos não compatíveis!"
===================================================================
'''

def soma_listas(lista1, lista2):
    try:
        # Testa o comprimento das listas
        if len(lista1) != len(lista2):
            return 'Tamanhos não compatíveis!'
    except TypeError:
        # Retorno caso os parâmetros não tiverem comprimento
        return 'Valores inválidos.'

    resultado = []

    try:
        # Itera os itens das listas juntos
        for item1, item2 in zip(lista1, lista2):
            resultado.append(item1 + item2)
    except TypeError:
        # Se alguma operação gerar um erro, retorna essa string
        return 'Valores inválidos.'
    
    return resultado

'''
===================================================================
4 - Crie uma função que receberá uma lista de nomes e irá lançar
uma exceção caso algum nome seja inválido.

Um nome é inválido quando:
- Não for uma string
- Tiver números
- Tiver um dos seguintes caracteres: "!@#$%¨&*()_+=-{}[]|:;<>,.?/

O tipo de exceção lançada deve ser diferente para cada um dos três
tipos de nomes inválidos. (Use raise Exception())
===================================================================
'''

def recebe_nomes(nomes):
    for nome in nomes:
        # Testa se é uma string
        if not isinstance(nome, str):
            raise TypeError('Era esperado string.')
        
        # Testa por dígitos no nome
        if any(char.isdigit() for char in nome):
            raise ValueError('Número inesperado encontrado.')
        
        # Regex para tentar encontrar algum dos caracteres proibidos
        if re.search(r'["!@#\$%¨&\*\(\)_\+=\-{}\[\]\|:;<>,\.\?\/]', nome):
            raise RuntimeError('Caractere inesperado encontrado.')

'''
===================================================================
5 - Crie uma função fatorial para os números inteiros não negativos
retorne o fatorial do número (exemplo 4!=24, 1!=1). Para criar essa 
função não é permitido utilizar bibliotecas, apenas o python 
padrão. Proteja a função para qualquer tipo de dados que seja
diferente dos números inteiros não negativos (-5! = exceção).
===================================================================

'''

def fatorial(numero):
    # Teste por números negativos
    # Caso a entrada não seja um número, a comparação levanta uma exceção, assim como o enunciado pede
    if numero < 0:
        # Levanta exceção em caso de número negativo
        raise ValueError('Fatorial não é definido para números negativos.')
    
    resultado = 1

    # Multiplica os números de 2 até a entrada para calcular o fatorial
    # Caso a entrada não seja inteira, a função range levanta uma exceção, assim como o enunciado pede
    for num in range(2, numero + 1):
        resultado *= num
    
    return resultado

# Linhas usadas para testar as funções:
# print(f'A média das alturas é {media_alturas()}')
# ler_txt('waaaa.txt')
# print(soma_listas([1, 2, 3], [1, 2, 'AAAAAAAAAAAAAAAAAAAAA']))
# recebe_nomes(["Pedro3"])
# print(fatorial(3.0))