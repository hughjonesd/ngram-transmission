#!/usr/bin/python3

# create a raw list of neongrams by finding the first year a 2gram is recorded

import datetime
import os
import gzip

# CONFIGURATION:
path = "../data/2gram"

# only accept neongrams that are visible in this many volumes in total
min_volumes = 5000
# only accept neongrams starting after this year as truly new
earliest_year = 1850
# count min_volumes within this many years after the first year
max_period = 100

# PROGRAM



def maybe_print_output(words, first_year, volumes):
  if volumes >= min_volumes:
    print("%s\t%s\t%s\t%s" % (words[0], words[1], first_year, volumes))

def process_gzip(file_path):
  print(datetime.datetime.now().time())
  with gzip.open(file_path, 'rt') as handle:
    content = handle.readlines()

  cur_words = ['', '']
  volumes = -1
  first_year = 0
  for line in content:
    fields = line.split() # first two words are space separated. Then there's tabs.

    # skip invalid words
    if not (fields[0].isalpha() and fields[0].islower() and fields[1].isalpha()
	  and fields[1].islower()): 
      continue

    if fields[0:2] != cur_words:
      # new 2gram
      # first evaluate current 2gram 
      maybe_print_output(cur_words, first_year, volumes) 
      cur_words = fields[0:2]
      first_year = int(fields[2])
      volumes = int(fields[4])
    else:
      # existing 2gram
      if first_year >= earliest_year and int(fields[2]) <= earliest_year + max_period: 
        volumes += int(fields[4])


# main loop:
for file in os.listdir(path):
  file_path = path + "/" + file
  process_gzip(file_path)

