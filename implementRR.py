def implementRR(word_data):
    for entry in word_data:
        if entry['graphemes'][0] == 'R':
            entry['graphemes'][0] = 'RR'
            del entry['graphemes'][1]

    return word_data