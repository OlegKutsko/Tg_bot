import pandas as pd
import matplotlib.pyplot as plt


def create_sum(file_name):
    global PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI, RESULT
    FIXED_DF = pd.read_csv(file_name, sep=';', encoding='cp1251', skiprows=12)

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

    RESULT = PRODUCT + TRANSPORT + HOUSE + CAR + CLOTHES + OPLATI
    return (
        f'Одежда: {CLOTHES} \nПродукты: {PRODUCT} \nТранспорт: {TRANSPORT} \n'
        f'Продукты для дома: {HOUSE}\nМашина: {CAR} \nОплати: {OPLATI} \nИтого расходов: {RESULT}')


def graph():
    categories = [PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI]
    EXP = 0.01
    EXPLODE = [EXP for i in range(len(categories))]
    LABELS = ['Продукты', 'Транспорт', 'Товары для дома', 'Машина', 'Одежда', 'Оплати']
    plt.pie(categories, labels=LABELS, explode=EXPLODE, autopct='%.0f%%')
    plt.savefig('graph', dpi=200)
