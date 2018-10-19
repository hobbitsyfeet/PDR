import numpy as np
from test_doc import test_doc
from document import Document


class TermDocumentMatrix():
    """ Rows correspond to terms and columns to documents
    """

    def __init__(self, document_list):
        self.document_info = [{}]
        self.terms = []
        
        # Frequency matrix 
        self.matrix = None
        self.matrix_str = ""
        
        self.get_terms(document_list)
        self.construct_matrix(document_list)

        # Singular value decompisition
        self.U, self.S, self.Vt = np.linalg.svd(self.matrix)
        self.S = np.diag(self.S)

    def get_terms(self, document_list):
        """ Fill terms array with all unique terms
        """
        s = set()
        for d in document_list:
            s = s.union(set(d.text.split()))
        self.terms = list(s)
    
    def construct_matrix(self, document_list):
        """ Fill the (i,j)th entry with the number of occurrences of 
            term i in document j
        """
        self.matrix = np.matrix([[0]*len(document_list)]*len(self.terms))
        for i, t in enumerate(self.terms):
            for j, d in enumerate(document_list):
                self.matrix.A[i][j] = d.text.count(t)
        s = ""
        r, c = self.matrix.shape
        for i in range(r):
            for j in range(c):
                s += str(self.matrix.A[i][j]) + ','
            s = s[:-1] + ';'
        self.matrix_str = s[:-1]

    def reduce_rank(self, k):
        """ Find an approximation to the frequency matrix by keeping
            only those entries in matrices U, and Vt corresponding to
            the largest k entries in the singular value matrix. 
        """
        pass

    def query(self, query_string, num_results):
        """ Given a query string, return a list of num_results indicating the
            closest matching documetns
        """
        pass    
    
    
if __name__ == '__main__':
    doc_list = [Document(x) for x in test_doc]
    tdm = TermDocumentMatrix(doc_list)
    
    
    
