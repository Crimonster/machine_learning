def class_counts(rows):
    results = {}
    for row in rows:
        # The result is the last column
        # 最后一列代表其类别
        r = row[9]
        if r not in results:
            results[r] = 0
        results[r] += 1
        return results


def gini(rows):
    total = len(rows)
    counts = class_counts(rows)
    imp = 0
    for k1 in counts:
        p1 = float(counts[k1]) / total
        imp += p1*p1
    return 1-imp


def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)
