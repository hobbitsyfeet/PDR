#Import Regex package
import nltk

Text = "Peter had a tiny prick, he pissed all about."

import test_doc as text_file

text = ""
for p in text_file.test_doc:
	text += p+" "
#returns a list of important words for document.
def prepare_document(tf):
	word_list = []
	#create a tokenizer that will give us all words.
	search_tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
	#Gives us a list of seperated words.
	tokens = search_tokenizer.tokenize(tf)
	#nltk.download('stopwords')
	#list of common english words that have little meaning.
	stop_words = nltk.corpus.stopwords.words('english')
	#print("Tokens without stopwords removed. \n")
	#print(tokens)
	#print("\nWith stopwords removed.\n")
	for w in tokens:
		if w not in stop_words:
			word_list.append(w.lower())
	#print(word_list)
	return word_list

print(prepare_document(text))
