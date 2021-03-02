def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}

        
    """
    frequencies = {}
    for ltr in phrase:
        if ltr in frequencies:
            
            frequencies[ltr]+=1
        else:
            frequencies[ltr]=1
    return frequencies