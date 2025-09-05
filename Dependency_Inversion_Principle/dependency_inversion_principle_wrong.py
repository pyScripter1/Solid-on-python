# Принцип инверсии зависимостей
# а). Модуль высокого уровня не должен зависеть от модулей низкого уровня. Оба должны зависеть от абстракций.
# б). Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
'''
Мы напрямую используем team_student_memberships.team_memberships в нашем классе высокого уровня Analysis и используем реализацию
этого списка непосредственно в классе высокого уровня. Сейчас это нормально, но представьте ситуацию, когда нам нужно изменить эту
реализацию со списка на что-то другое. В этом случае наш класс высокого уровня Analysis сломается, поскольку он зависит от
деталей реализации класса низкого уровня TeamMemberships.
'''

"""
Как показано в коде ниже, у нас есть класс Student, который мы используем для создания экземпляров Student
и класса TeamMemberships, который содержатся сведения о принадлежности учеников к разным командам.

Теперь мы определим высокоуровневый класс Analysis, где нам нужно отсеять всех учеников, принадлежащих красной команде.
"""


from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3

class Student:
  def __init__(self, name):
    self.name = name

class TeamMemberships:
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

class Analysis:
  def __init__(self, team_student_memberships):
    memberships = team_student_memberships.team_memberships
    for members in memberships:
      if members[1] == Teams.RED_TEAM:
        print(f'{members[0].name} is in RED team')

student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)

"""
Как видно из реализации, мы напрямую используем team_student_memberships.team_memberships в высокоуровневом классе Analysis,
и мы используем реализацию этого списка непосредственно в классе высокого уровня. На данный момент все нормально,
но представьте ситуацию, в которой нам нужно изменить эту реализацию со списка на что-то другое.
В этом случае наш класс высокого уровня Analysis сломается, поскольку он зависит от деталей реализации TeamMemberships
низкого уровня.
"""