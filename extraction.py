from bs4 import BeautifulSoup
from document import Document
import export
import os
from imp import reload

from NLTKtext import prepare_document

# encoding=utf8
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')




#global variable of local path to python documentation
localDocPath = "python-3.7.1rc2-docs-html/"

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
		for paragraphs in soupLink.find_all("p"):
			text = text + paragraphs.get_text()
			#text = text.
		text = prepare_document(text)
		#print(text)

		return text

#returns a list of documents for a given section, printout(T/F) will display summary of contents
def createDocuments(section,printout=False):
	termCounter = 0
	documents = []
	if os.path.isfile("./docs/"+section):
		documents = export.readDocument(section)
		if printout is True:
			for doc in documents:
				#proof what's contained in doc new
				print("---Contents Exporting---")
				print("Title: " + doc.title)
				print("Link: " + doc.link)
				print("Text: {} ... {} terms\n").format(doc.text[:5], len(doc.text))
				termCounter = termCounter + len(doc.text)
			print("Toal Terms: {}").format(termCounter)





	else:
		#find python language reference and grab contents
		sectionBlock = soup.find("a", text=section) 	#look for this line in contents.html
		referenceContent = sectionBlock.find_next_sibling() #everything within language reference
		duplicateLink = ""	#used to test if previous link == current

		#for each content, get the title, link and text
		for element in referenceContent.find_all("a"):	# find all "a" tags within referenceContent

			link = element.get("href")				# extract the link matched with title
			title = element.text

			#does link exist already - these are subtopics
			if trimSpecifier(duplicateLink) == trimSpecifier(link):
				continue
			#else they are different, create document and reset link for next time
			duplicateLink = link	#new link, used for checking if link is used

			#new Link, new list of titles, new document to download
			print("Creating new document: " + title + " From: " + link)

			#extract the text from the link provided, and create document
			doc = Document(title,extractText(link),link)

			termCounter = termCounter + len(doc.text)
			#append doc to list of documents
			if printout is True:
				#proof what's contained in doc new
				print("---Contents Exporting---")
				print("Title: " + doc.title)
				print("Link: " + doc.link)
				print("Text: {} ... {} terms\n").format(doc.text[:5], len(doc.text))
				termCounter = termCounter + len(doc.text)
				print("Toal Terms: {}").format(termCounter)

			documents.append(doc)
		export.exportDocument(documents,section)
	return documents


if __name__ == '__main__':
	print("Starting Process")

	#HOW TO USE
	#create a list named documents
	documents = []
	#Smaller dataset - recomended for testing
	PLR = createDocuments("The Python Language Reference",False)

	#Larger dataset
	PSL = createDocuments("The Python Standard Library",False)

	documents.extend(PLR)
	documents.extend(PSL)
