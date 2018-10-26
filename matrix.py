import numpy as np
import scipy
from test_doc import test_doc
from document import Document


class TermDocumentMatrix():
    """ Rows correspond to terms and columns to documents
    """

    def __init__(self, document_list, k):
        self.document_info = [{}]
        self.term_inds = []
        self.k = k
        
        # Frequency matrix 
        self.matrix = None
        self.matrix_str = ""
        
        self.get_terms(document_list)
        self.construct_matrix(document_list)

        # Singular value decompisition
        print (self.matrix.shape)
        self.U, self.S, self.Vt = scipy.sparse.linalg.svds(
            self.matrix, k=min(min(self.matrix.shape)-1, self.k))

    def get_terms(self, document_list):
        """ Fill terms array with all unique terms
        """
        s = set()
        for d in document_list:
            s = s.union(set(d.text))
        tlist = list(s)
        self.term_inds = {tlist[i]:i for i in range(len(tlist))}
        
    
    def construct_matrix(self, document_list):
        """ Fill the (i,j)th entry with the number of occurrences of 
            term i in document j
        """
        self.matrix = scipy.matrix([[0]*len(document_list)]*len(self.term_inds), dtype=float)

        for doc_ind, doc in enumerate(document_list):
            print("doc: " + str(doc_ind + 1) + " of " + str(len(document_list))) 
            for  term in doc.text:
                self.matrix.A[self.term_inds[term]][doc_ind] += 1
        self.matrix_str = "TODO"

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
    tdm = TermDocumentMatrix(doc_list, 100)
    
    
    
