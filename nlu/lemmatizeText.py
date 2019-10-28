import spacy 
nlp = spacy.load('en_core_web_md', parse=True, tag=True, entity=True)

def lemmatize_text(text):
	text = nlp(text)
	text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
	return text

#print(lemmatize_text("My system keeps crashing! his crashed yesterday, ours crashes daily"))