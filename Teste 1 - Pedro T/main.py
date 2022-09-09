import numpy as np
import funcoes_auxiliares as fa

print('3º número de Fibonacci:', fa.fibonacci_at(3))
print()
print('Números de Fibonacci menores que 10:', fa.fibonacci_less_than(10))
print()
print('8 é número de Fibonacci?', fa.is_in_fibonacci(8))
print()

ndarray_ate_10 = np.arange(11)
ate_10_em_fib = ndarray_ate_10[fa.ndarray_is_in_fibonacci(ndarray_ate_10)]
print('Números menores que 10 em Fibonacci:', ate_10_em_fib)
print()
print()

# Melhora a visualização
np.set_printoptions(suppress=True)

print('Pagando R$30.000,00 em 12 mêses com 1,5% de juros:')
print('1ª linha: valor atual do mês; 2ª linha: amortização; 3ª linha: juros pagos\n\n', fa.tabela_price(30000, 0.015, 12), sep='')
print()

notas_crit = fa.notas_rng(5)
notas_clientes = fa.notas_rng(5)

print('5 notas aleatórias de 1 a 5:', notas_crit)
print()
print('Notas de críticos e clientes agrupadas:\n', fa.junta_notas(notas_crit, notas_clientes), sep='')
print()

fa.metas_e_stats(notas_crit)