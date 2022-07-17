import sys
import numpy as np
import pandas as pd

def dropouts(data):

    student_list = data
    student_number_list = student_list[['番号']].to_numpy().tolist()
    student_point_list = student_list.drop('番号', axis=1)
    dropout_point = 90
    dropout_count = 2
    dropout_student_list = []
    
    dropout_count_list = (student_point_list <= dropout_point).sum(axis=1).to_numpy().tolist()

    for index, value in enumerate(dropout_count_list):
        if value > dropout_count :
            dropout_student_list.append(student_number_list[index][0])

    print(*dropout_student_list,sep='\n')


def top_vs_bottom(data):

    student_list = data
    student_number_list = student_list[['番号']].to_numpy().tolist()
    student_point_list = student_list.drop('番号', axis=1).to_numpy().tolist()
    max_point_list = []
    min_point_list = []
    
    mean_point_list = np.mean(student_point_list,axis=1)

    max_point = np.max(mean_point_list)
    min_point = np.min(mean_point_list)

    for index, value in enumerate(mean_point_list):
        if value == max_point :
            print(index)
        elif value == min_point :
            print(index)
# メイン関数
# コマンドライン引数: args[1]->ファイル名, args[2]->呼び出す関数
def main():

    args = sys.argv

    if len(args) < 3:
        print("コマンドライン引数には「実行する関数名」と「ファイル名」を指定する必要があります")
        sys.exit()
    elif len(args) > 3:
        print("入力が多すぎます")
        sys.exit()

    try:
        data = pd.read_csv(args[1])
    except FileNotFoundError:
        print('指定されたファイルが存在しません')

    if args[2] == 'dropouts':
        dropouts(data)
    elif args[2] == 'top_vs_bottom':
        top_vs_bottom(data)
    else:
        print('第二引数には「dropouts」か「top_vs_bottom」を指定してください')
        sys.exit()

if __name__ == "__main__":
    main()