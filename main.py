from typing import List

numpad = {
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8'],
    '0': ['8'],
}


def possible_values(password: str) -> List[str]:
    """Possible passwords.

    Args:
        password: str - initial password

    Returns:
        list of possible passwords

    """
    res = [password]
    for i in range(len(password)):
        try:
            for j in numpad[password[i]]:
                res.append(password[:i] + j + password[i + 1:])
        except KeyError:
            return f'"{password[i]}" it\'s not a number.'

    return res
