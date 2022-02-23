# 植物育種学研究室 学位論文作成のルール

### テンプレートファイル
最新バージョンは[ここ](https://github.com/qikushu/qikushu.github.io/raw/master/thesis/%E4%BF%AE%E8%AB%96%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%81%8A%E3%82%88%E3%81%B2%E3%82%99%E7%9B%AE%E6%AC%A1.docx)からダウンロードする

### フォント
日本語フォントはMS P明朝、英数字は英文半角フォント(Times New Roman, Centuryなど)を用いる。
図の中のフォントはArial, Calibriなどのゴシック体とする。
修士論文では図表はできるだけ英文にて作成する。

### フォントサイズ
本文、表は10ポイントにて作成する。図のタイトルと脚注のフォントサイズは10ポイントとし、
図内のフォントサイズは見やすさに応じて自由に変更してよい。

### 句点、読点
句読点は以下の四つパターンのいずれかから選択し、統一する。和文の場合はパターン2を推奨する。

| パターン | 句点 | 半角/全角 | 読点 | 半角/全角 |
--- |--- | --- | --- |---
| 1 | 、| 全角 | 。| 全角 |
| 2 |，| 全角 | ．| 全角 |
| 3 | , | 半角 | . | 半角 |

### 構成
基本的には博士論文を手本として構成する。General introductionには一般的背景から問題点、博士論文全体における目的を明確にする。
その目的を達成するための研究を章立て(Chapter)にして構成する。Chapterごとにより具体的な背景や問題点、引用文献等を引用し、研究目的を
明確に論じる。Chapter内のDiscussionでは実験結果に即した一次的な議論を行う。General discussionでは論文全体から得られた結論や
考えを、general introductionと対応させて、論じる。

+ Book cover (表紙)
+ Index (目次)
+ General introduction (一般的背景)
+ (General Materials and Methods) (共通の材料と方法)
+ Chapter 1 XXXXX (第一章)
    + Introduction (背景)
    + Materials and Methods (材料と方法)
    + Results (結果)
    + Discussion (考察)
+ Chapter 2 (第二章)
+ Chapter 3 (第三章)
+ General discussion (総合考察)
+ Acknowledgement (謝辞)
+ References (引用文献)
+ Abstract (摘要)
+ Supplemental Table (付表)
+ Supplemental Figure (付図)

### 背景

#### 引用文献に関する考え方
論文を引用するという行為は、その論文を著者が信頼に足るものだと意思表示していることと等しい。なので、怪しい論文を引用している著者は、その怪しさを見抜くことができない怪しいひとだと判断される。
(論文全体が怪しくても、部分的なデータは信頼する場合は引用することもある。)。また、孫引きをしないように気を付けること。

#### 図表に対する考え方
メインの図表については本論文についてオリジナリティを有するものに原則的には限定するべき。削除しても十分意味が通じるように本文中に必要な情報は文章で提供するべき。どうしても必要ならば、supplemental figureとして(Fig. S1)などのようにして引用する。

コメント：図表はもっとも人の目にふれ、オリジナリティが発揮されるアピールポイントである。他人の業績をメインの図表とするのは誤解を招くので控える。




### 材料と方法 
試薬や機器メーカーについて、初出においては、Manufacturer, Countryを記述する。アメリカの場合はstateも記載する。二回目以降はメーカー名だけでよい。

#### 海外 Manufacturer
Beckman Coulter, Brea, CA, USA

Illumina, San Diego，CA

Merck, Kenilworth, NJ, USA

New England Biolabs, Ipswich, MA, USA

Oxford Nanopore Technologies, Oxford, UK

Qiagen, Venlo, Netherlands

Roche,  Basel,  Switzerland

Thermo Fisher Scientific, Waltham, MA, USA

Promega, Madison, WI, USA

#### 日本国内
Astec, Fukuoka, Japan

### 単位
単位はSI単位系にて表現する。数字と単位の間は半角スペースを一つ入れる。
```
# 例
100 ng/μl
100 mM
```

μは全角を用いず、半角英文フォント(Times new roman, Centuryなど)を用いる。
```
# コピペ用
μ
```

### 度数
百分率(%)は度数であり、無単位である。数字と%の間に空白は入れない
```
# 例
50%
```

温度も度数の一種であるので数字と°Cの間にスペースは入れない。温度はセルシウス温度にて記載し、°Cのように、°とCの半角英字フォント(Times new roman, Centuryなど)にて表現する。 
MSP明朝など日本語フォントでは全角になり正しく表示されないので注意する。
```
# 例、コピペ用
25°C
```

### 統計
統計量は半角フォントのイタリックにする。

