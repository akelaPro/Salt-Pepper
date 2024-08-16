def combine_anagrams(words_array):
    result = {}
    for word in words_array:
        sort_word = ''.join(sorted(word))
        if sort_word not in result:
            result[sort_word] = [word]
        else:
            result[sort_word].append(word)
    return list(result.values())

