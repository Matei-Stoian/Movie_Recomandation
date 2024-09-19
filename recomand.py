import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recomander:
    def __init__(self):

        df = pd.read_csv('movie_metadata.csv')
        self.df2 = df.sort_values('imdb_score',ascending=False)
        self.df2['movie_title'] = self.df2['movie_title'].apply(lambda x:str(x).strip()[:-1])
        self.dataset = df[['director_name','actor_1_name','actor_2_name','actor_3_name','genres','plot_keywords','movie_title']]
        self.dataset['movie_title'] = self.dataset['movie_title'].apply(lambda x:str(x)[:-1])
        self.dataset['combine'] = self.dataset['director_name']+' '+self.dataset['actor_1_name']+' '+' '+self.dataset['actor_2_name']+' '+self.dataset['actor_3_name']+' '+self.dataset['genres']
        self.dataset.fillna('',inplace=True)
        vec = CountVectorizer()
        matrix = vec.fit_transform(self.dataset['combine'])
        self.cos_sim = cosine_similarity(matrix)



    def get_recomandation(self,movie):
        if movie not in self.dataset['movie_title'].unique():
            l = ['Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies']
            return l
        else:
            i = self.dataset.loc[self.dataset['movie_title']==movie].index[0]
            lst = list(enumerate(self.cos_sim[i]))
            lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
            l = []
            for i in lst:
                if len(l)>10:
                    break
                a = i[0]
                if self.dataset['movie_title'][a] not in l:
                    l.append(self.dataset['movie_title'][a])
            return l
    def get_top_recomand(self):
        return self.df2['movie_title'].unique()[0:11]
    
    def get_title(self):
        return self.dataset['movie_title'].values


if __name__ == '__main__':
    a = Recomander()
    print(a.get_recomandation('King Kong'))