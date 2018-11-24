import json
import get_content
import preprocessing
from spimi import SPIMI

def dump_bm25_param(documents):
    num_documents = len(documents.keys())
    doc_len = {}
    sum_len = 0

    for docId, terms_list in documents.items():
        length = len(terms_list)
        doc_len[docId] = length
        sum_len += length

    avg_len = sum_len / num_documents

    bm25_param = {
        'num_documents': num_documents,
        'doc_len': doc_len,
        'avg_len': avg_len
    }

    with open('bm25_param.txt', 'w') as f:
        json.dump(bm25_param, f)

if __name__ == '__main__':

    block_size_limit = 500
    print("=============== Retriving documents =============== ")
    documents = get_content.getDocuments()
    # print(documents)
    print("=============== Preprocessing documents ===========")
    documents = preprocessing.preprocess(documents)
    dump_bm25_param(documents)
    # print(documents)
    print("=============== Applying SPIMI Algorithm ==========")
    spimi = SPIMI(block_size_limit, documents)
    spimi.invert()