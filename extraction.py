from bs4 import BeautifulSoup
from document import Document

from NLTKtext import prepare_document

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
			text = text + paragraphs.get_text().encode('utf-8').strip()
		text = prepare_document(text)
		#print(text)
		return text

#returns a list of documents for a given section, printout(T/F) will display summary of contents
def createDocuments(section,printout=False):
	documents = []

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

		#append doc to list of documents
		if printout is True:
			#proof what's contained in doc new
			print("---Contents Exporting---")
			print("Title: " + doc.title)
			print("Link: " + doc.link)
			print("Text: {} ... {} terms\n").format(doc.text[:5], len(doc.text))
		documents.append(doc)
	return documents





#HOW TO USE
#create a list named documents
#documents = []

#Smaller dataset - recomended for testing
#documents = createDocuments("The Python Language Reference",False)

#Larger dataset
#documents.extend(createDocuments("The Python Standard Library",False))
#for docs in documents:
#	print(docs.link)
