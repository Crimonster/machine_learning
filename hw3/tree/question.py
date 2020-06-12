class Question:
    """A Question is used to partition a dataset.
        保存了特征和取值的信息
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        # print(val)
        return val >= self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = ">="
        return "Is %s %s %s?" % (
            self.column, condition, str(self.value))