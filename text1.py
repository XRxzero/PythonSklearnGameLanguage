text = u"我今天很快乐。我今天很愤怒。"
from snownlp import SnowNLP

s = SnowNLP(text)
for sentence in s.sentences:
    print(sentence)
s1 = SnowNLP(s.sentences[0])
print(s1.sentiments)
s2 = SnowNLP(s.sentences[1])
print(s2.sentiments)
