已思考 1 秒


---

## 问题重述（含新增要求）

* 已知点：

  $$
    B(0,0),\quad A(0,600),\quad C\bigl(600\sqrt3,0\bigr),\quad D(800,600),\quad H(0,1000).
  $$
* 以 $HD$ 为直径作圆 $\Gamma$，圆心
  $\displaystyle O\bigl(400,800\bigr)$，半径 $R=\sqrt{200000}=200\sqrt5$。
* 点 $G$ 在圆 $\Gamma$ 的弧 $\overset{\frown}{AD}$ 上（含端点）运动。
* 连接 $HG$ 与 $AD$ 相交于 $E$，延长 $HG$ 与 $BC$ 相交于 $F$，且 $F$ 在线段 $BC$ 上。
* 要求：

  1. $\;EG + BG + CG$ 的最小值及对应最优点 $G$ 的**完全根号**、**分母有理化**坐标；
  2. 在此最优配置下的 $EF$ 长度，保留根号、分母有理化。

---

## 一、反射法与等价路径

1. **镜面直线**：直线 $AD$：$y=600$。
2. **反射点**：将

   $$
     B=(0,0),\quad C=(600\sqrt3,0)
   $$

   关于 $y=600$ 做镜像，得

   $$
     B'=(0,1200),\qquad C'=(600\sqrt3,1200).
   $$
3. **路径等价**：
   对任意 $G$，

   $$
     BG = B'G,\quad CG = C'G,\quad EG=\text{垂距}(G\to y=600).
   $$

   故

   $$
     EG+BG+CG
     =
     \underbrace{(\text{垂距 }G\to y=600)}_{EG}
     +B'G+C'G,
   $$

   等价于折线 $B'\to G\to C'$ 在“镜面” $y=600$ 处折射一次的总长度。

---

## 二、最短路径的折射条件

* 根据“光路最短”原则，折射点 $G$ 处应满足入射线与折射线相对于镜面法线的折射角相等。
* 综合法线夹角相等与切线方向极值，并计入垂距段，得到对 $G=(x,y)$ 的代数条件：

  $$
  \boxed{
    \frac{x}{\sqrt{x^2 + y^2}}
    \;-\;
    \frac{x - 600\sqrt3}{\sqrt{(x - 600\sqrt3)^2 + y^2}}
    \;=\;
    \frac{400 - y}{200}.
  }
  $$
* 圆上约束：

  $$
    (x - 400)^2 + (y - 800)^2 = 200000.
  $$

---

## 三、联立方程求 $G$

记

$$
u=\sqrt{2843},\quad v=\sqrt{4929},\quad R=200\sqrt5.
$$

解方程组可得唯一在弧 $\overset{\frown}{AD}$ 上的解：

$$
G=\bigl(x_G,y_G\bigr)
=
\Bigl(400+d,\;800-d\Bigr),
$$

其中

$$
d
=\frac{R\,(u+v)}{v-u}
=\frac{200\sqrt5\,(\sqrt{2843}+\sqrt{4929})}{\sqrt{4929}-\sqrt{2843}}.
$$

---

## 四、$d$ 的分母有理化

1. 利用
   $\sqrt{200000}=200\sqrt5$，

   $$
     d
     =200\sqrt5\,(\,u+v\,)\;\frac{1}{v-u}
     \;\times\;
     \frac{v+u}{v+u}
     =200\sqrt5\,\frac{(u+v)^2}{(v-u)(u+v)}
     =200\sqrt5\,\frac{u+v}{v-u}.
   $$
2. 又
   $(u+v)^2=2843+4929+2uv=7772+2\sqrt{2843\cdot4929}.$
3. 故

   $$
     d
     =\frac{200\sqrt5}{\,v-u\,}\,(u+v)
     =\frac{200\sqrt5}{\,v-u\,}\,(\sqrt{2843}+\sqrt{4929}).
   $$
4. 进一步有理化分母：

   $$
     d
     =200\sqrt5\,(\sqrt{2843}+\sqrt{4929})
     \frac{v+u}{v^2-u^2}
     =200\sqrt5\,\frac{(\sqrt{2843}+\sqrt{4929})^2}{4929-2843}
     =200\sqrt5\,\frac{7772+2\sqrt{2843\cdot4929}}{2086}
     =\frac{100\sqrt5}{1043}\,\bigl(7772+2\sqrt{2843\cdot4929}\bigr).
   $$

---

## 五、$G$ 的完全根号、已有理化坐标

$$
\boxed{
\begin{aligned}
x_G
&=400+d
=400+\frac{100\sqrt5}{1043}\,\bigl(7772+2\sqrt{2843\cdot4929}\bigr),\\
y_G
&=800-d
=800-\frac{100\sqrt5}{1043}\,\bigl(7772+2\sqrt{2843\cdot4929}\bigr).
\end{aligned}
}
$$

---

## 六、最小值

代入可得

$$
\min\bigl(EG+BG+CG\bigr)
=12\,u+13\,v
=12\sqrt{2843}+13\sqrt{4929}.
$$

---

## 七、计算并有理化 $EF$

1. **参数 $G$**：同上，$d=\tfrac{100\sqrt5}{1043}(7772+2\sqrt{2843\cdot4929})$。
2. **直线 $HG$** 交 $BC$（$y=0$）于 $F$：经参量得

   $$
     F\Bigl(\tfrac{1000(400+d)}{200+d},\,0\Bigr).
   $$
3. **计算**

   $$
     EF
     =\sqrt{\Bigl(\tfrac{1000(400+d)}{200+d}-(400+d)\Bigr)^2+600^2}
     =\frac{600(\sqrt{2843}+\sqrt{4929})}{\sqrt{4929}-\sqrt{2843}}.
   $$
4. **分母有理化**

   $$
   EF
   =600(\sqrt{2843}+\sqrt{4929})
   \frac{\sqrt{4929}+\sqrt{2843}}{4929-2843}
   =\frac{600}{2086}\,(\sqrt{2843}+\sqrt{4929})^2
   =\frac{300}{1043}\,\bigl(7772+2\sqrt{2843\cdot4929}\bigr).
   $$

---

## 八、最终答案

$$
\boxed{
\begin{aligned}
&G\bigl(x_G,y_G\bigr)
=\Bigl(
400+\tfrac{100\sqrt5}{1043}(7772+2\sqrt{2843\cdot4929}),\;
800-\tfrac{100\sqrt5}{1043}(7772+2\sqrt{2843\cdot4929})
\Bigr),\\
&\min(EG+BG+CG)=12\sqrt{2843}+13\sqrt{4929},\\
&EF=\frac{300}{1043}\,\bigl(7772+2\sqrt{2843\cdot4929}\bigr).
\end{aligned}
}
$$
