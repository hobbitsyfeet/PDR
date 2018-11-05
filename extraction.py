from bs4 import BeautifulSoup
from document import Document
import export
import os

from NLTKtext import prepare_document

#global variable of local path to python documentation
localDocPath = "python-3.7.1rc2-docs-html/"
print("PATH"+os.getcwd())
with open(localDocPath + "contents.html", 'rb') as html:
	soup = BeautifulSoup (html, features = "html.parser") #create a new BS object

#trims link
def trimSpecifier(link): #returns html link up until "#" specifier
	if link.find("#") != -1:
		return link[ :link.find("#")]
	else:
		return link

#extracts text from a given link
def extractText(link):
	text = ""
	with open(localDocPath + trimSpecifier(link), 'rb') as html:
		soupLink = BeautifulSoup (html, features = "html.parser") #go to the link and then extract text
			#accumulate text from separate paragraphs in document
		for paragraphs in soupLink.find_all("p"):
			text = text + paragraphs.get_text()
		#strips unwanted terms
		list_of_words = prepare_document(text.lower())

		return list_of_words

#returns a list of documents for a given section, printout(T/F) will display summary of contents
def createDocuments(section,printout=False):
	termCounter = 0
	documents = []

	#if there is a file, collect it's contents
	if os.path.isfile("./docs/"+section):
		documents = export.readDocument(section)
		if printout is True:
			for doc in documents:
				#proof what's contained in doc
				print("---Contents Reading---")
				print("Title: " + doc.title)
				print("Link: " + doc.link)
				print("Text: " + str(doc.text[:5]) + "... " + str(len(doc.text)) + " terms\n")
				termCounter = termCounter + len(doc.text)
			print("Total Terms: " + str(termCounter))

	#else there is no file exported, create the file and collect contents
	else:
		sectionBlock = soup.find("a", text=section) 	#look for this line in contents.html
		referenceContent = sectionBlock.find_next_sibling() #everything within language reference
		duplicateLink = ""	#used to test if previous link == current

		#for each content, get the title, link and text
		for element in referenceContent.find_all("a"):	# find all "a" tags within referenceContent
			title = element.text					#extract the title
			link = element.get("href")				#extract the link matched with title

			#does link exist already - these are subtopics
			if trimSpecifier(duplicateLink) == trimSpecifier(link):
				continue

			#else they are different, create document and reset link for next time
			duplicateLink = link	#new link, used for checking if link is used

			#new Link, new list of titles, new document to download
			print("Creating new document: " + title + " From: " + link)

			#extract the text from the link provided, and create document
			doc = Document(title,extractText(link),link)

			#counter for terms in all the documents
			termCounter = termCounter + len(doc.text)

			if printout is True:
				#proof what's contained in doc new
				print("---Contents Exporting---")
				print("Title: " + doc.title)
				print("Link: " + doc.link)
				print("Text: " + str(doc.text[:5]) + "... " + str(len(doc.text)) + " terms")

				print("Total Terms: " + str(termCounter))

			#append each document to the file
			export.exportDocument(doc,section)

			#append each document to a list
			documents.append(doc)
	#return the list of documents
	return documents
	#Larger dataset
	PSL = createDocuments("The Python Standard Library",False)

	documents.extend(PLR)
	documents.extend(PSL)
