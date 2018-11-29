import os
import sys
from matrix import TermDocumentMatrix, TFIDF_Matrix
from extraction import createDocuments
from NLTKtext import prepare_document

""" Run with:
    python3 0 < input_file > output_file    for term frequency weights
    python3 1 < input_file > output_file    for tf-idf weights

    The first line of the input file should be the number of comments. The first word of each 
    comment should be the name of the function.
"""

if __name__ == '__main__':
    PLR = createDocuments("The Python Language Reference",False)
    PSL = createDocuments("The Python Standard Library",False)
    documents = PSL + PLR

    if sys.argv[0] != 2:
        raise RuntimeError('Missing argument')
    
    k = 50
    tdm = None
    if sys.argv[1] == '1':
        tdm = TFIDF_Matrix(documents, k)
    else:
        tdm = TermDocumentMatrix(documents, k)

    n = int(input())
    for i in range(n):
        comment = input()
        title = comment.split()[0]
        query = prepare_document(comment)
        result = tdm.query(query, 5)
    
        for i, x in enumerate(result):
            print(str(i + 1) + ": ", end="")
            print(documents[x[1]].title + " - " + str(x[0].A[0][0]))
            print('  ' + documents[x[1]].link + "$")
        print()