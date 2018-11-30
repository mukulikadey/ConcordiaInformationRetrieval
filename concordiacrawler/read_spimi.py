from collections import OrderedDict, defaultdict
from glob import iglob
import json


def generate_index_from_files():
    files_paths = []
    index = defaultdict(list)

    for file_path in iglob('DISK/BLOCK*.txt'):
        files_paths.append(file_path)

    for file in files_paths:
        with open(file, 'r') as file:
            block_object = json.load(file)
            #index.update(block_object) update would not take into consideration duplicate keys
            for key, value in block_object.items():
                index[key].append(value) #if the key already exists in the index, append its values so we don't lose any information

    ord = OrderedDict(index) #It is not sorted though
    return ord
