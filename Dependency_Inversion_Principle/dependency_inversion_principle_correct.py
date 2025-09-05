# Принцип инверсии зависимостей
# а). Высокоуровневый модуль не должен зависеть от низкоуровневых модулей. Оба должны зависеть от абстракций.
# б). Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций from enum import Enum
'''
Чтобы соответствовать принципу инверсии зависимостей, нам необходимо гарантировать, что высокоуровневый класс Anslysis не зависит от конкретной
реализации низкоуровневого класса TeamMemberships. Вместо этого он должен зависеть от какой-либо абстракции.
Итак, мы создаём интерфейс TeamMembershipLookup, содержащий абстрактный метод find_all_students_of_team, который передаётся любому
классу, наследующему от этого интерфейса. Мы делаем наш класс TeamMembership наследуемым от этого интерфейса, и, следовательно, теперь класс TeamMembership
должен предоставлять реализацию функции find_all_students_of_team. Эта функция затем возвращает результаты любой
другой вызывающей сущности. Мы перенесли обработку, выполнявшуюся в высокоуровневом классе Analysis, в класс TeamMemberships через
интерфейс TeamMembershipLookup.
Таким образом, мы устранили зависимость высокоуровневого класса Analysis от низкоуровневого класса TeamMemberships и перенесли эту
зависимость в интерфейс TeamMembershipLookup. Теперь высокоуровневый класс не зависит от деталей реализации низкоуровневого класса.
Любые изменения в деталях реализации низкоуровневого класса не влияют на высокоуровневый класс.
'''

"""
Теперь взгляните на пример ниже,
в котором мы меняем эту реализацию и приводим ее в соответствие с принципом инверсии зависимостей.
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3

class TeamMembershipLookup():
  @abstractmethod
  def find_all_students_of_team(self, team):
    pass

class Student:
  def __init__(self, name):
    self.name = name

class TeamMemberships(TeamMembershipLookup):
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

  def find_all_students_of_team(self, team):
    for members in self.team_memberships:
      if members[1] == team:
        yield members[0].name

class Analysis():
  def __init__(self, team_membership_lookup):
    for student in team_membership_lookup.find_all_students_of_team(Teams.RED_TEAM):
      print(f'{student} is in RED team.')

student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)

"""
Чтобы следовать принципу инверсии зависимостей, нам необходимо убедиться,
что класс высокого уровня Analysis не зависит от конкретной реализации класса низкого уровня TeamMembership.
Вместо этого он должен зависеть от некоторой абстракции.

Итак, мы создаем интерфейс TeamMembershipLookup, который содержит абстрактный метод find_all_students_of_team,
передающийся любому классу, наследующему этот интерфейс. Мы наследуем наш класс TeamMembership от этого интерфейса,
следовательно, теперь класс TeamMembership должен предоставлять реализацию функции find_all_students_of_team.
Затем эта функция передает результаты любому другому вызывающему ее объекту.
Мы перенесли обработку, которая делалась в классе высокого уровня Analysis в TeamMemberships через интерфейс
TeamMembershipLookup.

Сделав все это, мы убрали зависимость класса Analysis от класса TeamMemberships и перенесли ее в интерфейс
TeamMembershipLookup. Теперь класс высокого уровня не зависит от деталей реализации класса низкого уровня.
Любые изменения в деталях реализации класса низкого уровня не влияют на класс высокого уровня.
"""