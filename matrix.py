from test_doc import test_doc
from document import Document

class TermDocumentMatrix():
    def __init__(self):
        self.td_freq = []
        self.links = []
        self.terms = set()

    def get_terms(self, document_list):
        for d in document_list:
            self.terms = self.terms.union(set(d.text.split()))
    
    def count_terms(self, document_list):
        for d in document_list:
            row = { t:0 for t in self.terms }
            for t in d.text.split():
                row[t] += 1
            self.td_freq.append(row)

    def print_all(self):
        for s in self.terms:
            print(s, end="\t")
        print()
        for row in self.td_freq:
            for k in row:
                print(row[k], end="\t")
            print()
            
if __name__ == '__main__':
    doc_list = [Document(x) for x in test_doc]
    matrix = TermDocumentMatrix()
    matrix.get_terms(doc_list)
    matrix.count_terms(doc_list)
    matrix.print_all()
    
    
    
