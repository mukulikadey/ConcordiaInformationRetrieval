
import preprocessing
from read_spimi import generate_index_from_files
import score

import functools


def query_single(query):
    index = generate_index_from_files()
    sanitized_query = query.strip().split()

    if len(sanitized_query) == 1:
        normalized_query = preprocessing.all(sanitized_query)

        if normalized_query[0] in index:
            hits = index[normalized_query[0]]["postings"]

            dfts = {}
            dfts[normalized_query[0]] = len(hits)

            scores = score.generate_scores_for_hits(normalized_query, hits, dfts, index)

            print('Number of hits: ', len(scores))
            print('Hits: ', scores)
        else:
            print('No documents found!')


def intersect(a, b):
    return a.intersection(b)


def query_and(query):
    index = generate_index_from_files()
    sanitized_query = query.strip().split()

    postings_lists_list = []
    normalized_query = preprocessing.all(sanitized_query)

    dfts = {}

    for term in normalized_query:
        if term in index:
            hits = index[term]["postings"]
        else:
            hits = []

        postings_lists_list.append(set(hits))
        dfts[term] = len(hits.keys())

    intersection_hits = list(functools.reduce(intersect, postings_lists_list))
    
    scores = score.generate_scores_for_hits(normalized_query, intersection_hits, dfts, index)

    print('Number of hits: ', len(scores))
    print('Hits: ', scores)


def union(a, b):
    return a.union(b)


def query_or(query):
    index = generate_index_from_files()
    query_terms = query.strip().split()

    postings_lists_list = []
    normalized_query = preprocessing.all(query_terms)

    dfts = {}

    for term in normalized_query:
        if term in index:
            hits = index[term]["postings"]
        else:
            hits = []

        postings_lists_list.append(set(hits))
        dfts[term] = len(hits.keys())

    union_hits = list(functools.reduce(union, postings_lists_list))

    scores = score.generate_scores_for_hits(normalized_query, union_hits, dfts, index)

    print('Number of hits: ', len(scores))
    print('Hits: ', scores)

if __name__ == '__main__':
    print('Select one of the options below:')
    print('Single query (1)')
    print('AND query (2)')
    print('OR query (3)')

    option = input('Pick a number: ')

    if option == '1':
        query = input('Query: ')
        query_single(query)
    elif option == '2':
        query = input('Query: ')
        query_and(query)
    elif option == '3':
        query = input('Query: ')
        query_or(query)
