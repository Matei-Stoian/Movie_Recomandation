import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
ds = pd.read_csv("movie_dataset.csv")


categorys = ["keywords", "director", "cast", "genres"]


def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']


for c in categorys:
    ds[c] = ds[c].fillna('')
ds["combine"] = ds.apply(combine_features, axis=1)


cv = CountVectorizer()
count_matrix = cv.fit_transform(ds["combine"])

sim = cosine_similarity(count_matrix)


def index_from_title(title):
    return ds[ds.title == title]["index"].values[0]


def title_from_index(index):
    return ds[ds.index == index]["title"].values[0]


def get_recomandation(title):
    ind = index_from_title(title)
    s = list(enumerate(sim[ind]))
    s = sorted(s,key = lambda x:x[1],reverse=True)[1:]
    return s
def get_titles():
    return ds["title"].values
if __name__ == '__main__':
    for i in get_titles():
        print(i)