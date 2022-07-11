import matplotlib.pyplot as plt
from .consts import (PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI)


def create_sum():
    result = sum(PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI)
    return (
        f'Одежда: {CLOTHES} \nПродукты: {PRODUCT} \nТранспорт: {TRANSPORT} \nПродукты для дома: {HOUSE}'
        f'\nМашина: {CAR} \nОплати: {OPLATI} \nИтого расходов: {result}')


def grafic():
    labels = ['Продукты', 'Транспорт', 'Товары для дома', 'Машина', 'Одежда', 'Оплати']    # Вынести в константы можно
    categories = [PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI]
    explode = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]  # Генерить динамически
    plt.pie(categories, labels=labels, explode=explode, autopct='%.0f%%')
    plt.savefig('graphic', dpi=200)

