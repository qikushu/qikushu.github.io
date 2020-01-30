
## スカラー

数字の代入

    # Assin a value to a valuable
    $a = 1;
    $b = 3;
    # Confirm
    print $a;  # 1
    print $b;  # 3
    
四則計算

    # addition  (+)  和
    $sum = $a + $b;
    print $sum;  # 4
    
    # substraction (-)  差
    $sub = $a - $b;
    print $sub;  # -2
    
    # multiplication  (*)  乗
    $mul = $a * $b;
    print $mul; # 3
    
    # division  (/)  除
    $div = $a / $b;
    print $div;  # 0.333333
    
    # remainder  (%) 余り
    $rem = $a % $b;
    print $rem;  # 1
    
文字列の代入

    $a = "apple";
    $b = "banana";
    print "$a\n";   # apple
    print "$b\n";   # banana
    
文字列の結合はドット

    $c = $a . $b;
    print "$c\n";   # applebanana

## 配列
作成

    @market = ('apple', 'banana','cherry');

要素の追加 (右側から)

    push(@market, "durian");

要素の追加 (左側から)


## ハッシュ


## 制御構文

○ while
○ if
○ if  else
○ if  elsif
○ for
○ foreach


## ファイル入出力

open()
close()

## 正規表現

## サブルーチン





## 二次元行列

行列の例

    my $matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ];
    print ${ ${ $matrix }[0] }[2]; # 30





無名ハッシュとは、リファレンスを用いたハッシュの事

    $person = {name => 'ken', age => 19};

無名ハッシュのデリファレンス（値の取り出し・参照）

    $name = $person -> {name};
    
ハッシュのリファレンスから直接ハッシュの値を呼び出すには
->演算子を用いる

無名ハッシュに関しては、
=>	ハッシュを作る
->	ハッシュを取り出す
というイメージだが…ハッシュのキーを新たに追加する際の操作

%hashとして、$hash{'key'}='val'

$hashとして、$hash->{'key'}='val'


を応用すれば、アロー演算子->で無名ハッシュが作れることになる。
すなわち

    #無名ハッシュをつくって、
    $ref_hash = {"element1" => "A","element2" => "B",};
    # 要素を追加
    $ref_hash->{"element3"} ="C";



## リファレンス

リファレンスの作成 = バックスラッシュをふる。

    my $s = "This is a pen.";
    my @a = ("Apple", "Orange", "Melon");
    my %h = (jp => 'Japan', kr => 'South Korea');
    sub f { print $_[0] }
    
リファレンス作成 リファレンスはスカラー変数

    my $s_ref = \$s;
    my $a_ref = \@a;
    my $h_ref = \%h;
    my $f_ref = \&f;
    
リファレンスからのデリファレンスはサブルーチンは &{ } を使う。

    ${ $s_ref } # $s
    @{ $a_ref } # @a
    %{ $h_ref } # %h
    &{ $f_ref } # &f
    
リファレンスからの配列の要素、ハッシュの要素へのアクセス

    ${ $a_ref }[1]     # "Orange"
    ${ $h_ref }{jp}    # "Japan"
    &{ $f_ref }('hey') # hey とプリント


## 大事な小技

    配列の数値ソート
    my @nums = (5, 11, 3, 2);
    # 数値的な昇順
    @nums = sort {$a <=> $b} @nums;
    # 数値的な降順
    @nums = sort {$b <=> $a} @nums;
    # 文字列的な昇順
    @nums = sort {$a cmp $b} @nums;
    # 文字列的な降順
    @nums = sort {$b cmp $a} @nums;






