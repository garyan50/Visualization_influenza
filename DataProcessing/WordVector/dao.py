import pymongo
import pandas as pd
import pickle
import gensim
from gensim.parsing.preprocessing import remove_stopwords

mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

print(mongo_client.server_info())  # 判断是否连接成功

collection = mongo_client["FluRelatedTweets2020"]["tweet"]
all_data = collection.find()

dataset = []
#
count = 0
for i in all_data:
    sentence = i['text']
    print("---------" + str(count) + "-----------")
    # filtered_sentence = remove_stopwords(sentence)
    dataset.append(sentence.split())
    count = count + 1


import time

word2vec = gensim.models.Word2Vec
fasttext = gensim.models.FastText

start = time.clock()
model = word2vec(twitter_dataset, size=100, window=5, min_count=5, workers=4)
model.save("w2vmodel2019")
model = word2vec.load("w2vmodel2020")
model = fasttext(twitter_dataset, size=100, window=5, min_count=5, workers=4)
model.save("ftmodel2019")
model = fasttext.load("ftmodel2020")
end = time.clock()
print('Running time: %s Seconds' % (end - start))

for i in model.wv.most_similar(u"wuhan"):
    print(i[0], i[1])

model_2019_w2v = word2vec.load("w2vmodel2019")
model_2019_w2v_clean = word2vec.load("w2vmodel2019_clean")
model_2020_w2v = word2vec.load("w2vmodel2020")
model_2020_w2v_clean = word2vec.load("w2vmodel2020_clean")

model_2019_ft = fasttext.load("ftmodel2019")
model_2019_ft_clean = fasttext.load("ftmodel2019_clean")
model_2020_ft = fasttext.load("ftmodel2020")
model_2020_ft_clean = fasttext.load("ftmodel2020_clean")

# print("19w2v")
# for i in model_2019_w2v.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2019_w2v.wv.similarity('flu', 'influenza')
print("sim = " + str(sim))
print(model_2019_w2v.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("20w2v")
# for i in model_2020_w2v.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2020_w2v.wv.similarity('COVID', 'coronavirus')
print("sim = " + str(sim))
print(model_2020_w2v.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("19w2vclean")
# for i in model_2019_w2v_clean.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2019_w2v_clean.wv.similarity('flu', 'influenza')
print("sim = " + str(sim))
print(model_2019_w2v_clean.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("20w2vclean")
# for i in model_2020_w2v_clean.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2020_w2v_clean.wv.similarity('COVID', 'coronavirus')
print("sim = " + str(sim))
print(model_2020_w2v_clean.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("19ft")
# for i in model_2019_ft.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2019_ft.wv.similarity('flu', 'influenza')
print("sim = " + str(sim))
print(model_2019_ft.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("20ft")
# for i in model_2020_ft.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2020_ft.wv.similarity('COVID', 'coronavirus')
print("sim = " + str(sim))
print(model_2020_ft.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("19ftclean")
# for i in model_2019_ft_clean.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2019_ft_clean.wv.similarity('flu', 'influenza')
print("sim = " + str(sim))
print(model_2019_ft_clean.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))
# print("20ftclean")
# for i in model_2020_ft_clean.wv.most_similar(u"coronavirus"):
#     print(i[0], i[1])
sim = model_2020_ft_clean.wv.similarity('COVID', 'coronavirus')
print("sim = " + str(sim))
print(model_2020_ft_clean.wv.most_similar(positive=['man', 'boy'], negative=['women'], topn=3))