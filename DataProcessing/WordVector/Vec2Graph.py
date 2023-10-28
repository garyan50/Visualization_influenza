import pickle
from datetime import datetime

from vec2graph import visualize
import gensim
import umap
from gensim.models import KeyedVectors, Word2Vec
import pandas as pd
import scattertext as st

import spacy
from gensim.models import word2vec
from scattertext import SampleCorpora, word_similarity_explorer_gensim, Word2VecFromParsedCorpus, dense_rank

w2vmodel2019 = gensim.models.Word2Vec.load("w2vmodel2019")
w2vmodel2020_clean = gensim.models.Word2Vec.load("w2vmodel2020_clean")
ftmodel2020 = gensim.models.FastText.load("ftmodel2020")




w2vmodel2019.wv.save_word2vec_format("2019" + '.model.bin', binary=True)  # C binary format 磁盘空间比上一方法减半
w2vmodel2020_clean.wv.save_word2vec_format("2020" + '.model.bin', binary=True)  # C binary format 磁盘空间比上一方法减半
ftmodel2020.wv.save_word2vec_format("2020" + '.model.bin', binary=True)  # C binary format 磁盘空间比上一方法减半
#

model2019 = gensim.models.KeyedVectors.load_word2vec_format('2019clean.model.bin', binary=True)
visualize('temp/graphs/2019', model2019, 'influenza', depth=1, topn=10, edge=1)

model2020 = gensim.models.KeyedVectors.load_word2vec_format('2020clean.model.bin', binary=True)
visualize('temp/graphs/2020', model2020, 'influenza', depth=1, topn=10, edge=1)
#
file = open("data_2019_clean_stop.pkl", 'rb')
data2019 = pickle.load(file)
data2019_label = []
for i in range(len(data2019)):
    data2019_label.append("2019")

sentences_2019 = []
for i in data2019:
    sentences_2019.append(" ".join(i))

file = open("data_2020_clean_stop.pkl", 'rb')
data2020 = pickle.load(file)
data2020_label = []
for i in range(len(data2020)):
    data2020_label.append("2020")

sentences_2020 = []
for i in data2020:
    sentences_2020.append(" ".join(i))

word2vec = gensim.models.Word2Vec
fasttext = gensim.models.FastText
#
for i in sentences_2020:
    sentences_2019.append(i)

for i in data2020_label:
    data2019_label.append(i)

print(len(data2019))
print(len(data2020))


data_dict = {'sentences': sentences_2019, 'category': data2019_label}

data_frame = pd.DataFrame(data_dict)

print("df done")
#
data_frame.to_pickle("./data_frame_clean.pkl")


data_frame = pd.read_pickle("data_frame_clean.pkl")
#
# from random import sample
#
data_frame1 = data_frame.iloc[sample(range(1134222), 1500), :]
data_frame2 = data_frame.iloc[sample(range(1134223,1926000), 1500), :]
import numpy as np

chosen_idx1 = np.random.choice(1134223, 5000, replace=False)
chosen_idx2 = np.random.choice(792501, 5000, replace=False)
chosen_idx2 = list(chosen_idx2)
chosen_idx1 = list(chosen_idx1)

idx2 = []
for i in chosen_idx2:
    idx2.append(i + 1134222)

print(len(chosen_idx2))
print(len(chosen_idx1))
idx = chosen_idx1 + idx2
print(idx)

data_frame_sample = data_frame.iloc[idx]
print("df sample done")
sub_ = data_frame.iloc[:5000, :]
sub_2 = data_frame.iloc[-5000:, :]
start = datetime.now()
frames = [sub_, sub_2]
data_frame = pd.concat(frames)
print("data_frame build time: " + str(datetime.now() - start))
data_frame = data_frame.sample()
import spacy
#
nlp = spacy.load('en')
print(data_frame.head())
data_frame['parsed'] = data_frame.sentences.apply(nlp)
print(data_frame)
print("parse done")
data_frame.to_pickle("./parsed.pkl")

# data_frame= pd.read_pickle("parsed.pkl")
# start = datetime.now()
# print(data_frame)
data_frame = data_frame_sample
print("assign done")
corpus = st.CorpusFromParsedDocuments(
    data_frame,
    category_col='category',
    parsed_col='parsed',
).build()
print("corpus done")
pd.set_option('display.max_columns', None)
print(data_frame)
print("corpus build time: " + str(datetime.now() - start))
start = datetime.now()
#
model = Word2Vec(size=100, window=5, min_count=5, workers=4)

html = st.produce_frequency_explorer(
    corpus,
    category='2020',
    category_name='2020',
    not_category_name='2019',
    term_scorer=st.CohensD(corpus),
    grey_threshold=0
)

open("temp/Plot_clean_remove_stop/effect-size-10000.html", 'wb').write(html.encode('utf-8'))

html = st.word_similarity_explorer_gensim(corpus,
                                          category='2020',
                                          category_name='2020',
                                          not_category_name='2019',
                                          target_term='influenza',
                                          minimum_term_frequency=5,
                                          pmi_threshold_coefficient=4,
                                          width_in_pixels=1000,
                                          word2vec=Word2VecFromParsedCorpus(corpus, model).train(),
                                          max_p_val=0.05,
                                          save_svg_button=True)

open("temp/Plot_clean/Sim-influenza-10000.html", 'wb').write(html.encode('utf-8'))

html = st.produce_projection_explorer(corpus,
                                      word2vec_model=model,
                                      projection_model=umap.UMAP(min_dist=0.5, metric='cosine'),
                                      category='2020',
                                      category_name='2020',
                                      not_category_name='2019',
                                      )
open("temp/Plot_clean_remove_stop/Projection-10000.html", 'wb').write(html.encode('utf-8'))

# print("html build time: " + str(datetime.now() - start))
