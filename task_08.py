from functools import reduce
def multiply_numbers(inputs=None):
    if not inputs:
        return None
    output = [int(x) for x in str(inputs) if x.isdigit()]
    if not output:
        return None
    result = reduce(lambda x, y: x * y, output, 1)
    return result
