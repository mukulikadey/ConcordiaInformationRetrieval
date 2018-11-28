import json
import math
import operator
import os
from afinn import Afinn

afinn = Afinn()

def get_num_docs():
    # Load file and get the number of docs in the collection
    data = dict()
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'concordiacrawler\\spiders\\concordiaData.json')

    try:
        with open(file_path, 'r') as fi:
            inverted_index = dict()
            data = json.load(fi)
    except:
        with open(file_path.replace('\\', '/'), 'r') as fi:
            inverted_index = dict()
            data = json.load(fi)

    num = len(data)

    return num


# This function computes the bm25 score for one document
def get_score(query_parameters):
    N = get_num_docs()

    score = 0

    for query_parameter in query_parameters.values():
        dft = query_parameter['dft']
        tftd = query_parameter['tftd']
        sentiment = query_parameter['sentiment']

        idf = math.log(N / dft)
        tf_idf = idf * tftd

        score += tf_idf * sentiment

    return score / len(query_parameters)


# This function computes the bm25 scores for each document in the hits
def generate_scores_for_hits(query_terms, hits, dfts, index):
    scores = {}

    for url in hits:
        query_parameters = {}

        for term in query_terms:
            query_parameters[term] = {}
            query_parameters[term]['dft'] = dfts[term]
            query_parameters[term]['sentiment'] = index[term]['sentiment']

            if url in index[term]["postings"]:
                query_parameters[term]['tftd'] = index[term]["postings"][url]
            else:
                query_parameters[term]['tftd'] = 0

        scores[url] = get_score(query_parameters)

    query_sentiment = afinn.score(' '.join(query_terms))

    if query_sentiment >= 0:
        return sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    else:
        return sorted(scores.items(), key=operator.itemgetter(1), reverse=False)
