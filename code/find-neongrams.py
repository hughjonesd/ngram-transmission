#!/usr/bin/python3

# find "neongrams" from a cleaned list of Google 2gram data

# config
path = "../data/2gram/"
onegram_path = "../data/1gram/clean-1grams.txt"
start_year = 1850
end_year = 1950
minimum_volumes = 1000

import pandas as pd
import numpy as np

twograms = pd.read_table(path + "cleaned-2grams.txt", columns = ["word1",
                        "word2",  "year", "tokens", "volumes"], na_filter = False)
onegrams = pd.read_table(onegram_path, columns = ["word", "year", "tokens",
                         "volumes"], na_filter = False)

# conditions for a neongram:
# minimum popularity over time
# originates in the study period (1850-2000)?
# more common than expected given the frequency of words over time

twograms.groupby(["word1", "word2"]).aggregate()
