#/usr/bin/python3

import string
import requests
import os.path

data_dir = "../data"

# download all the 5gram files
letters = list(string.ascii_lowercase)
first_letters = [s1 + s2 for s1 in letters for s2 in letters]

for fl in first_letters:
  url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20120701-%s.gz" % fl
  local_path = "%s/googlebooks-eng-all-5gram-20120701-%s.gz" % (data_dir, fl)
  if os.path.isfile(local_path):
    continue 
  req = requests.get(url)   
  file = open(local_path, 'wb')
  for chunk in req.iter_content(100000):
    file.write(chunk)
  file.close()
  print("Stored file " + fl + "\n") 
