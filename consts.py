import pandas as pd


def get_file(file_name: any) -> any:
    return file_name


FIXED_DF = pd.read_csv(get_file(), sep=';', encoding='cp1251', skiprows=12)
desired_columns = FIXED_DF[['Дата операции', 'MCC', 'Сумма в валюте транзакции']]

PRODUCT = desired_columns[
    ((desired_columns['MCC'] == 5411) | (desired_columns['MCC'] == 5921) | (desired_columns['MCC'] == 5499))][
    'Сумма в валюте транзакции'].map(lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

TRANSPORT = desired_columns[desired_columns['MCC'] == 4111]['Сумма в валюте транзакции'].map(
    lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

HOUSE = desired_columns[desired_columns['MCC'] == 5399]['Сумма в валюте транзакции'].map(
    lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

CAR = desired_columns[desired_columns['MCC'] == 5541]['Сумма в валюте транзакции'].map(
    lambda x: x.lstrip('-').rstrip('BYN')).astype(
    float).sum()

CLOTHES = desired_columns[desired_columns['MCC'] == 5651]['Сумма в валюте транзакции'].map(
    lambda x: x.lstrip('-').rstrip('BYN')).astype(
    float).sum()

OPLATI = desired_columns[desired_columns['MCC'] == 6012]['Сумма в валюте транзакции'].map(
    lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()
