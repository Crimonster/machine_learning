**定义**  假设空间 H 的 VC-dimension 是能被 H 打散的最大数据集的大小

 *VC*(*H*) = *d* 表明存在大小为 *d* 的数据集能被假设空间 H 打散。

 通常这样来计算 H 的 VC-dimension：若存在大小为 d 的数据集能被 H 打散，但不存在任何大小为 d+1 的数据集能被 H 打散，则 H 的 VC-dimension 是 d。





## 问题1：

对于
$$
\sigma(x)=x
$$
计算时，只需要求出数据集大小即可：

VC(o)=d\*(d\*n+n) + n

应该可以使用归纳法证明：不存在任何大小为 d+1 的数据集能被 H 打散



## 问题2：

使用一篇论文的证明结果

(Nearly-tight VC-dimension and Pseudo dimension Bounds for Piecewise Linear Neural Networks
Peter L. Bartlett, Nick Harvey, Christopher Liaw, Abbas Mehrabian; 20(63):1−17, 2019.)

使用RELU激活函数的神经网络，VC维上界：**O(WLlog(W))**

​																	下界： **Ω(WLlog(W/L))**

o = W<sub>2</sub>*σ(W<sub>1</sub>\*v + b<sub>1</sub>) + b<sub>2</sub> 

weights：W=n 
$$
\sigma(x)=RELU(x)
$$


则VC(o)=O(2d(nlogn)+n),      Ω(2d(nlog(n/2))+n)



参考资料：https://github.com/Hirotransfer/Big-Data-Algorithms-2020-Spring-