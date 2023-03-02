# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def list_create(lenght):
    list = []
    for i in range(0, lenght):
        list.append(int(input('Введите чисело: ')))
    print(list)
    return (list)


def list_sort(list):
    size = len(list)
    for index_work in range(0, size - 1):
        index_min = index_work
        for i in range(index_work + 1, size):
            if list[i] < list[index_min]:
                index_min = i
        list[index_work], list[index_min] = list[index_min], list[index_work]


list1_lenght = int(input('Введите кол-во чисел 1 множества: '))
list2_lenght = int(input('Введите кол-во чисел 2 множества: '))

list1 = set(list_create(list1_lenght))
list2 = set(list_create(list2_lenght))

final_list = list(list1.intersection(list2))

print(list_sort(final_list))
