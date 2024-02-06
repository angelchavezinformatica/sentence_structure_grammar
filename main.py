import sys

from nltk import CFG, ChartParser

from core.grammar import NON_TERMINALS, TERMINALS
from core.sentences import sentences
from core.utils import np_chunk, preprocess


grammar = CFG.fromstring(NON_TERMINALS + TERMINALS)
parser = ChartParser(grammar=grammar)


def run(sentence: str):
    sentence = preprocess(sentence=sentence)
    
    try:
        trees = list(parser.parse(sentence))
    except ValueError:
        print("No es una frase valida")
        return
    
    if not trees:
        print("No se pudo analizar la oración.")
        return
    
    for tree in trees:
        tree.pretty_print()
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sentence = input("Frase: ")
        run(sentence=sentence)
    elif sys.argv[1] == "--test":
        for sentence in sentences:
            print(sentence)
            run(sentence=sentence)
            print()
        