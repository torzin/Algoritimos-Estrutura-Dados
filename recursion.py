# toda função recursiva deve ter um caso base: uma condição que encerre o algoritimo
# para que fique executando eternamente
# 3 regras da recursão:
# 1. Um algoritimo deve ter um caso base
# 2. Um algoritimo deve alterar seu estado e prosseguir em direção ao caso base
# 3. Um algoritimo recursivo deve chamar a si mesmo recursivamente.

# qualquer algoritimo recursivo pode ser iterativo

# exemplo: fatorial
# sem recursividade


def factorial_0(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n-1
    return the_product

# com recursividade


def factorial_1(n):
    if n == 0:
        return 1
    return n * factorial_1(n - 1)

# exiba os números de 1 a 10 recursivamente
def show_numbers(n):
    if n == 0:
        print(n)
        return
    print(n)
    return show_numbers(n-1)

show_numbers(10)
