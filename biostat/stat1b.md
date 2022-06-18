# 生物統計演習第1回後半
## 記述統計
### subsectionプロット図
まず**プロット図**を用いてデータを俯瞰しよう。
#### ヒストグラム (histogram)
前節の演習問題にて作成したスカラー変数SL_setosa、SL_versicolor、SL_virginicaについて、ヒストグラムを作成してみよう。
Rではhist()関数にてヒストグラムを容易に作成できる。データの区間を**階級(class)** といい、breaksオプションに区間をベクトルで与えて指定する。
今回は、階級は4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0で作成する。

```
 kaikyu = c(4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0)  # 階級をベクトルとして保存。
# 得られた結果をSL_setisa_histに代入、X軸は"Sepal length"とする。
SL_setosa_hist = hist(SL_setosa, breaks = kaikyu, xlab="Sepal length") 
#SL_setosa_histの内容を確認
SL_setosa_hist
# 下記のような結果が出てくる 
$`breaks`
[1] 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0
$counts
[1]  5 23 19  3  0  0  0  0
$density
[1] 0.20 0.92 0.76 0.12 0.00 0.00 0.00 0.00
$mids
[1] 4.25 4.75 5.25 5.75 6.25 6.75 7.25 7.75
$xname
[1] "SL_setosa"
$equidist
[1] TRUE
attr(,"class") 
[1] "histogram"

#いろいろ出てきて分かりにくいが、countsにそれぞれの階級の
#度数が出てくるので、適宜活用する
```
```
# 結果をplot
plot(SL_setosa_hist)
```
<img src="./KgD4T7tf.png"  width="1200">
```
#以下同様に、、、、、、
 # 得られた結果をSL_versicolor_histに代入
SL_versicolor_hist = hist(SL_versicolor, breaks = kaikyu) 
plot(SL_versicolor_hist)
# 得られた結果をSL_virginica_histに代入
SL_virginica_hist = hist(SL_virginica, breaks = kaikyu)  
plot(SL_virginica_hist)  
```
ヒストグラムを見ると、大まかにsetosa, versicolor, virginicaの順でがくが大きいとわかる。

#### 散布図
散布図(scatter plotあるいはdot plot)では、x-y平面上にデータをプロットし、二者間のデータの関連を図示することができるstripchart()関数にて容易に得ることができる。
<img src="./4iZ53u0j.png">
```
stripchart(data=iris, Sepal.Length~Species,method="jitter",vert=T,pch=1)
```
dataオプションでデータフレームを指定する。$\bm{y} \sim \bm{x}$のように二つの列ベクトルを記述する\footnote{$\bm{y} \sim \bm{x}$は、$\bm{y}$は$\bm{x}$に従う、と読む。$\bm{x} \sim \bm{y}$と入力してうまくいかなかった学生がいたので、注意すること}。$\bm{y}$は
目的変数といい、着目するデータを含む列を指定する。$\boldsymbol{x}$は説明変数といい、目的変数を説明する変数である。
しばしば原因として目的変数との関連を調べたいデータの列を指定する。上記の例では$\boldsymbol{x}$に種名の列、$\boldsymbol{y}$に
花弁長の列を指定し、種と花弁長の関連をしめす散布図を得ている。
関数ごとに、データの入力形式が異なるので、各関数の使い方を習熟しておく必要がある。
使い方のわからない関数が出てきた場合、関数の名前にクエスチョンマークをつけて実行すると、ヘルプが立ち上がり、
説明書を読むことができる。

```
# 実行してみよう
?stripchart
```
<img src="./HIAulcAs.png">

