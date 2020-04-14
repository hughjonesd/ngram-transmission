#/bin/sh

cd ../data/1gram

zcat *.gz > all-1grams.txt
grep -P "^[a-z]+\t" all-1grams.txt > clean-1grams.txt
aspell -l en dump master | aspell -l en expand > aspell-wordlist.txt
grep -w -f aspell-wordlist.txt clean-1grams.txt > word-1grams.txt

cd ../code
