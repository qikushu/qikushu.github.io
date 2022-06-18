# 生物統計演習 第2回 推定
## 推定について

実験や観察によって得られたデータは、サンプル数が十分大きい**母集団 (population)** から得られた**標本(sample)** であるとし、
標本から母集団全体を推定する方法を **推定統計(inferential statistics)** という。

母平均と標本平均を $\mu$ および $m$ 、母分散と標本の分散を $\sigma^2$ および $s^2$ とおく。
経験的に $\mu$ と $m$ は似ているし、$\sigma^2$ と $s^2$ も似ているだろうが、どのように似ているかはわからない。通常、標本から母数をよりよく推定する。

<img src="./Yv2RteVWRz.png">

**標本から母集団の母数の推定**

## 期待値と分散
### 期待値の定義
#### 離散変数の期待値
$X$が確率変数の場合、その期待値を$\textrm{E}[X]$とおく。$X$が離散分布する変数の場合、$X=X_i$になるときの確率を$p_i$とすると

$$ \textrm{E}[X] = \sum_{i=1}^{n} p_i X_i
\label{KRXI5fjSFU}
$$

と表す。
離散分布する変数の例としてはサイコロや宝くじがある。サイコロを1回投げた場合の期待値は、$\frac{1}{6} \cdot 1 +\frac{1}{6} \cdot 2 +\frac{1}{6} \cdot 3 +\frac{1}{6} \cdot 4 +\frac{1}{6} \cdot 5 +\frac{1}{6} \cdot 6 = \frac{1+2+3+4+5+6}{6}=3.5$である。また、平成28年11~12月に行われた年末ジャンボ宝くじの発売数と当選数、当選金額は以下のとおりである。

**宝くじ当せん金・本数(発行枚数が5億枚の場合**

|等級等 | 当せん金 | 本数 |
----| ----|----
|1等 | 700,000,000円 | 25本 |
|1等の前後賞 | 150,000,000円 | 50本 |
|1等の組違い賞 | 500,000円	 & 4,975本 |
|2等 | 15,000,000円 | 500本 |
|3等 | 1,000,000円 | 5,000本 |
|4等 | 10,000円 | 500,000本 |
|5等 | 3,000円 | 5,000,000本 |
|6等 | 300円 | 50,000,000本 |

この場合、期待値は149.975円となる。

#### 連続変数の期待値
$x$が連続分布する変数の場合、$x$の確率密度関数を$f(x)$とすると、

$$ \textrm{E}[x] = \int_{-\infty}^{\infty} xf(x) dx $$

と表す。$x$と$x$が起こる確率$P(x)$の積の総和が期待値であることには変わりはない。
離散変数の期待値と比較すると、総和の記号($\Sigma$)が積分記号($\int$)に、$f(x) \mathrm{d}x$は$x$の時の確率$P(x)$に対応している。

### 母集団
### 母平均と母分散の定義
離散変数および連続変数$X$についての期待値を、母平均$\textrm{E}[X] = \mu_X$と定義する。
$X$についての分散$\textrm{V}[X] = \textrm{E}[(X-\textrm{E}[X])^2]$を母分散$\textrm{V}[X] = \sigma_X^2$と定義する。

### 1変数の平均と分散}
正規分布を例に、期待値と分散の性質を理解する。様々な事象が持つばらつきや誤差の多くは正規分布に従うことが知られている。以下の演習にて
目で見てみよう。

```
# 平均10、標準偏差2の正規分布をもつ母集団から、10個の標本をランダムに取り出す
rnorm(n=10, mean=10, sd=2)
# 結果が見えたか。10回シミュレーションしなさい。毎回結果はどうなるか。

# 次は散布図にて観察する。 n=100
stripchart(rnorm(n=100, mean=10, sd=2), method="jitter", pch=".")
# n=5000 にして標本数を大きくする
stripchart(rnorm(n=5000, mean=10, sd=2), method="jitter", pch=".")
# 10回シミュレーションしなさい。 平均値はどのあたりを推移するか。

# 散布図では数がわからないので、ヒストグラムを作成する。
# nclassオプションは最大値と最小値の間をnclassの数で均等に分割して、区間を自動的に設定してくれる
便利な機能である。分布の概略をつかみたいだけの場合は便利である
hist(rnorm(n=5000, mean=10, sd=2), nclass=100)
# 10回シミュレーションしなさい。ランダムにサンプリングされているが、個体数が多いと母集団の概略が見えてくるだろう

# sdを大きくしたり、小さくしたりして、ヒストグラムを眺めてみてください。横軸の単位を注意深く見ましょう
# 5回いじってみてください。
hist(rnorm(n=5000, mean=10, sd=1), nclass=100)
hist(rnorm(n=5000, mean=10, sd=3), nclass=100)
hist(rnorm(n=5000, mean=10, sd=10), nclass=100)

# 平均値の計算をしなさい。10回シミュレーションしなさい。平均値がばらつくのはなぜですか？
mean(rnorm(n=5000, mean=10, sd=2))
# 標準偏差を100に変更して、平均値の計算をしなさい。10回シミュレーションしなさい。標準偏差2のときにくらべてなにか気が付きますか。
mean(rnorm(n=5000, mean=10, sd=100))

# 不偏分散を計算しなさい。10回シミュレーションしなさい。(ヒント: 標準偏差の二乗が分散です)
var(rnorm(n=5000, mean=10, sd=2))
# 標準偏差を100に変更して、不偏分散の計算をしなさい。10回シミュレーションしなさい。標準偏差2のときにくらべてなにか気が付きますか。
var(rnorm(n=5000, mean=10, sd=100))
```

### 2変数の平均と分散
確率変数$X$と$Y$の2変数を足したり引いたりしたときの平均と分散はどのように変化するだろうか。以下が公式である。

#### 期待値の公式
確率変数$X$についての期待値は

$$\textrm{E}(X) = \mu_X $$

であり、母平均$\mu_X$の定義である。$a$が定数のとき、

$$
	\textrm{E} [a] &= a \quad \mbox{(定数の期待値は定数)}\\
	\textrm{E} [X + a] &= \textrm{E}[X] + a  \quad \mbox{(定数は外に出せる1)}\\
	\textrm{E} [aX] &= a\textrm{E}[X] \quad \mbox{(定数は外に出せる2)}\\
	\textrm{E} [X+Y] &= \textrm{E}[X]+\textrm{E}[Y]  \quad \mbox{(期待値の和は、和の期待値と等しい)}\\
	\textrm{E} [XY] =&\textrm{E}[X]\textrm{E}[Y] \quad (ただし、XとYが独立の場合) \\
$$

が成り立つ。

#### 分散の公式
確率変数$X$についての分散の定義は、

$$\textrm{V}[X] = \textrm{E}[(X-\textrm{E}[X])^2] = \sigma_X^2 $$
である。$a$が定数とすると

$$
	&\textrm{V}[a] = 0 \quad \mbox{(定数の分散は0)}\\
	&\textrm{V}[aX] = a^2 \textrm{V}[X] \quad \mbox{($X$の$a$倍の分散は、$X$の分散の$a^2$倍)}\\
	&\textrm{V}[X + a] = \textrm{V}[X] \mbox{(定数の和は無視)} \\
$$
である。

```
# 平均10、標準偏差2の正規分布に従うXを5000個ランダムサンプリング
X=rnorm(n=5000, mean=10, sd=2)
# 平均23、標準偏差5の正規分布に従うYを5000個ランダムサンプリング
Y=rnorm(n=5000, mean=23, sd=5)
# 散布図を書きなさい。平均はどのあたりですか
stripchart(X+Y, method="jitter", pch=".")
# ヒストグラムを書きなさい、平均はどのあたりですか
hist(X+Y, nclass=100)
# 平均を計算しなさい
mean(X+Y)
# 不偏分散を計算しなさい。得られた不偏分散は理論値と比べていかがですか。(ヒント var(X)+var(Y) = sd(X)^2 + sd(Y)^2)
var(X+Y)
```

\paragraph{共分散}
確率変数$X$と$Y$について$\textrm{V}[X]  = \sigma_X^2$および$\textrm{V}[Y]  = \sigma_Y^2$のとき、
\begin{equation}
	\textrm{V}[X \pm Y] = \textrm{V}[X] + \textrm{V}[Y] \pm 2 \cdot \textrm{Cov}[X,Y]
	\label{eq:Y4lOpwxCF7HN}
\end{equation}
である。ただし、\textrm{Cov}[X,Y]は{\bf 共分散(co-variance)}といい、
\begin{equation}
\begin{split}
	&\textrm{Cov}[X,Y] = \textrm{E}[ ( X - \textrm{E}(X) )( Y - \textrm{E}(Y))] = r \cdot  \sigma_X \cdot \sigma_Y 
\end{split}
\end{equation}
の性質を持つ。$r$は{\bf 相関係数}といい、 $-1 \leq r \leq  1$の範囲を持つ\footnote{相関係数については、第6回「相関と回帰」にて
説明する。}。$X$と$Y$が独立の場合は $r=0$となり、$\textrm{Cov}[X,Y]=0$であるため、
\begin{equation}
\begin{split}
	\textrm{V}[X \pm Y] = \textrm{V}[X] + \textrm{V}[Y] 
\end{split}
\end{equation}
となる。すなわち、分散は$X$と$Y$が独立ならば、$X+Y$の分散は、$X$の分散と$Y$の分散に分割できる。


%%%%%%%%%%%%%%
\subsubsection{練習問題}
%%%%%%%%%%%%%%
\begin{enumerate}
  \item コムギの10アール(a)当たり収量について、品種Aの収量をしめす確率変数$A$は母平均386.1 kg/10aおよび母標準偏差25.4 kg/10aをもつ。コムギの20アールにおける母平均と母標準偏差はいくつが期待されるか。
  \item コムギ品種Bの確率変数$B$は母平均333.6 kg/10aおよび母標準偏差は22.4 kg/10aをもつと仮定する。品種Aを10 a、品種Bを10 a育成した場合、両者を合わせたコムギ収量の母平均と母標準偏差はいくつか。ただし、品種Aと品種Bの育成は相互に影響を与えない(独立)とする。
  \item 品種Aを10 a、品種Bを20 a育成した場合、両者を合わせたコムギ収量の母平均と母標準偏差はいくつか。ただし、品種Aと品種Bの育成は相互に影響を与えない(独立)とする。
\end{enumerate}

%%%%%%%%%%%%%%
\subsubsection{練習問題こたえ}
%%%%%%%%%%%%%%
\begin{enumerate}
  \item $\textrm{E}[2A] = 2\textrm{E}[A] = 2 \cdot 386.1 = 772.2$、$\textrm{V}[2A] = 2^2 \cdot \textrm{V}[A] = 4 \cdot 25.4^2 = 2580.64$。ゆえに母平均は772.2、母標準偏差は$\sqrt{2580.64}=50.8$である。
  \item $\textrm{E}[A+B] = \textrm{E}[A]+\textrm{E}[B]=386.1+333.6 = 719.7$ kg/10aである。また、$\textrm{V}[A+B]=\textrm{V}[A] + \textrm{V}[B] = 25.4^2 + 22.4^2 =1146.92$より、母標準偏差は$\sqrt{1146.92}\fallingdotseq33.87$である。
  \item $\textrm{E}[A+2B] = \textrm{E}[A]+\textrm{E}[2B]=386.1+2 \cdot 333.6 = 1053.3$ kg/10aである。また、$V[A+2B]=\textrm{V}[A] + \textrm{V}[2B] = 25.4^2 + 4 \cdot 22.4^2 =2652.2$より、母標準偏差は$\sqrt{2652.2}\fallingdotseq51.50$である。

Rでシミュレーションして確かめてみると、理解が深まる。
\end{enumerate}

%%%%%%%%%%%%%%%%%%
\subsection{標本集団}
%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%
\subsubsection{標本$X$から母平均を推定}
%%%%%%%%%%%%%%

母集団からランダムにサンプリングした標本$X$の期待値は、母集団から取り出したものだから、期待値は母平均と変わらない。
\begin{equation}
	E[X] = \mu_X
\end{equation}

一方、標本の平均$\bar X = \frac{X_1 + X_2 + \cdots + X_n}{n}$は、(さっきRでシミュレーションしましたが、)母平均と一致しない。
しかし、n=10から5000、10000と大きくすると、標本の平均$\mu_X$は母集団の期待値(すなわち母平均)$E[\bar X] $に近づく(さっきシミュレーションしました)。
これを{\bf 大数の法則}という。

すなわち、{\bf 母平均$\mu_X$の推定値として、標本平均$\bar{X}$を用いてもいいよ、ということ。}

%%%%%%%%%%%%%%
\subsubsection{標本$X$から母分散を推定}
%%%%%%%%%%%%%%

標本の不偏分散
\begin{equation}
s^2 = \frac{(X_1 - \bar X)^2 + \cdots + (X_n - \bar X)^2}{n-1} 
\end{equation}
の期待値は、母分散$\sigma_X^2$と等しい。
\begin{equation}
E[s^2]  = \sigma_X^2
\end{equation}
すなわち、{\bf 母分散$\sigma_X$の推定値として、$s^2$を用いてもいいよ、ということ。}

%%%%%%%%%%%%%%
\subsubsection{標本平均$\bar{X}$の分散の推定}
%%%%%%%%%%%%%%
中心極限定理から、標本平均の分散の期待値$\textrm{V}[\bar X]$は、標本の不偏分散$s^2$を個体数$n$で割った値と等しい。。
\begin{equation}
 \textrm{V}[\bar X] = \frac{s^2}{n}
\end{equation}

すなわち、{\bf 標本$X$の平均$\bar{X}$をとると、分散は$n$分の1になるよ、ということ。}平均を取った方が母平均の推定値として安定する、ということだね。
この平方根$s/\sqrt{n}$を{\bf 標準誤差 (Standard error)} といい、標本の平均値の標準偏差である。


%%%%%%%%%%%%%%
\subsubsection{練習問題}
%%%%%%%%%%%%%%
コムギ品種Aの10アール(a)当たり収量について、5箇所の調査を行い、$280, 290, 300, 260, 255$ kg/10aのデータを得た。
\begin{enumerate}
  \item コムギ品種Aの母平均、母分散、母標準偏差を推定せよ。
  \item 標本平均の標準誤差を求めよ。

\end{enumerate}

%%%%%%%%%%%%%%
\subsubsection{練習問題こたえ}
%%%%%%%%%%%%%%
\begin{enumerate}
  \item 標本平均はmean()関数、不偏分散はvar()関数にて求める。
\begin{breakbox}
\begin{verbatim}
a = c(280, 290, 300, 260, 255)
mean(a)
[1] 277
var(a)
[1] 370
\end{verbatim}
\end{breakbox}
よって、標本平均は277, 不偏分散は370
   \item 母平均の不偏推定値は標本平均である。母分散の不偏推定量は不偏分散である。母分散の平方根は母標準偏差(定義)である。
\begin{breakbox}
\begin{verbatim}
sqrt(var(a))
[1] 19.23538
\end{verbatim}
\end{breakbox} 
よって、母平均の不偏推定値は277、母分散の不偏推定量は370、母標準偏差の不偏推定値は370の平方根の19.23538である。
   \item  標本平均の標準誤差は、不偏分散を標本数で割った平方根。
\begin{breakbox}
\begin{verbatim}
sqrt(var(a)/5)
[1] 8.602325
\end{verbatim}
\end{breakbox} 
よって、標本平均の標準誤差は8.602325である。

\end{enumerate}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newpage
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{確率密度関数}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
　連続型の確率変数$x$について、$x$の確率が区間$a \leq x \leq b$における定積分
\begin{equation}
\begin{split}
	P(a \leq x \leq b) = \int_a^b f(x) dx
\end{split}
\end{equation}
と表される場合、$f(x)$を{\bf 確率密度関数 (probability density function)}という(図\ref{fig:slndj5})。$a=b$の場合$P(x=a)=0$である。
{\bf 連続変数の場合、確率は点ではなく 区間で推定}する。
確率密度関数には、正規分布(normal distribution)、指数分布 (exponential distribution)、
ガンマ分布(gamma distribution)、ベータ分布(Beta distribution)　などがある。

%%%%%%%%%%%%%%%%%%%%
\subsection{正規分布}
%%%%%%%%%%%%%%%%%%%%
 {\bf 正規分布 (Normal distribution)}はもっとも代表的な連続型の確率密度関数であり、
\begin{equation}
\begin{split}
	f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \mathrm{exp} \left\{\frac{-(x-\mu)^2}{2\sigma^2} \right\} \quad (-\infty < x < \infty)
	\label{eq:JEnj1DYI}
\end{split}
\end{equation}
とあらわされる。$\mathrm{exp}(x)$はネイピア数$e=2.718\cdots$の$x$乗であることを示す。$x$が平均$\mu$、分散$\sigma^2$の
正規分布に従う場合、$x \sim \mathcal{N}(\mu, \sigma^2)$と表記する。
式(\ref{eq:JEnj1DYI})は、山なりの曲線である$y=e^{-x^2}$について、$x-\mu$にてx軸方向の平行移動、$\sigma^2$による割り算で、x軸方向のスケーリングをしている。発見者のC. F. ガウスにちなみガウス(ガウシアン)分布とも呼ばれる。彼は天文観測データの誤差が正規分布にしたがうことを発見した。$x$の定義域は$-\infty<x<\infty$であるため、確率の要件を満たすため
\begin{equation}
\begin{split}
	P(-\infty \leq x \leq \infty) = \int_{-\infty}^{\infty} f(x) dx = 1
\end{split}
\end{equation}
となるように$\frac{1}{\sqrt{2\pi \sigma^2}}$をかけて調整している。

\begin{figure}[htbp]
\begin{center}
 \fbox{\includegraphics[clip,width=8.0cm]{./slndj5.png}}
 \caption{確率密度関数}
 \label{fig:slndj5}
\end{center}
\end{figure}

%%%%%%%%%%%%%%%%%%%%
\subsection{正規分布の例}
%%%%%%%%%%%%%%%%%%%%
厚生労働省平成21年度体力・運動能力調査によると、日本人男性20才の平均身長(m)は1.7166、
標準偏差は0.0560、女性の平均身長は1.5832、標準偏差は0.0552であり、身長の分布は正規分布に従うことが
知られている。

\paragraph{グラフでの理解}
curve()はグラフを描画するRコマンドである。curve(expr =関数、from=xの最小値、to=xの最大値)のように指定すると、
exprに指定した関数$f(x)$のグラフを描画できる。男性の正規分布の確率密度関数のグラフを1.2mから2.0mの範囲でRに描画させる。
\begin{breakbox}
\begin{verbatim}
m = 1.7166  # 平均
v = 0.0560^2   #分散は標準偏差の二乗で0.003136
# curve()コマンドを用いて正規分布曲線を描画
curve(expr=(1/sqrt( 2*pi*v )*exp ( -(x - m)^2 / (2*v) ) ), from=1.2,  to=2.0)
\end{verbatim}
\end{breakbox}
と入力し、図\ref{fig:NuhXvQik}で示すようなグラフが描画される。正規分布関数は
慣れないうちはタイプミスや勘違いで入力が大変なので、コピペすればよい。

\begin{figure}[htbp]
\begin{center}
 \fbox{\includegraphics[clip,width=6.0cm]{./NuhXvQik.png}}
 \caption{curve()コマンドにて作成した平均1.7166、分散0.003136の正規分布}
 \label{fig:NuhXvQik}
\end{center}
\end{figure}

確率密度関数$f(x)$は$x=1.7166$に最大値をもち、そこから対称に
裾野を持っていることがわかる。



\begin{itembox}[l]{演習問題}
男性で身長1.7から1.8mの人は全体の何\%か。
\end{itembox}

連続型変数の確率を計算するには、区間の積分をする必要があるが、これは陽(あらわ)に解けないので数値計算にて近似解を求める。
Rコマンドintegrate(ユーザ定義関数、lower=a, upper=b)にて数値積分を行う。
\begin{breakbox}
\begin{verbatim}
m = 1.7166 # 平均
v = 0.0560^2 #分散
# ユーザー定義関数  function()コマンドは慣れないと使いにくい
teigikansuu <- function(x) {1/sqrt(2*pi*v)*exp(-(x-m)^2/(2*v))}
# 数値積分
integrate(teigikansuu,lower=1.7, upper=1.8)
# 結果 数値積分に由来する誤差は6.1 * 10^(-15)でかなり小さい=信頼できる
0.5483425 with absolute error < 6.1e-15
\end{verbatim}
\end{breakbox}
すなわち、全体の54.8\%の人間が身長1.7から1.8mの区間に入る。ユーザー定義関数をfunction()コマンドで
定義したが、正規分布の確率密度関数はRではdnorm(x, mean=平均, sd=標準偏差)である。よって上記は
\begin{breakbox}
\begin{verbatim}
# ユーザー定義関数 
teigikansuu2 <- function(x) {dnorm(x, mean=m, sd=sqrt(v))}
# 数値積分
integrate(teigikansuu2,lower=1.7, upper=1.8)
# おなじ結果が得られる
0.5483425 with absolute error < 6.1e-15
\end{verbatim}
\end{breakbox}
となる。
\begin{itembox}[l]{問題}
身長が1.80m以上の男性は、日本全体で何\%に入るだろうか。
\end{itembox}
\begin{breakbox}
\begin{verbatim}
# 数値積分  1.80から無限大(Inf)まで数値積分
integrate(teigikansuu2,lower=1.80, upper=Inf)
# 結果
0.06820607 with absolute error < 1.4e-06
\end{verbatim}
\end{breakbox}
で全体の上位6.8\%に入る。つまり、平均と標準偏差を知ることにより、正規分布に従う場合は、
正規分布の区間積分により、割合あるいは確率を推定することが可能になる！ことを実感してほしい。


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newpage
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{母平均の点推定と区間推定}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{中心極限定理}
%%%%%%%%%%%%%%
確率変数$X$が母平均$\mu$と母分散$\sigma^2$をもつとき、以下が成り立つ。
\begin{itembox}[l]{中心極限定理1}
nが十分大きい場合、標本平均$\bar{X}$は母平均$\mu$、分散$\sigma^2/n$の正規分布に従う($\bar{X} \sim \mathcal{N}(\mu, \sigma^2/n)$)。
標準化しても成り立ち、
標本平均$\bar{X}$の標準化スコア$Z = (\bar{X} - \mu) / (\sigma / \sqrt{n})$は
母平均$0$、分散$1$の標準正規分布に従う($Z \sim \mathcal{N}(0, 1$))。
 \end{itembox}
これより、{\bf 確率変数$X$が正規分布に従っていなくても、平均値については正規分布を利用した推定を行ってもよい。}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{信頼区間の推定}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$-\infty < z < T_1$を満たす確率密度関数$f(z)$の積分を累積確率$\Phi(z < T_1)$(ふぁいとよむ)としめす(図\ref{fig:rd0jfey})。
$T_2 < z < \infty $を満たす$z$の累積確率は、$\Phi(T_2 < z) = 1-\Phi(z < T_2)$と求められる。


$Z$分布は$z=0$について対称であるが、$\Phi(z < T_1) = (1-0.95) / 2 = 0.025$を満たす$T_1$と
$1 - \Phi(z < T_2) =1 - (1 - 0.025) = 0.025$を満たす$T_2$に挟まれた領域に$z$は95\%の確率で存在する。
これを$z$の信頼区間といい、$T_1$を下側信頼限界、$T_2$を上側信頼限界という。

R関数のqnorm(累積確率)にて、標準正規分布において$-\infty$から$z$までの累積確率が、ユーザーが与えた累積確率になるときの$z$を求めることが
できる。

\begin{figure}[htbp]
\begin{center}
 \fbox{\includegraphics[clip,width=9.0cm]{./rd0jfey.png}}
 \caption{95\%信頼区間.}
 \label{fig:rd0jfey}
\end{center}
\end{figure}


\begin{breakbox}
\begin{verbatim}
# T1を求める場合
qnorm(0.025)
# 結果
[1] -1.959964

# T2を求める場合
qnorm(0.975)
# 結果
[1] 1.959964   # 標準正規分布は左右対称なので、T2はT1にマイナス1をかけた値。
\end{verbatim}
\end{breakbox}
よって、$Z$の信頼区間から、$\bar{X}$の範囲を求めるように逆算すると
\begin{equation}
	\begin{split}
	& -1.959964 <Z = (\bar{X} - m) / (\sigma / \sqrt{n}) < 1.959964 \\
	& -1.959964 \cdot \sigma / \sqrt{n} <\bar{X} - m < 1.959964  \cdot \sigma / \sqrt{n} \\
	& -1.959964 \cdot \sigma / \sqrt{n} + m < \bar{X} < 1.959964 \cdot \sigma / \sqrt{n} + m \\
	\end{split}
	\label{eq:ikp7yrnq}
\end{equation}
となる。母分散既知の時の$\bar{X}$の95\%の信頼区間である。$\bar{X}$を推定するとき、。$\bar{X}=(X_1 + X_2 + \cdots + X_n)/n$と
単一の数字として推定することを{\bf 点推定}という。いっぽう、信頼区間に基づいて$\bar{X}$を区間で推定する場合を{\bf 区間推定}という。

\paragraph{解説} 母平均$\mu$は未知だが定数である。一方、確率変数$X$がばらつくので、
標本平均$\bar{X}$も標本が変わるたびばらつく。毎回違う値なんだけれども、$ -1.959964 \cdot \sigma / \sqrt{n} + m < \bar{X} < 1.959964 \cdot \sigma / \sqrt{n} + m $の区間に95\%の確率で入る、という意味である。標本をとって標本平均を計算する、を繰り返すと、100回に95回は95\%信頼区間の中に入る頻度である。
標本平均として$\bar{X}$と$m$が説明の中で出てくるが、両者の違いは、$\bar{X}$は変数で、$m$は標本から計算される具体的な値である。


%%%%%%%%%%%%%%
\subsection{母分散既知の場合}
%%%%%%%%%%%%%%
\subsubsection{1標本問題}
\begin{itembox}[l]{例題}
ある道の駅でリンゴMサイズ1箱を購入し、入っていた12個のリンゴの重さ(グラム)を計測したところ、$A = \{329.5, 316.7, 336.3, 336.0, 325.9,
327.2, 326.4, 356.5, 325.1, 324.4, 341.0, 353.5\}$であった。Mサイズの母分散$9^2$であることが分かっている。標本平均$\bar{A}$についての
点推定と95\%信頼区間の推定を行いなさい。
\end{itembox}
\paragraph{考え方}
おなじ確率分布から得られるデータ群が1つの場合である。これを1標本問題という。母分散がすでに分かっていないと、問題として成立しないので、
標本が一つで母分散が示されていれば、1標本問題として処理しましょう。

\paragraph{解答例}
$E[\bar{A}]=\mu$より、標本平均が母平均の一致推定量である。よって標本平均$\bar{A}=(329.5 + 316.7 + 336.3 + 336.0 + 325.9 + 327.2 + 
326.4 + 356.5 + 325.1 + 324.4 + 341.0 + 353.5)/12 \fallingdotseq 333.2$が点推定量である。一方、95\%信頼区間は
式(\ref{eq:ikp7yrnq})より、$ -1.959964 \cdot 9 / \sqrt{12} + 333.2 \fallingdotseq 328.1 < \bar{A} < 1.959964 \cdot 9 / \sqrt{12}+ 332.3 \fallingdotseq 338.3$である。

\subsubsection{2標本問題}
\begin{itembox}[l]{例題}
 ある飼育法により昆虫個体群XとYを飼育したとする。飼育法以外の条件を均一にそろえたうえで、個体群XおよびYの昆虫重量 (mg)は
 $X=\{27.6, 19.0, 20.1, 24.7, 21.8, 21.7\}$、$Y=\{26.1, 27.1, 23.0, 25.9, 19.4, 22.7\}$であった。個体群XおよびYの母分散は
 $\sigma_X^2 = 4.0^2$および$\sigma_Y^2 = 2.9^2$であることがわかっている。$X$と$Y$平均の差についての確率変数、
 すなわち$\bar{X}-\bar{Y}$についての点推定および区間推定を行いなさい。
 \end{itembox}
\paragraph{考え方1}
上記は独立の確率分布から得られるデータ群が二つの場合である。これを二標本問題といい、しばしばこの両者を比較する問題である。
この節では、この二標本それぞれの母分散がすでに分かっている場合について解説をする。一方、母分散がわかっていない場合、次節のカイ二乗
分布とt分布の考え方が必要になってくる。\\


\paragraph{考え方2\\}
難しいが、順を追って処理しよう。
{\bf (Step 1. まずは定義)} 
確率変数$X \sim \mathcal{N}(\mu_x, \sigma_x^2)$および$Y \sim \mathcal{N}(\mu_y, \sigma_y^2)$があり、
標本平均の確率変数を$\bar{X} = 1/m (X_1 + X_2 + \cdots + X_m)$および、$\bar{Y} = 1/n (Y_1 + Y_2 + \cdots + Y_ n)$とおく。\\
{\bf (Step 2. 二つの正規分布の和あるいは差に由来する正規分布の特性)}
中心極限定理より、$\bar{X} \sim \mathcal{N}(\mu_x, \sigma_x^2/m)$および$\bar{Y} \sim \mathcal{N}(\mu_y, \sigma_y^2/n)$であるから、
正規分布あるいは期待値の特性(式\ref{eq:JtVTI3dH}と\ref{eq:sHoyELqU42Dx})より、$\bar{X}-\bar{Y} \sim \mathcal{N}(\mu_x - \mu_y, \sigma_x^2/m + \sigma_y^2/n)$である。\\
{\bf (Step 3. 標本平均の差に関する点推定量)}
$E[\bar{X} -\bar{Y}] = E[\bar{X}] -E[\bar{Y}] = \mu_x - \mu_y$だから、 $\bar{X} -\bar{Y}$が一致推定量。\\
{\bf (Step 4. 標準正規分布への帰着)}つぎに、95\%信頼区間推定を行う。$\bar{X}-\bar{Y}$の標準化$Z$は、定義通り
\begin{equation}
	\begin{split}
	Z = \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{\sigma_x^2/m + \sigma_y^2/n}}
	\end{split}
	\label{eq:KKJybRhR}
\end{equation}
であり、標準正規分布$\mathcal{N}(0,1)$に従う。\\
{\bf (Step 5. 区間推定)}  95\%信頼区間において、下側信頼限界($z_1$)は$z_1=-1.959964$、上側信頼限界($z_2$)は$z_2=1.959964$だから、
\begin{equation}
	\begin{split}
	z_1 < &Z < z_2 \\
	-1.959964 < &\frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{\sigma_x^2/m + \sigma_y^2/n}} < 1.959964 \\
	-1.959964 \cdot \sqrt{\sigma_x^2/m + \sigma_y^2/n} < &(\bar{X}-\bar{Y}) - (\mu_x - \mu_y) < 1.959964 \cdot \sqrt{\sigma_x^2/m + \sigma_y^2/n} \\
	-1.959964 \cdot \sqrt{\sigma_x^2/m + \sigma_y^2/n} + (\mu_x - \mu_y) < &\bar{X}-\bar{Y} < 1.959964 \cdot \sqrt{\sigma_x^2/m + \sigma_y^2/n} + (\mu_x - \mu_y) \\
	\end{split}
	\label{eq:slbemgj5}
\end{equation}

\paragraph{解答例}
標本平均の差$m_x - m_y$が標本平均の差の一致推定量である。$m_x = (27.6+19.0+20.1+24.7+21.8+21.7)/6 =22.48333$、$m_y = (26.1+27.1+23.0+25.9+19.4+22.7)/6=24.03333$より$E[\bar{X} - \bar{Y}]=22.48333-24.03333 = -1.55$が標本平均の差の点推定量。95\%信頼区間については式(\ref{eq:slbemgj5})に代入して、$-5.50 < \bar{X} - \bar{Y} < 2.40$である。


%%%%%%%%%%%%%%
\subsection{母分散未知の場合}
%%%%%%%%%%%%%%

%%%%%%%%%%%%%%
\subsubsection{$t$分布}
%%%%%%%%%%%%%%

前節では、母分散$\sigma^2$が既知の時、標準正規分布
\begin{equation}
	Z = \frac{\bar{X}-\mu}{\sqrt{\sigma^2/n}}
\end{equation}
を考えた。一方、母分散$\sigma^2$が未知の場合、$\sigma^2$の代わりに$s^2$を用いて
\begin{equation}
	t = \frac{\bar{X}-\mu}{\sqrt{s^2/n}}
	\label{NOcyH5hANm}
\end{equation}
をスチューデントの$t$統計量として新たに定義する。$t$統計量は自由度$n-1$の$t$分布に従う。
$t$分布は自由に動ける変数のかず「自由度」によってその分布が変化する。$t$分布表を参照するか、統計ソフトを用いて信頼区間の推定を行う。


\paragraph{$t$分布と$z$分布(標準正規分布)をRで比較してみよう！} とにかくやってみる。自由度(degree of freedom (df))が大きくなるにつれて
標準正規分布に近づくのがお分かりか。dnormは標準正規分布をあらわす。 dtは$t$分布で自由度を要求する。

\begin{breakbox}
\begin{verbatim}
curve(dnorm,-4,4)  # まず標準正規分布のグラフ
curve(dt(x,df=1),-4,4,add=T,lty=2)  #自由度1のt分布を追加
curve(dt(x,df=3),-4,4,add=T,lty=3)  #自由度3のt分布を追加
curve(dt(x,df=10),-4,4,add=T,lty=4)  ##自由度10のt分布を追加
\end{verbatim}
\end{breakbox}

\begin{figure}[htbp]
\begin{center}
 \fbox{\includegraphics[clip,width=9.0cm]{./wdk32jah.png}}
 \caption{標準正規分布にどんどん近づく$t$分布。}
 \label{fig:wdk32jah}
\end{center}
\end{figure}

$t$分布は$n \rightarrow \infty$で標準正規分布$\mathcal{N} (0, 1)$に近づく。


\paragraph{母分散が未知だが等しいと仮定するとき($\sigma_x^2 = \sigma_y^2 = \sigma^2)$\\ \\}
\begin{itembox}[l]{例題}
 ある飼育法により昆虫個体群XとYを飼育したとする。飼育法以外の条件を均一にそろえたうえで、個体群XおよびYの昆虫重量 (mg)は
 $X=\{27.6, 19.0, 20.1, 24.7, 21.8, 21.7\}$、$Y=\{26.1, 27.1, 23.0, 25.9, 19.4, 22.7\}$であった。個体群XおよびYの母分散は
不明であるが、等しいと仮定する。$X$と$Y$平均の差$\bar{X}-\bar{Y}$についての点推定および区間推定を行いなさい。
 \end{itembox}
 
\paragraph{$t$分布を例題に当てはめて考える}
式(\ref{eq:KKJybRhR})は$\sigma_x^2 = \sigma_y^2 = \sigma^2$より
\begin{equation}
	\begin{split}
	Z &= \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{\sigma_x^2/m + \sigma_y^2/n}} \\
	&= \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{(1/m + 1/n)\sigma^2}} (\because \sigma_x^2 = \sigma_y^2 = \sigma^2)
	\end{split}
\end{equation}
ここで$X$と$Y$の標本不偏分散の{\bf プールした分散 (pooled variance)}$s_p^2$ を考える。
\begin{equation}
	\begin{split}
	s_p^2 &= \frac{\sum_{i=1}^{m}(X_i - \bar{X})^2 + \sum_{j=1}^{n}(Y_j - \bar{Y})^2}{(m-1) + (n-1)} \\
	\end{split}
\end{equation}
$X$と$Y$が与えられている場合は、上記のように計算できるが、$s_x^2$および$s_y^2$のみ与えられている場合は、
\begin{equation}
	\begin{split}
	s_p^2 &= \frac{(m-1)s_x^2 + (n-1)s_y^2}{(m-1) + (n-1)} (\because s_x^2 = \frac{\sum_{i=1}^{m}(X_i - \bar{X})^2}{m-1})
	\end{split}
\end{equation}
と求める。
式(\ref{eq:LajlNviyHv})より、
\begin{equation}
	\begin{split}
	t = \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{(1/m + 1/n) s_p^2}}
	\end{split}
\end{equation}
となり、２標本$t$統計量は自由度$m+n-2$の$t$分布に従う。



\paragraph{考え方2 $\quad $信頼区間の推定}
図\ref{fig:rvtn2q4p}を見てほしい。$t$分布は$t=0$について対称であるので、95\%信頼区間の下側信頼限界は
$\Phi(T_1 < t) = (1-0.95) / 2 = 0.025$を満たす$T_1$であり、上側信頼限界は$1 - \Phi(T_2 > t) =1 - (1 - 0.025) = 0.025$を満たす$T_2$である。
R関数のqt(累積確率, df=m+n-2)にて、t分布において$-\infty$から$t$までの累積確率が、ユーザーが与えた累積確率になるときの$t$を求めることが
できる。自由度が$m+n-2=6+6-2=10$のときの上側および下側信頼限界を求める。

\begin{figure}[htbp]
\begin{center}
 \fbox{\includegraphics[clip,width=9.0cm]{./rvtn2q4p.png}}
 \caption{$t$分布における信頼区間推定。ちょっと形が違うのが伝わります！？}
 \label{fig:rvtn2q4p}
\end{center}
\end{figure}

\begin{breakbox}
\begin{verbatim}
# T1を求める場合
qt(0.025, df=10)
# 結果
[1] -2.228139

# T2を求める場合
qt(0.975,df=10)
# 結果
[1] 2.228139 # T1にマイナス1をかけただけの値であることに注意
\end{verbatim}
\end{breakbox}
よって、95\%信頼区間は、
\[
	-2.228139 < t = \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{(1/m + 1/n) s_p^2}}  < 2.228139
\]
$\bar{X}-\bar{Y}$で整理して
\begin{equation}
	\begin{split}
	-2.228139 \cdot \sqrt{(1/m + 1/n) s_p^2} +  (\mu_x - \mu_y) &< \bar{X}-\bar{Y} < 2.228139 \cdot \sqrt{(1/m + 1/n) s_p^2}  +  (\mu_x - \mu_y) \\
	\end{split}
\end{equation}
それではRの標準関数でコツコツ解いてみよう。
\begin{breakbox}
\begin{verbatim}
X= c(27.6, 19.0, 20.1, 24.7, 21.8, 21.7)
Y = c(26.1, 27.1, 23.0, 25.9, 19.4, 22.7)
mean_X = mean(X)  # Xの標本平均 値は22.48333
mean_Y = mean(Y)  # Yの標本平均　値は24.03333
var_X = var(X)  # Xの標本不偏分散  値は9.997667
var_Y = var(Y)  # Yの標本不偏分散  値は8.294667 (等しいと仮定する)
pooled_var = (var_X * 5 + var_Y * 5 ) / (6+6-2)  # 9.146167

# 標本平均の差の推定値
mean_X - mean_Y
[1] -1.55
# 95%下側信頼限界をもとめる
qt(0.025,df=10)*( sqrt( ( 1/6 + 1/6 ) * pooled_var) )+(mean_X - mean_Y) 
[1] -5.440462
# 95%上側信頼限界をもとめる
qt(0.975,df=10)*( sqrt( ( 1/6 + 1/6 ) * pooled_var) )+(mean_X - mean_Y) 
[1] 2.340462
\end{verbatim}
\end{breakbox}
これはRの専用関数t.test()関数で一撃である。標本$X$と標本$Y$の分散が等しいことは
var.equal = TRUEと指示する。また、両側確率を求めるため、alternative = c("two.sided")を
指定している。
\begin{breakbox}
\begin{verbatim}
t.test(X,Y,var.equal = TRUE, alternative = c("two.sided"))
##### 以降 結果の表示  ######
	Two Sample t-test

data:  X and Y
t = -0.88771, df = 10, p-value = 0.3955   # t値、自由度=10, p値 (検定の回に説明)
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:   # 95%信頼区間
 -5.440462  2.340462  
sample estimates:
mean of x mean of y 
 22.48333  24.03333 
\end{verbatim}
\end{breakbox}
デフォルトで95\%信頼区間を求めている。上記の95 percent confidence interval: の箇所を参照すればよい。99\%信頼区間を求めたい場合は
conf.level = 0.99にて指定する。
\begin{breakbox}
\begin{verbatim}
t.test(X,Y,var.equal = TRUE,alternative = c("two.sided"), conf.level = 0.99)
##### 以降 結果の表示  ######
	Two Sample t-test

data:  X and Y
t = -0.88771, df = 10, p-value = 0.3955
alternative hypothesis: true difference in means is not equal to 0
99 percent confidence interval:  # 99%信頼区間
 -7.083737  3.983737
sample estimates:
mean of x mean of y 
 22.48333  24.03333 
\end{verbatim}
\end{breakbox}
t.test()関数、便利ですよね。。。きちんとt分布の区間推定ができたなら、t.test()関数のありがたみがわかる。




\paragraph{母分散が未知だが等しいとは限らないとき($\sigma_x^2 \neq \sigma_y^2$)}
式(\ref{eq:KKJybRhR})の$\sigma_x^2$に$s_1^2$、$\sigma_y^2$に$s_2^2$を代入した
\begin{equation}
	\begin{split}
	t = \frac{(\bar{X}-\bar{Y}) - (\mu_x - \mu_y)}{\sqrt{s_1^2/m + s_2^2/n}}
	\end{split}
\end{equation}
は近似的に自由度が
\begin{equation}
	\begin{split}
	\nu = \cfrac{\left( \cfrac{s_1^2}{m} + \cfrac{s_2^2}{n} \right)^2}{\cfrac{(s_1^2/m)^2}{m-1}+\cfrac{(s_2^2/n)^2}{n-1}}
	\end{split}
\end{equation}
に最も近い整数$\nu^*$(ニュー、スターと読む)の$t$分布$t(\nu^*)$に従うことが知られている。これをウェルチの近似法という。\\
Rでは、先ほどのt.test()関数のうち、等分散性を仮定しないvar.equal = FALSEを指定する。
\begin{breakbox}
\begin{verbatim}
t.test(X,Y,var.equal = FALSE,alternative = c("two.sided"))
##### 以降 結果の表示  ######
	Welch Two Sample t-test   # Welch法との表示に切り替わる。

data:  X and Y
t = -0.88771, df = 9.9141, p-value = 0.3957
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -5.445038  2.345038
sample estimates:
mean of x mean of y 
 22.48333  24.03333 
\end{verbatim}
\end{breakbox}

%%%%%%%%%%%%%%
\subsubsection{第二回演習のレポート課題}
%%%%%%%%%%%%%%
まず課題データをRでダウンロードし、オブジェクトに保存してください。
\begin{breakbox}
\begin{verbatim}
URL3 = "https://raw.githubusercontent.com/qikushu/stat/master/kadai_R3.txt"
kadai_data3 = read.table(URL3, head=T)
\end{verbatim}
\end{breakbox}
うまく読め込めたでしょうか。\\

今回は日本型イネ台中65号とアウス型(いわゆる印度型の一種)イネDV85の交雑F2を自殖して得られた
組換え自殖系統群(Recombinant Inbred Line)という種類のイネで、ほぼすべての遺伝子型が台中65号ホモ接合型(課題
データではAと表記)とDV85ホモ接合型(課題データではBと表記)に固定している。それは今回の統計の授業には関係ないが、
とにかく、いわゆるメンデルの遺伝の法則のAAホモ型とBBホモ型でABのヘテロ接合型はほぼない、ということだ。\\
HD93とは1993年にイネを播種して出穂するまでの到穂日数の日数について、この系統群について観察した結果である。この
到穂日数と関連のあるゲノム領域を探索するため、100個以上のDNAマーカーを用いて遺伝子型を解析している。
今回の課題では、そのうち染色体1に座乗(ざじょう)するDNAマーカーC813と染色体8に座乗するDNAマーカーR902によって
調査したこのゲノム領域の遺伝子型が判明している。HD93が90とは大体播種から出穂まで90日、約三か月かかっているということだ。
それではてならしに、第一回演習で行った記述統計の解析を行う。次に、今日解説した方法を用いて、各遺伝子型別に
イネ系統を分類し、到穂日数の平均値に関する点推定と信頼区間の推定を行ってほしい。下記課題を順に解いていくと
答えにたどり着けるようにしているので、順番に解いてほしい。t.test()を使わずに解ければ加点である(たぶん)。答え合わせはt.test()で
できますよね！？

\begin{enumerate}
  \item stripchart()関数を用いて、C813の遺伝子型をもとにHD93の散布図を作成せよ。(第一回レポート課題の問題とほぼ同じ問題)
  \item stripchart()関数を用いて、R902の遺伝子型をもとにHD93の散布図を作成せよ。(第一回レポート課題の問題とほぼ同じ問題)
  \item DNAマーカーC813における遺伝子型をもとに、HD93のデータを分類し、平均値および不偏分散を求めよ。(第一回レポート課題の問題とほぼ同じ問題)
  \item DNAマーカーR902における遺伝子型をもとに、HD93のデータを分類し、平均値および不偏分散を求めよ。(第一回レポート課題の問題とほぼ同じ問題)
   \item DNAマーカーC813において、遺伝子型Aをもつ系統の標本平均を$\bar{A}_{C813}$、遺伝子型Bをもつ系統の標本平均を$\bar{B}_{C813}$と
   おくと、$\bar{A}_{C813}-\bar{B}_{C813}$の平均および95\%信頼区間を示せ。ただし、今回は等分散性は仮定してよい。$\bar{A}_{C813}$と$\bar{B}_{C813}$は二つ前の問題で導出したものである。  ちなみにベクトルXの要素数を調べる場合はlength(X)である。データ数を数えたい場合ってありますよね.
   \item DNAマーカーC902において、遺伝子型Aをもつ系統の標本平均を$\bar{A}_{R902}$、遺伝子型Bをもつ系統の標本平均を$\bar{B}_{R902}$と
   おくと、$\bar{A}_{R902}-\bar{B}_{R902}$の平均および95\%信頼区間を示せ。ただし等分散性は仮定してよい。$\bar{A}_{R902}$と$\bar{B}_{R902}$は二つ前の問題で導出したものである。
\end{enumerate}

