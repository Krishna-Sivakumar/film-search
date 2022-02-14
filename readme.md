### FilmSearch

---

A toy implementation of an inverted index search for movie titles on IMDb.

I used the basic titles dataset, available as `title.basics.tsv.gz` [here.](https://www.imdb.com/interfaces/)

As this is still in ideation and development, I've designed the interface with a live environment in mind. I'm probably gonna change this later.

**To Setup (on NIX systems):**
```shell
virtualenv .env
source .env/bin/activate
pip -r requirements.txt
wget https://datasets.imdbws.com/title.basics.tsv.gz
gunzip title.basics.tsv.gz
```

---

**Usage:**


To initialize the `FilmSearch` class:
```python
f = FilmSearch()
```

To load the data and build the inverted index:
```python
f.load_dataset()
f.build_filmset_in_memory()
```

Once the index has been built, you can search it.
Here's how to do it:
```python
resut = f.search_in_memory("Captain America: The Winter Soldier") # Tokenizes the string, and removes stopwords and punctuation marks.

# The result is a set of IMDb film indices.

print(result) # {'tt1843866'}
```

