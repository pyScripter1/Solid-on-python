"""
Все можно исправить, следуя принципу разделения интерфейсов, как в примере ниже.
Вместо создания большого интерфейса мы создаем более маленькие ролевые интерфейсы для каждого метода.
Соответствующие классы будут использовать только связанные интерфейсы.
"""

from abc import ABCMeta, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
Smaller role interfaces are created for each feature and the classes would only extend the required interfaces and implement the
relevant methods
'''

class CallingDevice:
  @abstractmethod
  def make_calls(self):
    pass

class MessagingDevice:
  @abstractmethod
  def send_sms(self):
    pass

class InternetbrowsingDevice:
  @abstractmethod
  def browse_internet(self):
    pass

class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
  def make_calls(self):
    #implementation
    pass

  def send_sms(self):
    #implementation
    pass

  def browse_internet(self):
    #implementation
    pass

class LandlinePhone(CallingDevice):
  def make_calls(self):
    #implementation
    pass