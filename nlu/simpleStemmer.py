import nltk

def simple_stemmer(text):
	ps = nltk.porter.PorterStemmer()
	text = ' '.join([ps.stem(word) for word in text.split()])
	return text

#print(simple_stemmer("My system keeps crashing his crashed yesterday , our crashes daily"))