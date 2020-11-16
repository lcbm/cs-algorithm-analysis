""" Functions to mock data that represents either the worst and best case of sorting algorithms. """


def best_and_worst_cases(quantity: int) -> tuple:
    """ Function to mock data for the best and worst cases for some sorting algorithms. """
    best_case = __mock_best_case(quantity=quantity)
    common_worst_case = __mock_worst_case(arr=best_case)
    merge_worst_case = __mock_merge_worst_case(arr=common_worst_case)
    return (best_case, common_worst_case, merge_worst_case)


def __mock_best_case(quantity: int) -> list:
    return list(range(1, quantity + 1))


def __mock_worst_case(arr: list) -> list:
    return arr[::-1]


def __mock_merge_worst_case(arr: int) -> list:
    evens = arr[0:][::2]
    odds = arr[1:][::2]
    return evens + odds
