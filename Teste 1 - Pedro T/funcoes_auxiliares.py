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


def fibonacci_less_than(n):
    try:
        # O parâmetro precisa ser inteiro
        if not isinstance(n, int):
            raise TypeError('O parâmetro deve ser inteiro')
    
    except Exception as error:
        return error

    fib_less = []

    elem_a = 0
    elem_b = 1

    while elem_a < n:
        fib_less.append(elem_a)

        # O próximo elemento é a soma dos anteriores
        elem_a, elem_b = elem_b, elem_a + elem_b
    
    # Retorna um NumPy Array
    return np.array(fib_less)


def is_in_fibonacci(n):
    try:
        # O parâmetro precisa ser inteiro
        if not isinstance(n, int):
            raise TypeError('O parâmetro deve ser inteiro')
    
    except Exception as error:
        return error
    
    elem_a = 0
    elem_b = 1

    # Itera até encontrar o menor elemento maior ou igual a n
    while elem_a < n:
        # O próximo elemento é a soma dos anteriores
        elem_a, elem_b = elem_b, elem_a + elem_b
    
    return n == elem_a


def ndarray_is_in_fibonacci(array):
    try:
        # O parâmetro precisa ser um NumPy Array
        if not isinstance(array, np.ndarray):
            raise TypeError('O parâmetro deve ser um NumPy Array')
        
        # O parâmetro só pode conter inteiros
        if not issubclass(array.dtype.type, np.integer):
            raise TypeError('O tipo dos dados do Array deve ser inteiro')
        
        # O parâmetro não pode conter inteiros menores que 0 ou maiores que 1000
        if np.any(array < 0) or np.any(array > 1000):
            raise ValueError('O parâmetro deve conter apenas inteiros entre 0 e 1000')
    
    except Exception as error:
        return error
    
    # Números de Fibonacci menores ou iguais a 1000
    fib_0_to_1000 = fibonacci_less_than(1001)

    # Verifica se cada elemento está na sequência
    return np.isin(array, fib_0_to_1000)