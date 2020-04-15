#!/usr/bin/python3

# find "neongrams" from a cleaned list of Google 2gram data


# config
path = "../data/2gram/"
onegram_path = "../data/1gram/word-1grams.txt"

start_year = 1850
end_year = 1950
year_range = 50
min_vols_pa = 10

# for testing
twogram_nrows = 1e9

import pandas as pd
import numpy as np
import csv
import sys

twogram_path = path + sys.argv[1]
output_path = twogram_path[:-3] + "neongrams.csv"

onegrams = pd.read_table(onegram_path, names = ["word", "year", "tokens",
                         "volumes"], na_filter = False)
onegrams = onegrams[(onegrams["year"] >= start_year) & (onegrams["year"] <=
                    end_year)]
word_pop = onegrams.groupby("word")["volumes"].sum()/(end_year - start_year)
word_pop = word_pop.to_frame()

twograms = pd.read_table(twogram_path, names = ["word1",
                        "word2",  "year", "tokens", "volumes"], 
                         usecols = ["word1", "word2", "year", "volumes"],
#                         na_filter = False)
                          na_filter = False, nrows = twogram_nrows)

# conditions for a neongram:
# minimum popularity over time
# more common than expected given the frequency of words over time
# originates in the study period (start_year to end_year)?


twograms["first_year"] = twograms.groupby(["word1", "word2"])["year"] \
        .transform("min")
twograms.query("first_year > @start_year & first_year < @end_year", inplace = True)
twograms["total_volumes"] = twograms \
        .query("year >= first_year & year <= first_year + @year_range") \
        .groupby(["word1", "word2"])["volumes"]\
        .transform("sum")
# fill in NA values because the query above left some holes:
twograms["total_volumes"] = twograms.groupby(["word1",
        "word2"])["total_volumes"].transform("max")
twograms["vols_pa"] = twograms["total_volumes"] / year_range

twograms = twograms[twograms["vols_pa"] > min_vols_pa]

twograms = (
    twograms.merge(word_pop, left_on = "word1", right_on = "word",
                   suffixes = ("", "_word1")) 
    .merge(word_pop, left_on = "word2", right_on = "word",
                   suffixes = ("", "_word2"))
)

twograms["rel_pop"] = twograms["vols_pa"]/(twograms["volumes_word1"] * 
                                           twograms["volumes_word2"])

twograms.drop(["year", "volumes"], axis = 1, inplace = True)
twograms.drop_duplicates(subset = ["word1", "word2"], inplace = True)
twograms.sort_values("rel_pop", ascending = False, inplace = True)

# sanity check
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(twograms.head(40))

twograms.to_csv(output_path, sep = "\t", index = False, quoting =
                csv.QUOTE_NONE)

