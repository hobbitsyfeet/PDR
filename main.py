import os
import sys
from matrix import TermDocumentMatrix, TFIDF_Matrix
from extraction import createDocuments
if __name__ == '__main__':


    #print("Starting Process")

    PLR = createDocuments("The Python Language Reference",False)
    PSL = createDocuments("The Python Standard Library",False)
    documents = PSL

    k = 0
    try:
        s = sys.argv[1]
        print("From: " + s + "$")
    except:
        print("\nEnter k: ", end="")
        k = int(input())
        print("Enter query: ", end="")
        s = input()

    if k is 0:
        k = 50

    # tdm = TermDocumentMatrix(documents, k)
    tdm = TFIDF_Matrix(documents, k)
    r = tdm.query(s.lower().split(), 5)
    for i, x in enumerate(r):
        print(str(i + 1) + ": ", end="")
        print(documents[x[1]].title + " - " + str(x[0].A[0][0]))
        print('  ' + documents[x[1]].link + "$")
    print()
