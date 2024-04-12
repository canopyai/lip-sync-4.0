from g2p_en import G2p
g2p = G2p()

def convert_word_to_graphemes(word):
    graphemes = g2p(word)
    return graphemes