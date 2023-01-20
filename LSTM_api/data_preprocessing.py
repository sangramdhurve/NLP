import re
import string
import tensorflow as tf
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from keras.preprocessing.text import one_hot

stop_words = set(stopwords.words("english"))


ps = PorterStemmer()


def preprocessAndEncode(text):
    corpus1 = []
    text = re.sub(r"http\S+", "", text)
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)

    text = text.lower()
    text = re.sub(
        f"[{re.escape(string.punctuation)}]", "", text
    )
    text_tokens = word_tokenize(text)
    text_without_stopwords = [ps.stem(word) for word in text_tokens if word not in stop_words]
    text_without_stopwords = ' '.join(text_without_stopwords)
    corpus1.append(text_without_stopwords)
    onehot_test=[one_hot(words, 5000)for words in corpus1]
    embedded_test=tf.keras.preprocessing.sequence.pad_sequences(onehot_test,padding='pre',maxlen=20)
    return embedded_test
    
# a = preprocessAndEncode('#Microsoft Has Identified Evidence of a Destructive Malware Operation ... - Latest Tweet by IANS India - LatestLY https://t.co/YY5sV3uuEK https://t.co/SSVXuqAMb3')
# print(a)
