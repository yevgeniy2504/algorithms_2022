"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict


companies = defaultdict(int)
n = int(input("Количество компаний: "))
for i in range(n):
    s = 0
    comp_name = input("Название компании: ")
    for k in range(4):
        temp_s = int(input(f"Введите сумму за {k + 1}-й квартал: "))
        s = s + temp_s
    companies[comp_name] = s

avr = sum(companies.values()) / len(companies)

print(f'Среднегодовая прибыль - {avr} руб.')
print('Выше среднего---:')
for key, val in companies.items():
    if val > avr:
        print(f'Компания {key} - {val} руб:')
print('---Ниже среднего:')
for key, val in companies.items():
    if val < avr:
        print(f'Компания {key} - {val} руб:')














