#
import os
import sys


from matrix import TermDocumentMatrix
from extraction import createDocuments
if __name__ == '__main__':
    

    #print("Starting Process")

    PLR = createDocuments("The Python Language Reference",False)
    PSL = createDocuments("The Python Standard Library",False)
    documents = PSL

    #print("\nEnter k: ", end="")
    
    k = 50
    #print("Enter query: ", end="")
    try:
        s = sys.argv[1]
        print("From: " + s + "$")
    except:
        print("Enter query: ", end="")
        s = input()

    #print(s)
    tdm = TermDocumentMatrix(documents, k)
    r = tdm.query(s.lower().split(), 5)
    for i, x in enumerate(r):
        print(str(i + 1) + ": ", end="")
        print(documents[x[1]].title + " - " + str(x[0].A[0][0]))
        print('  ' + documents[x[1]].link + "$")
    print()