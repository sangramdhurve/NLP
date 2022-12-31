import re
import string
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec


from typing import List
stop_words = set(stopwords.words("english"))

#print(w2v_model)
def preprocess_text(text: str) -> List[str]:
    # Remove links
    text = re.sub(r"http\S+", "", text)
    
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)
    
    text = text.lower()
    text = re.sub(
        f"[{re.escape(string.punctuation)}]", "", text
    )
    text_tokens = word_tokenize(text)
    text_without_stopwords = [word for word in text_tokens if word not in stop_words]
    print(text_without_stopwords)
    w2v_model = Word2Vec(sentences=text_without_stopwords, vector_size=300)
    print(w2v_model)
    vector_size = w2v_model.vector_size
    #print(vector_size)
    wv_res = np.zeros(300)
    # print(wv_res)
    ctr = 1
    for w in text:
        #print(w)
        if w in w2v_model.wv:
            ctr += 1
            wv_res += w2v_model.wv[w]
    wv_norm = wv_res/ctr
    return wv_norm

# input_text = "Disadvantages Intelligence Technology."
# a = preprocess_text(input_text)
# print(a)