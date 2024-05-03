def implementRR(word_data):
    for entry in word_data:
        print("Entry: ", entry['graphemes'])

        if entry['graphemes'][0] == 'R':
            entry['graphemes'][0] = 'RR'

    return word_data