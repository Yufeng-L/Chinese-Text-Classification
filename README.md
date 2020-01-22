# 中文文本分类 Chinese-Text-Classification 

对有 __特征性__ 的中文数据进行分类。<br/>
__Example:__

1.地址数据的特征 (省，市，区，路...) <br/>
2.公司名的特征（有限，集团，公司...) <br/>

此分类方法对训练数据的规范性和准确性有要求，训练的准确度和训练数据的 __数量__ 和 __质量__ 成正比。简单地说，类别的特征性要明显。

## 1.需要安装的包

#### jieba 
用于中文文本数据的预处理：分词
```python
pip install jieba
```
#### scikit-learn <br/>
scikit-learn是一个开源基于python的机器学习工具
```python
pip install -U scikit-learn
 ```

## 2.对训练集预先分类
针对数据的中文属性做文本分类训练，对中文数据输入能预测出类别。 <br/>
开始之前，我们预先把想要预测的大类分好，如下:

|Category Index 类别 | Category Name 类名 |
|-------------------|:------------------:|
|C1                 |company             |
|C2                 |address             |
|C3                 |material            |

-----

## 3.实现原理
对训练集和测试集的数据进行分词处理后，要把他们变成数据。我们采用了scikit-learn库中的Bunch数据结构来表示这两个数据集。<br/>
对于Bunch的通俗讲解，类似于python中的字典，也是key对应value的类型，比如dict[key]就是字典中key的值. 
### 创建Bunch对象：
----
我们在Bunch对象里面创建了有4个成员： <br/>
- target_name：是一个list，存放的是整个数据集的类别集合。（就是C1,C2,C3）<br/>
- label：是一个list，存放的是所有文本的标签。<br/>
- filenames：是一个list，存放的是所有文本文件的名字。<br/>
- contents：是一个list，分词后文本文件（一个文本文件只有一行）<br/>

绑定了Bunch的数据类型后，实现了数据集的变量表示。<br/>
下一步我们需要创建词向量，词向量简单来说就是将单词映射到向量空间，用向量表示。<br/>
我们要把我们要训练的词都统一放到一个向量空间里面。<br/>
为了节省空间，需要对文本进行一些垃圾词的处理，就是所谓的停用词。他们是一些含义模糊的词或者是一些语气助词标点符号等等。通常他们对文本起不了分类特征的意义。
### 权重策略（TF-IDF）：
----
TF-IDF（Term Frequency-InversDocument Frequency）是一种常用于信息处理和数据挖掘的加权技术。该技术采用一种统计方法，根据字词的在文本中出现的次数和在整个语料中出现的文档频率来计算一个字词在整个语料中的重要程度。它的优点是能过滤掉一些常见的却无关紧要本的词语，同时保留影响整个文本的重要字词。<br/>
我们现在有词向量空间了，在此称为A空间。我们还有测试集的数据，以后实际运用的时候也会有新的数据，这些数据也会转移到我们的A空间。
即使测试集出现了新的词汇或新的文本数据有新词汇，只要它不是训练生成的TF-IDF词向量空间中的词，我们都不予考虑。<br/>
再简单点来理解就是我们把训练集数据成功构建了TF-IDF词向量空间，空间的每个词都是出自我们的训练集，各个值的权值都一并保存了下来，这就是权重矩阵。权重矩阵是一个二维矩阵，可以用a[i][j]去表示。
### TF-IDF计算：
----
Scikit-Learn中TF-IDF权重计算方法主要用到两个类：CountVectorizer和TfidfTransformer。
CountVectorizer类会将文本中的词语转换为词频矩阵，例如矩阵中包含一个元素a[i][j]，它表示j词在i类文本下的词频。它通过fit_transform函数计算各个词语出现的次数，通过get_feature_names()可获取词袋中所有文本的关键字，通过toarray()可看到词频矩阵的结果。
接下来我们会将训练集数据转换为TF-IDF词向量空间中的实例，保存在tfdifspace.dat中，具体来说，这个文件里面有两个我们感兴趣的东西，一个是vocabulary，即词向量空间坐标，一个是tdm，即训练集的TF-IDF权重矩阵。

### 分类器：
----
做这些工作之前，我们首先要把测试数据也映射到上面这个TF-IDF词向量空间中，也就是说，测试集和训练集处在同一个词向量空间，只不过测试集有自己的权重tdm，与训练集（train_word_bag/tfdifspace.dat）中的tdm不同而已。<br/>
由于我们使用词的出现次数作为特征，可以用多项分布来描述这一特征。在sklearn中使用sklearn.naive_bayes模块的MultinomialNB类来构建分类器。

## 4.分类样例输出
该分类运行在windows系统，下图是文本分类的样例输出：<br/>
![sampleout](https://github.com/Yufeng-L/Chinese-Text-Classification/blob/master/result/sampleout.png)

## 5.txt文件编码事项
txt文本理论应使用 __UTF-8__ 编码，windows下本人为训练集和测试集均为在ASCII编码下运行无误，但是在linux下数据集显示乱码，关于对编码的详细信息后续会探索并更新。









