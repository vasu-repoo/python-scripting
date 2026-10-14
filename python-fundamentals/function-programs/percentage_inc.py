def percentage_increase(original, new):
    '''Calculate the percentage increase from the original value to the new value.

    Args:
        original (float): The original value.
        new (float): The new value.

    Returns:
        float: The percentage increase.

    Examples:
    >>> percentage_increase(50, 75)
    50.0
    >>> percentage_increase(80, 100)
    25.0
    '''
    return ((((new-original)/original)))*100