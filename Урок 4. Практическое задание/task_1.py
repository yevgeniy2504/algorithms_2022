"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
<<<<<<< HEAD


def func_2(nums):
    new_arr = []
    if nums[0] % 2 == 0:
        new_arr.append(0)
    if nums[1] % 2 == 0:
        new_arr.append(1)
    if nums[2] % 2 == 0:
        new_arr.append(2)
    if nums[3] % 2 == 0:
        new_arr.append(3)

    return new_arr


def func_3(nums):
    new_arr = []
    for i in range(4):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_4(nums):
    new_arr = []
    i = 0
    while i < 4:
        if nums[i] % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr


def func_5(nums):
    new_arr = []
    for i in range(len(nums)):
        new_arr.append(i) if nums[i] % 2 == 0 else True
    return new_arr


print(timeit("func_1([1, 2, 3, 4])", globals=globals()))
print(timeit("func_2([1, 2, 3, 4])", globals=globals()))
print(timeit("func_3([1, 2, 3, 4])", globals=globals()))
print(timeit("func_4([1, 2, 3, 4])", globals=globals()))
print(timeit("func_5([1, 2, 3, 4])", globals=globals()))
=======
>>>>>>> Lesson-4
