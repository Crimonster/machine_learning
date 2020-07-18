# DeepInf: Social Influence Prediction with Deep Learning

## 1 论文解读

### 1.1 关键字

Representation Learning;  表示学习

Network Embedding;          网络嵌入

Graph Convolution;            图卷积

Graph Attention;                 图注意力

Social Influence;                  社会影响

Social Networks;                  社交网络

### 1.2 功能概述

To date,there is little doubt that social influence has become a prevalent,yet complex force that drives our social decisions, making a clear need for methodologies to characterize, understand, and quantify the underlying mechanisms and dynamics of social influence.

 着重对用户层面的社会影响进行预测。 我们的目标是预测用户的行动状态，考虑到她的近邻的行动状态和她当地的结构信息

Inspired by the recent success of neural networks in representation learning, we design an end-to-end approach to discover hidden and predictive signals in social influence automatically. By architecting network embedding [37], graph convolution [25], and graph attention mechanism [49] into a unified framework, we expect that the end-to-end model can achieve better performance than conventional methods with feature engineering. In specific, we proposea deep learning based framework, DeepInf, to represent both influence dynamics and network structures into a latent space. To predict the action status of a user *v*, we first sample her local neighbors through random walks with restart. After obtaining a local network as shown in Figure 1, we leverage both graph convolution and attention techniques to learn latent predictive signals.

### 1.3 问题及定义

#### 定义1：*r***-neighbors and** *r***-ego network**

*G* = (*V*, *E*)                 -社会网络

V                               -用户集

*E* ⊆ *V* × *V*                 -社会关系集

 对于一个用户 *v*，它的 *r**-neighbors** 定义如下

$\Gamma_v^r$= {*u* : *d*(*u*,*v*) ≤ *r* }         -*d(u,v)* 是网络G中u与v之间的最短路径距离(以跃点数计)

对于用户*v* ,  *r***-ego network**   以 $\Gamma_v^r$ 作为子网产生

用$G_v^r$表示

#### 定义2：**Social Action**

用户活动：

时间戳 *t*  ，用户*u*

活动$ s_u^t \in$ {0,1}​，0表示活动未进行，1表示进行

#### 假设：

用户活动只受近邻元素影响

#### 问题1：**Social Influence Locality**



### 1.4 网络流程

However, for different users, $G_v^r$’s may have different sizes. Meanwhile, the size (regarding the number of vertices) of $G_v^r$’s can be very large due to the small-world property in social networks [50].

Such variously sized data is unsuited to most deep learning models. To remedy these issues, we sample a fixed-size sub-network from *v*’s *r*-ego network, instead of directly dealing with the *r*-ego network.

**这种大小不一的数据不适合大多数深度学习模型。为了解决这些问题，我们从v的r-ego网络中抽取一个固定大小的子网络，而不是直接处理r-ego网络。**

抽样方法使用 随机游走：

人们更容易受到活跃邻居的影响，而不是不活跃邻居。受此启发，我们从自我用户v或她的活跃邻居中随机开始随机行走。接下来，随机游走迭代地移动到它的域，其概率与每条边的权值成比例。此外，在每一步中，散步被分配一个返回开始节点的概率，即自我用户v或v的一个活跃邻居。

RWR运行直到成功收集到固定数量的顶点

