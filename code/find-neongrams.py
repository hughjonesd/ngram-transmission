#!/usr/bin/python3

# create a raw list of neongrams by finding the first year a 2gram is recorded

import os
import gzip

# CONFIGURATION:
path = "../data/2gram"

# only accept neongrams that are visible in this many volumes in total
min_volumes = 50000
# only accept neongrams starting after this year as truly new
earliest_year = 1850

# PROGRAM

cur_words = ['', '']
volumes = 0
cur_line = ''
already_printed = False

for file in os.listdir(path):
  file_path = path + "/" + file
  with gzip.open(file_path, 'rt') as handle:
    
    for line in handle:
      fields = line.split() # first two words are space separated. Then there's tabs.
      
      # skip invalid words
      if not (fields[0].isalpha() and fields[0].islower() and fields[1].isalpha()
            and fields[1].islower()): 
        continue

      if fields[0:1] != cur_words:
        # new potential neongram
        cur_line = line
        cur_words = fields[0:1]
        first_year = int(fields[2])
        volumes = int(fields[4])
        already_printed = False
      else:
        # existing 2gram
        if first_year >= earliest_year and not already_printed:
          volumes += int(fields[4])
          if volumes >= min_volumes:
            print(cur_line, end = '')
            already_printed = True

# we'd like to have "reliable" recording - maybe from 1850 or so
# also ignore misprints... so they should exist for at least 20 years
