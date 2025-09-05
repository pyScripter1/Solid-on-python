from enum import Enum
from abc import ABCMeta, abstractmethod

class DiscountCalculator:

  @abstractmethod
  def get_discounted_price(self):
    pass

class DiscountCalculatorShirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculatorTshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())

"""
Как видно из примера выше, теперь у нас есть очень простой базовый класс DiscountCalculator
с одним абстрактным методом get_discounted_price. Мы создали новые классы для одежды,
которые расширяют базовый класс DiscountCalculator. Следовательно, теперь каждый подкласс будет реализовывать
функционал скидок самостоятельно. Сделав так, мы устранили предыдущие ограничения, которые требовали внесения изменений
в базовый класс. Теперь, не изменяя базовый класс, мы можем добавлять больше одежды,
а также изменять размер скидки на отдельный вид одежды по мере необходимости.
"""