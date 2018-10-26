from document import Document
import os

#creates a path and overwrites the existing document
def createFile(name):
	if not os.path.isdir("./docs"):
		os.mkdir("./docs")
	file = open("./docs/"+name,"w")
	file.close()
	return file


#takes a list of documents and prints them into a file
def exportDocument(docs,name):
	if not os.path.isdir("./docs"):
		os.mkdir("./docs")
	file = open("./docs/"+name,"w")

	for eachDocument in docs:
		file.write(eachDocument.title + "\n")
		for word in eachDocument.text:
			file.write(word)
			file.write (" ")
		file.write("\n")
		file.write(eachDocument.link + "\n")
	#file.close()

def readDocument(name):
	#print("Reading {}...").format(name)
	file = open("./docs/"+name,"r")
	totalTerms = 0
	documents = []

	counter = 0
	for line in file:
		if counter%3 == 0:
			title = line
			title = title.strip('\n')
		if counter%3 == 1:
			text = line
			text = text.strip('\n')
			words = text.split()
			totalTerms = totalTerms + len(words)

		if counter%3 == 2:
			link = line
			link = link.strip('\n')
			documents.append(Document(title,words,link))
		counter = counter + 1


	#file.close()
	#print("Finished Reading " + name)
	#print("For {} documents, {} terms were extracted").format(len(documents), totalTerms)

	return documents
