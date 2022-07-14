import matplotlib.pyplot as plt
from consts import (PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI, EXP, LABELS)


def create_sum():
    result = PRODUCT+TRANSPORT+HOUSE+CAR+CLOTHES+OPLATI
    return (
        f'Одежда: {CLOTHES} \nПродукты: {PRODUCT} \nТранспорт: {TRANSPORT} \n'
        f'Продукты для дома: {HOUSE}\nМашина: {CAR} \nОплати: {OPLATI} \nИтого расходов: {result}')


def grafic():
    categories = [PRODUCT, TRANSPORT, HOUSE, CAR, CLOTHES, OPLATI]
    explode = [EXP for i in range(len(categories))]
    plt.pie(categories, labels=LABELS, explode=explode, autopct='%.0f%%')
    plt.savefig('graphic', dpi=200)

print(create_sum())