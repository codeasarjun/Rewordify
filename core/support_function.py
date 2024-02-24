
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import random
# Function to get synonyms for a word
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

# Function to rephrase a sentence
def rephrase_sentence(sentence,style):
    words = word_tokenize(sentence)
    rephrased_sentence = []
    for word in words:
        synonyms = get_synonyms(word)
        if style == 'simple':
            # Use only basic synonyms for Simple English
            synonyms = [s for s in synonyms if "_" not in s]
        elif style == 'academic':
            # Use more formal synonyms for Academic English
            synonyms = [s for s in synonyms if s.isalpha() and s.islower()]
        elif style == 'fluency':
            # Use a mix of synonyms for Fluency
            pass  # You can customize this based on your requirements
        elif style == 'tech':
            # Use technical synonyms for Technical English
            synonyms = [s for s in synonyms if s.isalpha() and s.islower() and "_" in s]
        if synonyms:
            rephrased_sentence.append(random.choice(synonyms))
        else:
            rephrased_sentence.append(word)
    return ' '.join(rephrased_sentence)