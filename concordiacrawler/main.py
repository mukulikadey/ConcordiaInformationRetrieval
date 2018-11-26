import json
import os
from glob import iglob
from spimi import SPIMI

if __name__ == '__main__':

    block_size_limit = 500
    print("=============== Retriving data =============== ")
    # data = dict()
    # script_dir = os.path.dirname(__file__)
    # file_path = os.path.join(script_dir, 'concordiacrawler\\spiders\\concordiaData.json')
    # with open(file_path, 'r') as fi:
    #     data = json.load(fi)

    print("=============== Apply Spimi =============== ")
    # spimi = SPIMI(block_size_limit, data)
    # spimi.invert()
