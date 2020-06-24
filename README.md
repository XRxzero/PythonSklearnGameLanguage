# PythonSklearnGameLanguage
单人实现，做的匆忙，文件都没有好好命名
test是用来生成模型文件的，读入train_data后通过jieba实现中文分词，并借用哈工大停词表删除停用词（实际上后来为了提高f1score没有加这个参数，铁分奴）
一开始使用的分类模型是MultinomialNB()（主要是图他跑得快）后来代码基本定型后使用SVC()（慢归慢但人家出分高啊）
test1是用来尝试snownlp的，但看起来对游戏的消极语言判定针对性不足，只好作罢
test2主要负责使用test生成的模型加上验证数据集跑个准确率 精确度 召回矩阵 f1score 什么的（实际上部分功能已经在test中实现了，但因为test跑一次时间挺长的，所以才单独分出来）
test3是洗数据用的，因为拿到手的数据真的过脏，只好按着自己的理解给标上label
test4用处不大，只是用来查看数据里label=1的数据数量的
main_test是用来最终运行的，用以获得通过模型标记好label的数据，用于后续验证
数据集不能外传，只能写一下格式：
train_data.txt和validation_data_demo.txt的格式是类似的，都是：
qid	text	label
1	我去送了个人头，结果啥也没那到。 	1
1	把我送死了是吧 	1
1	我都送了你们就下不信我杀了九个人。 	1
……
