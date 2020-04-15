#/bin/bash

for file in ../data/2gram/*.gz
do
  python3 find-neongrams.py $file &
done
