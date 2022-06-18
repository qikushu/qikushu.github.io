# 生物統計演習第1b回
## 記述統計
### subsectionプロット図
まず**プロット図**を用いてデータを俯瞰しよう。
#### ヒストグラム (histogram)
前節の演習問題にて作成したスカラー変数SL_setosa、SL_versicolor、SL_virginicaについて、ヒストグラムを作成してみよう。
Rではhist()関数にてヒストグラムを容易に作成できる。データの区間を**階級(class)** といい、breaksオプションに区間をベクトルで与えて指定する。
今回は、階級は4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0で作成する。
(図\ref{fig:75YdRt6x})。

\fbox{\includegraphics[clip,width=16.0cm]{./KgD4T7tf.png}}
 \caption{花弁の長さのヒストグラム. (a) setosa, (b) versicolor, (c)virginica}


\begin{breakbox}
\begin{verbatim}
 kaikyu = c(4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0)  # 階級をベクトルとして保存。
# 得られた結果をSL_setisa_histに代入、X軸は"Sepal length"とする。
SL_setosa_hist = hist(SL_setosa, breaks = kaikyu, xlab="Sepal length") 
#SL_setosa_histの内容を確認
SL_setosa_hist
# 下記のような結果が出てくる 
$`breaks`    # 結果
[1] 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0  # 結果
$counts  # 結果
[1]  5 23 19  3  0  0  0  0  # 結果
$density  # 結果
[1] 0.20 0.92 0.76 0.12 0.00 0.00 0.00 0.00  # 結果
$mids  # 結果
[1] 4.25 4.75 5.25 5.75 6.25 6.75 7.25 7.75  # 結果
$xname  # 結果
[1] "SL_setosa"  # 結果
$equidist  # 結果
[1] TRUE  # 結果
attr(,"class")  # 結果
[1] "histogra  # 結果m"

#いろいろ出てきて分かりにくいが、countsにそれぞれの階級の
#度数が出てくるので、適宜活用する
# 結果をplot
plot(SL_setosa_hist)

#以下同様に、、、、、、
 # 得られた結果をSL_versicolor_histに代入
SL_versicolor_hist = hist(SL_versicolor, breaks = kaikyu) 
plot(SL_versicolor_hist)
# 得られた結果をSL_virginica_histに代入
SL_virginica_hist = hist(SL_virginica, breaks = kaikyu)  
plot(SL_virginica_hist)  
\end{verbatim}
\end{breakbox}
ヒストグラムを見ると、大まかにsetosa, versicolor, virginicaの順で大きくなっていく様子がわかる。
