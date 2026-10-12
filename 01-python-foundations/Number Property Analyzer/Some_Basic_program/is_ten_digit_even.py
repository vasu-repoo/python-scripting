def is_ten_digit_even(n):
    '''Returns True if the number is a 10 digit even number, False otherwise.

    Args: 
        n (int): The given number. 

    Returns: 
        bool : result as True or False. 

    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(9289479278)
    True
    '''
    if len(str(n))==10 and n%2==0:
        return True
    else:
        return False
