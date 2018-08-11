# -*- coding: utf-8 -*-
import sklearn
from sklearn.datasets import load_iris

#导入IRIS数据集
iris = load_iris()

from sklearn.feature_selection import VarianceThreshold
print VarianceThreshold(threshold=3).fit_transform(iris.data)

#特征矩阵
iris.data

#目标向量
print iris.target