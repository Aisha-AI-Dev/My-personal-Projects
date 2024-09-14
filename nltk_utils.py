import nltk
#nltk.download('punkt')

nltk.download('punkt', download_dir='/Users/aishanipatil/nltk_data')

#from nltk.stem.porter import PorterStemmer
#stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass


a = "I am not here."
a = tokenize(a)
print(a)