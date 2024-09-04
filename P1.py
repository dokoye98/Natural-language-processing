import nltk
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
nlp = English()
sentence = "At eight o'clock on Thursday morning Authur did'nt feel very good"
##tokens = nltk.word_tokenize(sentence)
##print(tokens)
tokenizer = Tokenizer(nlp.vocab)
