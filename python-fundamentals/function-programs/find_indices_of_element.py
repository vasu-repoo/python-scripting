def find_indices_of_element(l, elem):
    '''Find all indices of an element in a list.

    Args:
        l (list): The input list.
        elem: The element to find.

    Returns:
        list: A list of indices where the element is found.

    Examples:
    >>> find_indices_of_element([1, 2, 3, 2, 4], 2)
    [1, 3]
    >>> find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
    [0, 2]
    '''
    result =[]
    for i in range(len(l)):
        if l[i]==elem:
            result.append(i)
    return result

print(find_indices_of_element([1, 2, 3, 2, 4], 2))