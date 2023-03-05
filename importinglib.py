import spacy
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

nlp = spacy.load('en_core_web_sm')

def process_input(input_text):
    tokens = nltk.word_tokenize(input_text)
    pos_tags = [(token.text, token.pos_) for token in nlp(input_text)]
    output = ''
    for token, pos in pos_tags:
        output += f'{token} ({pos}), '
    return output[:-2]

