from extraction import createDocuments
from matrix import TermDocumentMatrix

if __name__ == '__main__':
    print("Starting Process")

    PLR = createDocuments("The Python Language Reference",False)
    PSL = createDocuments("The Python Standard Library",False)
    documents = PLR + PSL

    print("\nEnter k: ", end="")
    k = int(input())
    print("Enter query: ", end="")
    s = input()

    tdm = TermDocumentMatrix(documents, k)
    r = tdm.query(s.lower().split(), 5)
    for i, x in enumerate(r):
        print('----')
        print(str(i + 1) + ": ", end="")
        print(documents[x[1]].title + " - " + str(x[0].A[0][0]))
        print('  ' + documents[x[1]].link)
    print()
