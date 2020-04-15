#!/usr/bin/python3

import os
import pandas as pd
import numpy as np
import re
import csv
import subprocess

path = "../data/2gram/"
onegram_path = "../data/1gram/"
csv_output_file = 'cleaned-2grams.txt'

onegrams = pd.read_table(onegram_path + "word-1grams.txt", 
                         names = ["word", "year", "tokens", "volumes"],
                         na_filter = False)
dictionary = onegrams["word"].unique()


def process_gzip(file_path):
    subprocess.run(["gunzip", "-k", file_path])
    file_path = file_path[:-3]

    first_clean_path = file_path + ".cleaned.tmp"
    with open(first_clean_path, 'w') as first_clean:
        subprocess.run(["rg", "^[a-z]+ [a-z]+\\s", file_path], stdout =
                       first_clean)
    with open(first_clean_path, 'rt') as first_clean:
        content =  pd.read_table(first_clean, sep = '\s+', names = ["word1",
                "word2", "year", "tokens", "volumes"]) 

    # throw out all non-dictionary words 
    content = content[content["word1"].isin(dictionary)]
    content = content[content["word2"].isin(dictionary)]

    os.remove(first_clean_path)
    os.remove(file_path)

    return content


# main loop:
with open(path + '/' + csv_output_file, 'w') as csv_output:
    for file in sorted(os.listdir(path)):
        if re.search(r'gz$', file) is None:
            continue
        file_path = path + "/" + file
        print(file)
        process_gzip(file_path).to_csv(csv_output, header = False, 
                                       index = False, sep = '\t', 
                                       quoting = csv.QUOTE_NONE)
