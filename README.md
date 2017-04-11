# SPSA-algorithm
随机扰动近似算法，Python实现

## 介绍
* 随机扰动近似算法SPSA，英文Simultaneous Perturbation Stochastic Approximation首字母的缩写。
* SPSA算法是Spall于1987年根据Kiefer-Wolforwitz随机逼近算法改进而成。它通过估计目标函数的梯度信息来逐渐逼近最优解。在每次梯度逼近中只利用了两个目标函数估计值，与优化问题的维数无关，从而大大减少了用于估计梯度信息的目标函数的测量次数，因此SPSA算法常用于解决高维问题以及大规模随机系统的优化。

## 开发记录
### 2017/3/21
* 完成算法主要程序编写
### 2017/4/11
* 初步加入traitUI，输入参数设置界面
