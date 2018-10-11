# coding: utf-8

'''
演習課題「おみくじを作ろう」
入力エリアに、おみくじの出目(例：大吉,中吉,吉,凶)が用意してあります。
右のコードエリアに、おみくじプログラムを作ってください。
おみくじは、標準入力から読み込んだ文字列をカンマで分割して、そのうち1つをランダムに出力します。
このとき、カンマで分割したリストをprint関数で出力して、それからおみくじの結果を出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 入力される値
大吉,中吉,吉,凶

 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値
['大吉', '中吉', '吉', '凶']
大吉
'''
# おみくじプログラム

import random
line = input().rstrip()

# 今回は自力で全部書いてみよう！

# カンマで分割して、リストに代入
# リストの要素数を変数に代入
# リストの中身を出力
# ランダムに選んだリストの要素を出力
omikuji = line.split(",")
num = len(omikuji)
print(omikuji)
kekka = random.randrange(num)
print(omikuji[kekka])
