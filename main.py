# import statments
import numpy
import re

def tokenize(text):
    words = []
    words = word_extraction(text)        
    words = sorted(list(set(words)))
    return words

def word_extraction(sentence):
    words = re.sub("[^\w]", " ",  sentence).split()
    cleaned_text = [w.lower() for w in words]
    return cleaned_text    
    
def generate_bow(text):    
    vocab = tokenize(text)
    words = word_extraction(text)
    bag_vector = numpy.zeros(len(vocab))
    for w in words:
        for i,word in enumerate(vocab):
            if word == w: 
                bag_vector[i] += 1
    return bag_vector

f = open("sent.txt", "r",encoding="utf8")
text = f.read()
text = result = re.sub(r'[^A-Z a-z]', ' ',text)

words = tokenize(text)
bow = generate_bow(text)
i = numpy.array(list(bow>44))
counts = (bow[i])
words = (numpy.array(words)[i])
d = dict(zip(words,counts))
print(sorted(d.items(), key=lambda x: x[1],reverse=True))
#print(numpy.array(words)[i])
#print(words[numpy.array(bow>10)])