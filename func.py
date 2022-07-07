import pandas as pd
import matplotlib.pyplot as plt


def processing_csv_file(file_name):
    fixed_df = pd.read_csv(file_name,
                           sep=';',
                           encoding='cp1251',
                           skiprows=12
                           )
    desired_columns = fixed_df[['Дата операции', 'MCC', 'Сумма в валюте транзакции']]

    products = desired_columns[
        ((desired_columns['MCC'] == 5411) | (desired_columns['MCC'] == 5921) | (desired_columns['MCC'] == 5499))][
        'Сумма в валюте транзакции'].map(lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    transport = desired_columns[desired_columns['MCC'] == 4111]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    house_products = desired_columns[desired_columns['MCC'] == 5399]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    car = desired_columns[desired_columns['MCC'] == 5541]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(
        float).sum()

    clothes = desired_columns[desired_columns['MCC'] == 5651]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(
        float).sum()

    service_oplati = desired_columns[desired_columns['MCC'] == 6012]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    res = products + transport + house_products + car + clothes + service_oplati
    return (
        f'Одежда: {clothes} \nПродукты: {products} \nТранспорт: {transport} \nПродукты для дома: {house_products}'
        f'\nМашина: {car} \nОплати: {service_oplati} \nИтого расходов: {res}')


def grafic(file_name):
    fixed_df = pd.read_csv(file_name,
                           sep=';',
                           encoding='cp1251',
                           skiprows=12
                           )

    desired_columns = fixed_df[['Дата операции', 'MCC', 'Сумма в валюте транзакции']]

    products = desired_columns[
        ((desired_columns['MCC'] == 5411) | (desired_columns['MCC'] == 5921) | (desired_columns['MCC'] == 5499))][
        'Сумма в валюте транзакции'].map(lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    transport = desired_columns[desired_columns['MCC'] == 4111]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    house_products = desired_columns[desired_columns['MCC'] == 5399]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    car = desired_columns[desired_columns['MCC'] == 5541]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(
        float).sum()

    clothes = desired_columns[desired_columns['MCC'] == 5651]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(
        float).sum()

    service_oplati = desired_columns[desired_columns['MCC'] == 6012]['Сумма в валюте транзакции'].map(
        lambda x: x.lstrip('-').rstrip('BYN')).astype(float).sum()

    labels = ['Продукты', 'Транспорт', 'Товары для дома', 'Машина', 'Одежда', 'Оплати']
    lst = [products, transport, house_products, car, clothes, service_oplati]
    explode = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    plt.pie(lst, labels=labels, explode=explode, autopct='%.0f%%')
    plt.savefig('graphic', dpi=200)

