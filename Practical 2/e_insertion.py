def e_insertion(word):
    last_word = ['s', 'z', 'x', 'sh', 'ss', 'ch'] # Noun ends with these words
    plural = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    len_word = len(word)

    if word[len_word-1] in last_word or word[len_word-2:] in last_word or ( word[len_word-2] in consonants and word[len_word-1] in ['o']):
        plural = word + 'es'
    elif ( word[len_word-2] in vowels and word[len_word-1] in ['o', 'y']):
        plural = word + 's'
    elif ( word[len_word-2] in consonants and word[len_word-1] == 'y'):
        plural = word[:len_word-1] + 'ies'
    else:
        plural = word + 's'
    return plural

words = ['watch', 'branch', 'fish', 'brush', 'bus', 'virus', 'glass', 'class', 'box', 'fox', 'mango', 'tomato', 'mosquito', 'studio', 'zoo', 'video', 'baby', 'duty', 'joy', 'toy', 'shoe', 'die']
for word in words:
    print(word, "->", e_insertion(word))
