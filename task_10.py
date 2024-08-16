def count_words(text=None):
    if not text:
        return None
    words = text.lower().split()
    word_count = {}

    for word in words:
        word = ''.join(filter(str.isalnum, word))
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
