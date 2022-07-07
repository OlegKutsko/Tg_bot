import pandas as pd


def prob(file_name):
    desired_columns = pd.read_csv(file_name,
                                  names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
                                  sep=';',
                                  encoding='cp1251')
    num2 = desired_columns.iloc[0:1]
    num3 = num2[['b']]['b'].map(lambda x: x.lstrip('Мини-выписка по карте **** **** **** 6803')).astype(str)
    num4 = num3[:1].astype(str)
    return f'Информация{num4}'


print(prob('report.csv'))
