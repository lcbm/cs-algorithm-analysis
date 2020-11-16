""" Python implementation of sorting algorithms. """

import constants


def run(algorithm: str, input: str) -> list:
    """Wrapper function to run the desired sorting algorithm"""
    algorithms = {
        constants.GNOME_SORT: __gnome_sort,
        constants.COCKTAIL_SORT: __cocktail_sort,
        constants.SELECTION_SORT: __selection_sort,
        constants.MERGE_SORT: __merge_sort,
    }

    if algorithm not in algorithms.keys():
        raise KeyError(
            f"Error: {algorithm} is not a valid algorithm, please chose one of {algorithms.keys()}"
        )

    return algorithms[algorithm](input)


def __gnome_sort(arr: list) -> list:
    length = len(arr)

    # 0. verificar caso base: se arr for vazio ou tamanho 1, retornar arr
    if length < 2:
        return arr

    index = 0
    while index < length:
        # 1. se estiver no inicio do arr, pule para a proxima posição
        if index == 0:
            index += 1
        # 2. se o elemento atual for MAIOR ou IGUAL ao anterior,
        # ir para próximo elemento
        if arr[index] >= arr[index - 1]:
            index += 1
        # 3. se o elemento atual for MENOR que o anterior,
        # trocar estes elementos de lugar e voltar uma etapa
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
        # 4. repetir etapas 2 e 3 até percorrer toda a lista

    # 5. se chegar ao fim da lista, a lista esta ordenada
    return arr


def __cocktail_sort(arr: list) -> list:
    length = len(arr)

    # 0. verificar caso base: se arr for vazio ou tamanho 1, retornar arr
    if length < 2:
        return arr

    start = 0
    end = length - 1
    swapped = True
    while swapped:
        # caso algum elemento tenha sido movido,
        # resetar a flag para ser usada no próximo estágio
        swapped = False

        # 1. iterar a lista da esquerda para direita
        for index in range(start, end):
            # 2. comparar elementos adjacentes,
            # se o elemento à esquerda for maior que o da direita,
            # trocar estes elementos de lugar e voltar uma etapa
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

        # se nenhum elemento foi movido, a lista esta ordenada
        if not swapped:
            break

        # caso algum elemento tenha sido movido,
        # resetar a flag para ser usada no próximo estágio
        swapped = False

        # mover índice final um índice para trás,
        # uma vez que na primeira iteração o maior valor
        # já está no lugar correto (na primeira iteração, mais à direita)
        end -= 1

        # 3. iterar a lista da direita para a esquerda,
        # desta vez a partir do último elemento ordenado
        for index in range(end - 1, start - 1, -1):
            # 4. comparar elementos adjacentes,
            # se o elemento à esquerda for maior que o da direita,
            # trocar estes elementos de lugar e voltar uma etapa
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

        # mover índice final um índice para trás,
        # uma vez que na primeira iteração o menor valor
        # já está no lugar correto (na primeira iteração, mais à esquerda)
        start += 1

    return arr


def __selection_sort(arr: list) -> list:
    length = len(arr)

    # 0. verificar caso base: se arr for vazio ou tamanho 1, retornar arr
    if length < 2:
        return arr

    for index in range(length):
        # 1. buscar o menor elemento na lista
        min = index
        for j in range(index + 1, length):
            if arr[min] > arr[j]:
                min = j

        # 2. trocar o menor elemento com o primeiro
        arr[index], arr[min] = arr[min], arr[index]
        # 4. repetir etapas 2 e 3 até percorrer toda a lista

    # 5. se chegar ao fim da lista, a lista esta ordenada
    return arr


def __merge_sort(arr: list) -> list:
    length = len(arr)

    # 0. verificar caso base: se arr for vazio ou tamanho 1, retornar arr
    if length < 2:
        return arr

    # 1. encontrar o centro da lista
    # e dividir a lista em duas metadas a partir do centro
    center = length // 2
    left = arr[:center]
    right = arr[center:]

    # 2. chamar merge_sort para ordenar cada metade da lista, recursivamente
    __merge_sort(left)
    __merge_sort(right)

    # 3. combinar as duas listas
    index = j = k = 0
    while index < len(left) and j < len(right):
        if left[index] < right[j]:
            arr[k] = left[index]
            index += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 4. percorrer itens remanescentes
    # e inseri-los na lista
    while index < len(left):
        arr[k] = left[index]
        index += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
