<h1  align = "center" >数值分析与算法<br>第一次大作业 </h1>

<h6 align = "center">自96 曲世远 2019011455</h6>



## 双线性插值

#### 完成思路

本题给出了一幅通过坐标变换得到的二维码。首先，由于给出的图片为$.png$格式，且包含有$alpha$通道，不便于通过矩阵处理，因此我先通过图像处理软件将其转换为了$.jpg$格式，再将图片读入，依据给定公式进行双线性插值。

#### 数学推导

根据题目中给定的坐标系，遍历直角坐标二维码图中的每个像素，先将像素值转化为坐标值，并映射为极坐标系中的$r, \theta$：
$$
r = x / length \times 2\pi\\
\theta = y / length \times 2\pi\\
$$


再将$r，\theta$转化得到极坐标二维码图中的像素下标：
$$
x_0 = (2\pi + r\cos\theta) \times length / 4\pi\\
y_0 = (2\pi - r\sin\theta) \times length / 4\pi\\
$$
之后找到该下标附近的像素点及像素值根据双线性插值的公式进行计算即可。

#### 误差分析



#### 作图结果



<img src="report.assets/qr_polar.jpg" alt="qr_polar" style="zoom:50%;" /><img src="report.assets/qr_carts.jpg" alt="qr_carts" style="zoom: 50%;" />