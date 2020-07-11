## problem 1

$$
\begin{aligned}
k(\overrightarrow{x},\overrightarrow{y})
&=\gamma(\overrightarrow{x})\cdot\gamma(\overrightarrow{y})\\
&=(x_1y_1+x_2y_2+\cdots+x_dy_d)^n
\\进行多项式展开：\\
&=\sum\frac{n!}{k_1!k_2!\cdots k_d!}(x_1y_1)^{k_1}(x_2y_2)^{k_2} \cdots (x_dy_d)^{k_d}
\\ \\
&(\sum_{i=1}^d k_i=n)
\end{aligned}
$$

由此得出：
$$
\gamma(\overrightarrow{x})=\sum\sqrt\frac{n!}{k_1!k_2!\cdots k_d!}(x_1)^{k_1}(x_2)^{k_2} \cdots (x_d)^{k_d}\\
(\sum_{i=1}^d k_i=n)
$$
维数取决于多项式的项数，而映射后超平面的VC dimension为项数+1

暂时只想到暴力解法：

每次得到 $\sum_{i=1}^d k_i=n$的一种组合，记有m个不同的重复的数字，对于数字$a_j$，有$h_j$数字与$a_j$相同(包括本身)，则这种组合的项数共有：
$$
\frac{n!}{\prod_{j=1}^m a_j!}
$$
遍历每种组合，并将结果相加得到项数。







## problem 2

​	在问题1的基础上增加了常数项1，与问题1同理，得出$\gamma$：
$$
\gamma(\overrightarrow{x})=\sum\sqrt\frac{n!}{k_1!k_2!\cdots k_d!k_{d+1}!}(x_1)^{k_1}(x_2)^{k_2} \cdots (x_d)^{k_d}\\
(\sum_{i=1}^{d+1} k_i=n)
$$
VC dimension 同problem1

