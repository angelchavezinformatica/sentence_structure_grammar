from nltk import word_tokenize

def preprocess(sentence: str):
    final_processed_sentence =""
    processed_sentence = sentence.lower().split()

    for word in processed_sentence:
        processed_word = filter(str.isalnum, word)
        processed_word = filter(str.isalnum, processed_word)
        words = "".join(processed_word)
        final_processed_sentence += words + " "
    tokenized_words = word_tokenize(final_processed_sentence)

    return tokenized_words

def np_chunk(tree):
    output = list()

    for x in range(tree.height()):
        if x < 2:
            continue
        for s in tree.subtrees(lambda tree: tree.height() == x):
            s_text = str(s)
            if s_text.count("(NP") == 1:
                if s_text.find("(NP", 0, 3) > -1:
                    output.append(s)
    
    return output