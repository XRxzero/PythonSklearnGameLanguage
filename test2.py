import pandas as pd
import jieba


def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


# import joblib
# model = joblib.load("./model.joblib")
import pickle

model = pickle.load(open("./model.pickle", 'rb'))

va = pd.read_table("./validation_data_demo(re).txt")

X_test = va[['text']]
y_test = va.label

X_test['cutted_text'] = X_test.text.apply(chinese_word_cut)

from sklearn.model_selection import cross_val_score

# print(cross_val_score(pipe, X.cutted_text, y, cv=20, scoring='accuracy').mean())

y_pred = model.predict(X_test.cutted_text)

from sklearn import metrics

print(metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import precision_score

print(precision_score(y_test, y_pred))

from sklearn.metrics import recall_score

print(recall_score(y_test, y_pred))

from sklearn.metrics import f1_score

# print(f1_score(y_test, y_pred, average='macro'))
# print(f1_score(y_test, y_pred, average='micro'))
# print(f1_score(y_test, y_pred, average='weighted'))
# print(f1_score(y_test, y_pred, average=None))
# print(y_pred)
# print(y_test)
print(y_pred)
print(f1_score(y_test, y_pred))
print(metrics.confusion_matrix(y_test, y_pred))
