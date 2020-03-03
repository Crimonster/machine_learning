import numpy as np
from scipy import stats
from decision_tree import DecisionTree
# import sys
#
# sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
# 预处理

# 生成np数组
txt_path = 'breast-cancer-wisconsin.data'  # txt文本路径
with open(txt_path) as f:
    data_lists = f.readlines()  # 读出的是str类型

dataset = []
# 对每一行作循环
for data in data_lists:
    data1 = data.strip('\n')  # 去掉开头和结尾的换行符
    data2 = data1.split(',')  # 把,作为间隔符
    data1 = []
    for x in data2:
        if len(x) > 2:
            pass
        elif x == '?':
            data1.append(0)
        else:
            data1.append(int(x))
    dataset.append(data1)  # 把这一行的结果作为元素加入列表dataset
dataset = np.array(dataset)
# print(dataset)

# 处理缺失值
miss_feature = {}
# 记录缺失值的位置
for i in range(len(dataset)):
    for j in range(10):
        if dataset[i][j] == 0:
            if j not in miss_feature:
                miss_feature[j] = []
            miss_feature[j].append(i)

# 使用同类中样本的众数进行插值
for k in miss_feature:
    temp = stats.mode(dataset[:, k])[0][0]
    vl = miss_feature[k]
    for v in vl:
        i = v
        j = k
        dataset[i, j] = temp

# 仿照网上重写question来建树
# dataset是数据集，有699个样本，
# 10个特征值，对应的下标是1-10，（其中0号下标对应的为id，是无用的属性）
# 取值范围：1-9是分类依据，10是分类结果：(2 for benign, 4 for malignant)

"""
大致流程：
 一，训练：
    1,每次分叉，选择gini变化量最大的特征作为结点
    2,剪枝
 二，验证：
    1，将test数据传入决策树中，经过一系列划分，得到结果
    2，对比预测结果与真实结果，统计正确率
"""
# 需要进行5-fold-cross-variation

decision_tree = DecisionTree(dataset)
print(decision_tree.five_fold_cross_validation())