"""
Допустим, у нас есть приложение для магазина одежды.
Среди функций системы есть функция применения специальных скидок в зависимости от типа одежды.

Пример ниже показывает один из способов реализации этого требования.

В примере у нас есть класс DiscountCalculator, который умеет хранить тип одежды.
В нем есть функция, которая рассчитывает скидку в зависимости от типа одежды и возвращает новую стоимость
за вычетом суммы скидки.

"""

from enum import Enum

class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3

class DiscountCalculator:
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discount_price(self):
        if self.product_type == Products.SHIRT:
            return self.cost - self.cost * 0.1
        elif self.product_type == Products.TSHIRT:
            return self.cost - self.cost * 0.15
        elif self.product_type == Products.PANT:
            return self.cost - self.cost * 0.25

dc_shirt = DiscountCalculator(Products.SHIRT, 1000)
print(dc_shirt.get_discount_price())

dc_tshirt = DiscountCalculator(Products.TSHIRT, 1000)
print(dc_tshirt.get_discount_price())

"""
Эта конструкция нарушает принцип открытости/закрытости, поскольку этот класс потребует изменения,
если будет добавляться какой-то тип одежды или если сумма скидки на какую-либо одежду изменится.
"""