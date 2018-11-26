import json
import os
from spimi import SPIMI
from preprocessing import normalize

if __name__ == '__main__':

    block_size_limit = 500
    print("=============== Retriving data =============== ")
    data = dict()
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'concordiacrawler\\spiders\\concordiaData.json')
    with open(file_path, 'r') as fi:
        inverted_index = dict()
        data = json.load(fi)

    print("=============== Normalize data =============== ")
    new_dict = dict()
    for entry in data:
        url = entry["url"]
        content = entry["content"]
        new_dict[url] = content

    for key, value in new_dict.items():
        new_dict[key] = normalize((value[0]))

    print(new_dict)

    print("=============== Apply Spimi =============== ")
    spimi = SPIMI(block_size_limit, new_dict)
    spimi.invert()
