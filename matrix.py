import scipy
import numpy as np
import math
from scipy import linalg
from scipy.sparse import linalg
from test_doc import test_doc
from document import Document


def cosine_rank(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def singular_value_decomp(matrix, k):
    """ Singular value decompisition
        U  - unitary matrix 
        S  - diagonal matrix containing k - largest singular values
        Vt - transpose of document vectors 
    """
    smaller_dim = min(matrix.shape)
    # if k too large, keep as many as possible
    k = min( smaller_dim - 1, k)
    U, S, Vt = scipy.sparse.linalg.svds(matrix, k)
    S = scipy.matrix(np.diag(S))
    return U, S, Vt


class TermDocumentMatrix():
    """ Rank-k approximation to the term-document matrix for a given set of documents.
        Rows correspond to terms and columns to documents.
    """
    def __init__(self, document_list, k):
        self.term_inds = {}
        self.k = k
        self.matrix = None
        self.get_terms(document_list)
        self.construct_matrix(document_list)
        self.U, self.S, self.Vt = singular_value_decomp(self.matrix, self.k)

    def get_terms(self, document_list):
        """ Fill term_inds map with an index for each unique term
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
        self.matrix = scipy.matrix(
            [ [0] * len(document_list)] * len(self.term_inds), 
            dtype=float)

        for j, doc in enumerate(document_list):
            for term in doc.text:
                i = self.term_inds[term]
                self.matrix.A[i][j] += 1


    def query(self, query_words, num_results = -1):
        """ Given a list of words in a query return a list of num_results indicating the
            closest matching documents. By default return all
        """
        q = [0] * len(self.term_inds)
        term_set = set(self.term_inds.keys())

        for word in query_words:
            if word in term_set:
                q[self.term_inds[word]] += 1

        q = scipy.matrix(q)
        sig_inv = scipy.linalg.inv(self.S).transpose()

        # Need to transform q the same way we transformed the initial matrix
        q_transform = q * self.U * sig_inv

        # compute cosine similarity for each document vector
        rank = []
        for i, v in enumerate(self.Vt.transpose()):
            rank.append((cosine_rank(q_transform, v), i))

        rank.sort(reverse=True)

        n = min(len(rank), num_results)
        if num_results == -1:
            n = len(rank)

        return rank[:n]


class TFIDF_Matrix(TermDocumentMatrix):

    def __init__(self, document_list, k):
        self.term_inds = []
        self.k = k
        self.matrix = None
        self.get_terms(document_list)
        self.construct_matrix(document_list)
        self.U, self.S, self.Vt = singular_value_decomp(self.matrix, self.k)

    def construct_matix(self, document_list):
        self.matrix = scipy.matrix(
            [[0] * len(document_list)] * len(self.term_inds), dtype=float)

        idf = [0] * len(self.term_inds)
        # Count the number of documents containing the term 
        for term in self.term_inds.keys():
            for doc in document_list:
                if term in doc.text:
                    idf[self.term_inds[term]] += 1
        
        # idf(term) = log (total number of docs / number of docs containing term)
        for term in idf.keys():
            idf[term] = math.log(len(document_list) / idf[term])

        for j, doc in enumerate(document_list):
            for term in doc.text:
                i = self.term_inds[term]
                self.matrix.A[i][j] += 1

        # tf-idf(term, doc) = term-count * idf(term)
        for i in range(len(self.matrix.A)):
            for j in range(len(i)):
                self.matrix.A[i][j] *= idf[i]