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

    # 値1,値2の平均値が一番大きい都道府県を取得

# メイン関数
# コマンドライン引数: args[1]->ファイル名, args[2]->呼び出す関数
def main():

    args = sys.argv

    # コマンドライン引数に与える項目が少ないと各項目の入力を促す
    # コマンドライン引数に与える項目が多いとエラー
    if len(args) < 3:
        print("コマンドライン引数には「実行する関数名」と「ファイル名」を指定する必要があります")
        sys.exit()
    elif len(args) > 3:
        print("入力が多すぎます")
        sys.exit()

    try:
        # data = pd.read_csv('sample.csv')
        data = pd.read_csv(args[1])

        if args[2] == 'max':
            # 最大値をもつ都道府県を出力する関数を呼び出す
            get_max_prefecture(data)
        elif args[2] == 'aggregate':
            # 行方向の集計を行う関数を呼び出す
            get_row_aggregate(data)
        else:
            print('第二引数には「max」か「aggregate」を指定してください')
            sys.exit()

    except FileNotFoundError:
        print('指定されたファイルが存在しません')

if __name__ == "__main__":
    main()