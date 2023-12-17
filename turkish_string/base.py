'''Base module for turkish_string package'''
LOWER_MAPPING = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
}

UPPER_MAPPING = {
    ord(u'ı'): u'I',
    ord(u'i'): u'İ'
}


def upper_tr(string:str) -> str:
    '''
    Return a copy of the string converted to uppercase.

    Works with Turkish characters.
    '''
    if not isinstance(string, str):
        raise TypeError(
            f'Argument must be of type "str" not "{type(string).__name__}"'
        )

    return string.translate(UPPER_MAPPING).upper()


def lower_tr(string:str) -> str:
    '''
    Return a copy of the string converted to lowercase.

    Works with Turkish characters.
    '''
    if not isinstance(string, str):
        raise TypeError(
            f'Argument must be of type "str" not "{type(string).__name__}"'
        )

    return string.translate(LOWER_MAPPING).lower()


def capitalize_tr(string:str) -> str:
    '''
    Return a capitalized version of the string.

    More specifically, make the first character have upper case
    and the rest lower case.

    Works with Turkish characters.
    '''
    if not isinstance(string, str):
        raise TypeError(
            f'Argument must be of type "str" not "{type(string).__name__}"'
        )

    if len(string) == 1:
        return string[0].translate(UPPER_MAPPING).capitalize()
    
    elif len(string) > 1:
        return (
            f'{string[0].translate(UPPER_MAPPING)}'
            f"{''.join([char.translate(LOWER_MAPPING) for char in string[1:]])}"
        ).capitalize()
    
    else:
        return string.capitalize()



def title_tr(string:str) -> str:
    '''
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and
    all remaining cased characters have lower case.

    Works with Turkish characters.
    '''
    if not isinstance(string, str):
        raise TypeError(
            f'Argument must be of type "str" not "{type(string).__name__}"'
        )

    return ' '.join(
                [
                    ''.join(
                        [
                            word[0].translate(UPPER_MAPPING),
                            word[1:].translate(LOWER_MAPPING)
                        ]
                    )\
                    if word != '' else ''
                    for word in string.split(' ')\
                ]
            ).title()