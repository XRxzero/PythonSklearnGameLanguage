import pandas as pd
import jieba


def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


df = pd.read_table("./train_data(re).txt")
va = pd.read_table("./validation_data_demo(re).txt")
# print(df)

X = df[['text']]
y = df.label


#print(y)
X['cutted_text'] = X.text.apply(chinese_word_cut)

X_test = va[['text']]
y_test = va.label

X_test['cutted_text'] = X_test.text.apply(chinese_word_cut)


# print(X.cutted_text[:5])

# 下面把训练集分成了两份#
# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# print(X_train.shape)

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list


stop_words_file = "stopwordsHIT.txt"
stopwords = get_custom_stopwords(stop_words_file)
# print(stopwords[-10:])

from sklearn.feature_extraction.text import CountVectorizer

# vect = CountVectorizer()
# term_matrix = pd.DataFrame(vect.fit_transform(X_train.cutted_text).toarray(), columns=vect.get_feature_names())

# vect = CountVectorizer(stop_words=frozenset(stopwords))


max_df = 0.9  # 在超过这一比例的文档中出现的关键词（过于平凡），去除掉。
min_df = 40  # 在低于这一数量的文档中出现的关键词（过于独特），去除掉。

vect = CountVectorizer(#max_df=max_df,
                       #min_df=min_df,
                       #token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                       #stop_words=frozenset(stopwords)
                       )

#vect = CountVectorizer(max_df=max_df,
#                       min_df=min_df,
#                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b')
# term_matrix = pd.DataFrame(vect.fit_transform(X_train.cutted_text).toarray(), columns=vect.get_feature_names())
#term_matrix = pd.DataFrame(vect.fit_transform(X.cutted_text).toarray(), columns=vect.get_feature_names())
# print(term_matrix.head())

#from sklearn.naive_bayes import MultinomialNB

#nb = MultinomialNB()

from sklearn.svm import SVC

nb = SVC()

from sklearn.pipeline import make_pipeline

pipe = make_pipeline(vect, nb)

# print(pipe.steps)

pipe.fit(X.cutted_text, y)

#from sklearn.model_selection import cross_val_score

#print(cross_val_score(pipe, X.cutted_text, y, cv=20, scoring='accuracy').mean())

y_pred = pipe.predict(X_test.cutted_text)

import joblib

joblib.dump(pipe, "./model.joblib")

import pickle
pickle.dump(pipe, open("./model.pickle", 'wb'))

from sklearn import metrics

print(metrics.accuracy_score(y_test, y_pred))
from sklearn.metrics import f1_score

print(f1_score(y_test, y_pred))
