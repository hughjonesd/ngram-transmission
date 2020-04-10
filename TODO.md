

# Plan to identify ngrams to books

* Use google books API to find ngrams which are unique to a book
* With a sample of your "long" and "short" ngrams that are unique to a book,
  classify the book by e.g. its intended audience, difficulty etc... maybe using
  a snippet?
* Need to use the sample that actually contains the neongrams...

* Could also just work with ngrams that are unique... but finding many may run
  up against TOS violations of API...

Books API lets you look up volumes by search terms:
https://www.googleapis.com/books/v1/volumes?q=search+terms&key=your_API_key


# Main plan

* Split 5-grams into long and short by length of first word. Take equal-size samples of
  both. (Maybe
* Take the last 2 words of these 5-grams. Summarize counts over the 5-grams.
* Find neongrams from 2-gram data: for each 2 gram, find year of first use.
* Show whether this is more likely to be in the "long" or "short" sample.
* Examine dynamics of spread from "long" to "short" (via "intermediate"?) over time

* (Maybe:) look at word associations using embeddings. Do the associated concepts
  get closer over time after the neongram?
  - Idea is that word associations are known to relate to psychology, via *that paper*

## Questions

* Does this prove it is actually from an "intellectual" book? One answer is as above.
* 
