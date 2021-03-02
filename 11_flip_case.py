def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    output = ""
    for ltr in phrase:
        if ltr.upper() == to_swap.upper():
            output += ltr.swapcase()
        else:
            output += ltr
    return output