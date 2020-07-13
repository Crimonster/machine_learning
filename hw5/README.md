## problem 1 ：

$$
\gamma(\overrightarrow{x})\cdot\gamma(\overrightarrow{y})
=\sum x_{i_1}y_{i_1}x_{i_2}y_{i_2}...x_{i_n}y_{i_n}
\\ 1 \leq i_1,...,in \leq d
$$

合并同类项得到：
$$
\gamma(\overrightarrow{x})\cdot\gamma(\overrightarrow{y})
=\sum a_{i_1,i_2,...,i_n} x_{i_1}y_{i_1}x_{i_2}y_{i_2}...x_{i_n}y_{i_n}
\\ 1 \leq i_1 \leq i_2 ... \leq i_n \leq d
\\ a_{i_1,i_2,...,i_n} = \frac{d!}{r_1!r_2!...r_p!}
$$
其中p是$i_1...i_n$中不同数字的个数，$r_1...r_p$是每个不同数字重复的次数。、

得到：
$$
\gamma(\overrightarrow{x})
=(\sqrt {a_{1,1,...,1}} x_1^n,\sqrt {a_{1,1,...,1}} x_1^{n-1}x_2,...,\sqrt {a_{d,d,...,d}} x_d^n)^T
$$
使用插板法得到其维数是：$C_{n+d-1}^{d-1}$

则，VC dimension 是：$C_{n+d-1}^{d-1}+1$



## problem 2

​	在问题1的基础上增加了常数项1，与问题1同理，得出$\gamma$：
$$
\gamma(\overrightarrow{x})
=(\sqrt {a_{1,1,...,1}} x_1^n,\sqrt {a_{1,1,...,2}} x_1^{n-1}x_2,...,\sqrt {a_{d+1,d+1,...,d+1}} 1^n)^T
$$
VC dimension :

因为最后一项作为偏差，所以结果为：$C_{n+d}^d$





## problem 3

$$
\gamma(\overrightarrow{x})\cdot\gamma(\overrightarrow{y})
=e^{-\sigma(||\overrightarrow{x}||^2+||\overrightarrow{y}||^2)}
$$

可以得到：
$$
\gamma(\overrightarrow{x})=(e^{-\sigma||x||^2})
$$
他的维度是1

则VC dimension 是 2