# Ни один клиент не должен зависеть от методов, которые он не использует.
'''
Более широкий интерфейс, связанный со всеми методами, обязывает все классы предоставлять реализацию всех методов, даже если
некоторые методы для них не важны.
'''

"""
Допустим, мы разрабатываем приложение для различных коммуникационных устройств.
Мы говорим, что устройство связи – это устройство, которое будет иметь одну или несколько из следующих функций:
совершать звонки, отправлять SMS или искать в Интернете. Итак, мы создаем интерфейс с именем
CommunicationDevice и добавляем соответствующие абстрактные методы для каждой из этих функций,
чтобы любой создаваемый класс смог реализовать эти методы.

Затем мы создаем класс SmartPhone с помощью интерфейса CommunicationDevice и реализуем функционал абстрактных методов.
До сих пор все было в порядке.

Теперь предположим, что нам нужно создать стационарный телефон.
Он тоже является устройством связи, поэтому мы создаем новый класс LandlinePhone через тот же интерфейс
CommunicationDevice. Именно здесь мы сталкиваемся с проблемой из-за объемного интерфейса CommunicationDevice.
В классе LandlinePhone мы реализовываем метод make_calls(), но поскольку мы также наследуем абстрактные методы
send_sms() и browse_internet(), мы должны предоставить реализацию и этих двух абстрактных методов в классе
LandlinePhone, даже если они в принципе неприменимы к этому виду телефонов.
Мы можем либо создать исключение, либо оставить pass вместо реализации, но нам все равно нужно ее предоставить.
"""

from abc import ABCMeta, abstractmethod


class CommunicationDevice:
  @abstractmethod
  def make_calls(self):
    pass

  @abstractmethod
  def send_sms(self):
    pass

  @abstractmethod
  def browse_internet(self):
    pass

class SmartPhone(CommunicationDevice):
  def make_calls(self):
    #implementation
    pass

  def send_sms(self):
    #implementation
    pass

  def browse_internet(self):
    #implementation
    pass

class LandlinePhone(CommunicationDevice):
    def make_calls(self):
      #implementation
      pass

    def send_sms(self):
      #just pass or raise exception as this feature is not supported
      pass

    def browse_internet(self):
      #just pass or raise exception as this feature is not supported
      pass