def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiouAEIOU"
    dict = {}

    phrase_vowels = [ltr.lower() for ltr in list(phrase) if ltr in vowels]

    for vowel in phrase_vowels:
        count = dict.get(vowel, 0) + 1
        dict[vowel] = count

    return dict