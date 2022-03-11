import sys
import numpy as np
import pandas as pd

# 最大値をもつ都道府県を出力する関数
def get_max_prefecture(data):

    # 使用する列を抽出する
    x = data[['値1']]
    # リストに変換
    x = x.to_numpy().tolist()
    # 表示して確認する
    print(x)
    # 合計
    print(np.sum(x))
    # 平均
    print(np.mean(x))
    # 最大値を取得
    print(np.max(x))
    # 最大値のインデックスを取得して都道府県名を取得
    argmax = np.argmax(x)
    prefecture = data[['都道府県']].to_numpy().tolist()
    print(prefecture[argmax])

# 行方向の集計を行う関数
def get_row_aggregate(data):

    # 使用する列を抽出する
    x = data[['値1','値2']]
    # リストに変換
    x = x.to_numpy().tolist()
    # 表示して確認する
    print(x)
    # 行ごとの合計
    row_sum = np.sum(x,axis=1)
    print(row_sum)
    # 行ごとの平均
    row_mean = np.mean(x,axis=1)
    print(row_mean)

# メイン関数
def main():

    args = sys.argv
    # data = pd.read_csv('sample.csv')
    data = pd.read_csv(args[1])
    # 最大値をもつ都道府県を出力する関数を呼び出す
    get_max_prefecture(data)
    # 行方向の集計を行う関数を呼び出す
    get_row_aggregate(data)

if __name__ == "__main__":
    main()