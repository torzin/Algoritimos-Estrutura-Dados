# Busca linear é aquela que interage sequencialmente com
# os carácteres de uma strig/array

list_1 = [1,2,54,4322,234,10,0]
def linear_search(list, n):
    for i in list:
        if i == n:
            return True
    return False

# ou

print(0 in list_1)