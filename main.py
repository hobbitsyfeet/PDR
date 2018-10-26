from extraction import createDocuments
from matrix import TermDocumentMatrix

if __name__ == '__main__':
    print("Starting Process")
    PLR = createDocuments("The Python Language Reference",False)
    PSL = createDocuments("The Python Standard Library",False)
    documents = PLR + PSL
    TDMatrix = TermDocumentMatrix(documents, 100)
