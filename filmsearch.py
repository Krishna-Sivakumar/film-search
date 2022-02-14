import nltk
import pandas
import string
from collections import defaultdict
from functools import reduce
from rich.progress import Progress


class FilmSearch:

    stop = set(nltk.corpus.stopwords.words(
        'english') + list(string.punctuation))

    def __init__(self):
        self.filmset = defaultdict(list)

    def atomize(self, title: str):
        return [
            i for i in nltk.word_tokenize(title.lower()) if i not in self.stop
        ]

    def load_dataset(self):
        print("loading dataset...")
        table = pandas.read_csv('title.basics.tsv', sep='\t')
        self.titles = table.loc[table['titleType'] ==
                                'movie'][['tconst', 'primaryTitle']]
        print("finished loading dataset.")

    def build_filmset_in_memory(self):
        with Progress() as progress:
            loader = progress.add_task(
                "[cyan]processing records...", total=len(self.titles))
            for _, row in self.titles.iterrows():
                for atom in self.atomize(row['primaryTitle']):
                    self.filmset[atom].append(row['tconst'])
                progress.update(loader, advance=1)

    def search_in_memory(self, title: str):
        atoms = self.atomize(title.lower())
        return reduce(
            lambda acc, atom: acc.intersection(set(self.filmset[atom])),
            atoms[1:],
            set(self.filmset[atoms[0]])
        )
