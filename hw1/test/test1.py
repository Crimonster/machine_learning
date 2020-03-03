# from scipy import stats
# data = [0,1,1,3]
# data[0]=1
# print(stats.mode(data)[0][0])

import numpy as np

data = []
# data.append([3,4,5])
# data.append([1,2,'?'])
# print(data)
# data = np.array(data)
# data[0,0] = 2
# print(data)

# list = [1,2,3,4,5]
# list.pop(0)
# print(list)

# for i in range(2,11):
#     print(i)

# i = 699/5
# print(i)

data.append([3,4,5])
data.append([1,2,'?'])
data = np.array(data)
t = [[1,2,3]]
ans = np.vstack((t, data))
print(ans[0:3,:])