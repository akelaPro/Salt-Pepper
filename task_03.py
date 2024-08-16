def max_odd(array):
    odd_list = list(filter(odd, array))
    if odd_list:
        max_char = max(odd_list)
        return int(max_char)
    return None

def odd(char):
    if isinstance(char, (int, float)):
        return int(char) % 2 !=0
