def coincidence(lst=None, ranges=None):
    if not lst and  not ranges:
        return []
    result = [char for char in lst if isinstance(char, (int, float))
                             and ranges.start <= char < ranges.stop]
    return result
