def implementRR(word_data):
    new_word_data = []
    for entry in word_data:
        if entry['graphemes'][0] == 'R':
            entry['graphemes'][0] = 'RR'
        new_word_data.append(entry)

    return new_word_data