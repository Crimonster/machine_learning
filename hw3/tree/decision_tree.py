import numpy as np
from tree.question import Question
from tree.gini import gini, info_gain, class_counts
# import sys
#
# sys.setrecursionlimit(1000000)  # 例如这里设置为一百万

def best_value(rows, col, flag):
    """
    param: fdata 第0行为属性，第1行为类别
    """
    # 选取一列，确定以一个值作为分界分出两部分的gini增益最大，
    # 返回这个分界值，以及gini增益，和划分后的两个数组
    # 遍历取值：2-10，>=取值的分到true
    # 然后分裂成两个
    # 循环，在循环中保存gini增益值最大的分界值和分裂后的数组

    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    if flag == 0:
        le = 30
        ri = 83
    elif flag ==1:
        le = 0
        ri = 4
    else:
        le = 1
        ri = 2

    for val in range(le, ri):
        question = Question(col, val)
        true_rows, false_rows = partition(rows, question)
        if len(true_rows) == 0 or len(false_rows) == 0:
            continue
        gain = info_gain(true_rows, false_rows, current_uncertainty)
        if gain > best_gain:
            best_gain, best_question = gain, question

    return best_gain, best_question


def best_feature(rows, method='CART'):
    # 一次划分的最优特征，比较各个特征
    # 选取最优的特征作为此树的结点，
    # 循环，保存增益值最大的特征，及分裂后的数组
    # 用此特征，
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    n_features = len(rows[0]) - 1  # number of columns

    con = 0  # 用来区分列
    for col in range(n_features):  # for each feature
        temp_gain, temp_question = best_value(rows, col, con)
        con += 1
        if best_gain < temp_gain:
            best_gain = temp_gain
            best_question = temp_question

    return best_gain, best_question


def partition(rows, question):
    """Partitions a dataset.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


def classify(row, node):
        """See the 'rules of recursion' above."""

        # Base case: we've reached a leaf
        if isinstance(node, Leaf):
            return node.prediction

        # Decide whether to follow the true-branch or the false-branch.
        # Compare the feature / value stored in the node,
        # to the example we're considering.
        if node.question.match(row):
            return classify(row, node.true_branch)
        else:
            return classify(row, node.false_branch)


def test_true_rate(model, test_data, class_column):
        total = len(test_data)
        true_count = 0

        for test in test_data:
            # 检查点（使用==号是否能判断出来）
            if classify(test, model) == test[class_column]:
                true_count += 1
        return float(true_count/total)


def prediction_testData(model, test_data):
        results = []
        for test in test_data:
            results.append(classify(test,model))
        return results


class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.prediction = self.result(rows)

    def result(self, rows):
        partitions = class_counts(rows)
        max = 0
        ans = 0
        for k in partitions:
            if max < partitions[k]:
                max = partitions[k]
                ans = k
        return ans


class DecisionNode:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch,):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch



class DecisionTree:
    def __init__(self, training_data):
        """
            预剪枝
            属性值：最大枝杈数目，
        """
        # self.__wait_list = [] 不用这个，使用递归
        self.rows = training_data
        self.mytree = None
        # 学习一下剪枝的方法

    def set_training_data(self, training_data):
        self.rows = training_data

    # 是否训练完成
    def state(self):
        if self.rows is None and self.mytree is not None:
            return True
        else:
            return False

    def build_tree(self, rows=None):
        # 判断使用给定数据，还是初始数据
        if rows is not None:
            pass
        elif rows is None and self.rows is not None:
            rows = self.rows
        else:
            print("Lack of training data")
            return False

        gain, question = best_feature(rows)

        # Base case: no further info gain
        # Since we can ask no further questions,
        # we'll return a leaf.

        if gain == 0:
            return Leaf(rows)

        # If we reach here, we have found a useful feature / value
        # to partition on.
        true_rows, false_rows = partition(rows, question)

        # Recursively build the true branch.
        true_branch = self.build_tree(true_rows)

        # Recursively build the false branch.
        false_branch = self.build_tree(false_rows)

        # Return a Question node.
        # This records the best feature / value to ask at this point,
        # as well as the branches to follow
        # depending on the answer.
        return DecisionNode(question, true_branch, false_branch)

    def five_fold_cross_validation(self):
        data = {}
        total_num = len(self.rows)
        num = int(total_num/5)

        count = 0
        # 切分
        for i in range(1, 6):
            fold = []
            for j in range(0, num):
                fold.append(self.rows[count])
                count += 1
                if count == total_num:
                    break
            data[i] = fold

        true_rate_aver = float(0)
        for i in range(1, 6):
            train_data = None
            test_data = []
            # 检查点
            # 划分训练集和测试集
            for k in data:
                v = data[k]
                if k == i:
                    test_data = v
                    continue
                if train_data is None:
                    train_data = v
                    continue
                train_data = np.vstack((train_data, v))
            model = self.build_tree(train_data)
            # 去掉id列后 下标为3的列为类标号
            true_rate_aver += test_true_rate(model, test_data, 3)

        true_rate_aver /= 5
        return true_rate_aver

    def prediction(self, test_data):
        model = self.build_tree(self.rows)
        return prediction_testData(model, test_data)
