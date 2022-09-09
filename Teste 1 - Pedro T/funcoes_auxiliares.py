import numpy as np


def fibonacci_at(n):
    try:
        # O parâmetro precisa ser inteiro
        if not isinstance(n, int):
            raise TypeError('O índice precisa ser inteiro')
        
        # Foi considerado que o primeiro índice é 0
        if n < 0:
            raise ValueError('O índice não pode ser negativo')

    except Exception as error:
        return error

    elem_a = 0
    elem_b = 1

    for i in range(n):
        # O próximo elemento é a soma dos anteriores
        elem_a, elem_b = elem_b, elem_a + elem_b
    
    return elem_a