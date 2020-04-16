#/bin/bash

# for file in ../data/2gram/*-cleaned.csv
# do
#   file=`basename $file`
#   now=`date`
#   echo $now  
#   echo $file
#   python3 find-neongrams.py $file &
# done

ls ../data/2gram/*neon* | \
    rg -o "(..)-cleaned" > already-cleaned.tmp

ls ../data/2gram/ |   \
    rg "cleaned.csv" | \
    rg -v -f already-cleaned.tmp | \
    parallel --jobs 32 --eta python3 find-neongrams.py 
