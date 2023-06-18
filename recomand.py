import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
class Recomander:
    def __init__(self):
        self.ds = pd.read_csv("movie_dataset.csv")
        categorys = ["keywords", "director", "cast", "genres"]
        for c in categorys:
            self.ds[c] = self.ds[c].fillna('')
        self.ds["combine"] = self.ds.apply(combine_features,axis=1)
        cv = CountVectorizer()
        matrix = cv.fit_transform(self.ds["combine"])
        self.cos_sim = cosine_similarity(matrix)
    def index_from_tile(self,title):
        return self.ds[self.ds.title == title]["index"].values[0]
    def title_from_index(self,index):
        return self.ds[self.ds.index == index]["title"].values[0]
    def get_titles(self):
        return self.ds["title"].values
    def get_recomandation(self,title):
        ind = self.index_from_tile(title)
        l = list(enumerate(self.cos_sim[ind]))
        l = sorted(l,key=lambda x:x[1],reverse=True)[1:]
        return l