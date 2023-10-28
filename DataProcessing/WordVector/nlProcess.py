import pickle
import nltk
import gensim
from vec2graph import visualize

# nltk.download()



file = open("twitter_dataset_2019.pickle", 'rb')
data2019 = pickle.load(file)
print(len(data2019))

sentences_2019 = []
for i in data2019:
    new_sentence = (" ".join(i))
    if "http" not in new_sentence or "https" not in new_sentence:
        sentences_2019.append(new_sentence)
print(data2019[:5])
print(len(sentences_2019))
data2019 = []

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
new_pun = "!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
print(new_pun)


stop_words = stopwords.words('english')

for i in range(len(sentences_2019)):
    if i % 50 == 0:
        print(i / len(sentences_2019))
    tokens = word_tokenize(sentences_2019[i])
    tokens = [w.lower() for w in tokens]
    words = [word for word in tokens if word.isalpha()]
    table = str.maketrans('', '', new_pun)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # words = [w for w in words if not w in stop_words]

    data2019.append(words)

file = open('data_2019_clean.pkl', 'wb')
# dump information to that file
pickle.dump(data2019, file)
# close the file
file.close()

file = open('data_2019_clean.pkl', 'rb')
data2019 = pickle.load(file)
file.close()
#
#
word2vec = gensim.models.Word2Vec
# fasttext = gensim.models.FastText
#
w2vmodel2019 = word2vec(data2019, size=100, window=5, min_count=5, workers=4)
# # w2vmodel2019.save("w2vmodel2019_clean")
w2vmodel2019.wv.save_word2vec_format("2019clean" + '.model.bin', binary=True)  # C binary format 磁盘空间比上一方法减半

model2019 = gensim.models.KeyedVectors.load_word2vec_format('2019clean.model.bin', binary=True)
visualize('temp/graphs/2019', model2019, 'influenza', depth=1, topn=10, edge=1)
#
