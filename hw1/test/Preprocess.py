import numpy as np
from scipy import stats

txt_path = '../data/breast-cancer-wisconsin.data'  # txt文本路径
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

print(dataset)

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


# 观察数据推测 其特征的应该属于连续值
# 分类for i in range(2,10)
#       value >= i  分一类
