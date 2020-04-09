#/usr/bin/python3

import string
import os.path
import subprocess
import sys


# download ngram files from google 

def usage():
  print("Usage: download.py [n] where n is 1-5 for the relevant n-grams")
  sys.exit()

n_in_ngram = sys.argv[1]

try:
  int(n_in_ngram)
except:
  usage()
if not (1 <= int(n_in_ngram) <= 5):
  usage()

data_dir = "../data/%sgram" % n_in_ngram 

first_letters = list(string.ascii_lowercase)
if int(n_in_ngram) > 1:
  first_letters = [s1 + s2 for s1 in first_letters for s2 in first_letters]

for fl in first_letters:
  url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-%sgram-20120701-%s.gz" % (n_in_ngram, fl)
  local_path = "%s/googlebooks-eng-all-%sgram-20120701-%s.gz" % (data_dir, n_in_ngram, fl)
  if os.path.isfile(local_path):
    print("Already got file " + fl)
    continue 
  res = subprocess.call(["wget", "-P", data_dir,  url])
  if res != 0:
    print("FAILED TO DOWNLOAD " + url)
  else:
    print("Stored file " + fl) 
