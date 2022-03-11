import sys
import numpy as np
import pandas as pd

# メイン関数
def main():

    args = sys.argv
    # data = pd.read_csv('sample.csv')
    data = pd.read_csv(args[1])
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

if __name__ == "__main__":
    main()