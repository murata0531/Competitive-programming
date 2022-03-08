import numpy as np
import pandas as pd
data = pd.read_csv('sample.csv')
# 使用する列を抽出する
x = data[['値']]
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
