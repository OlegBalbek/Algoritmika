import os, json
files = []
l = []
files += os.listdir('transactions')
for i in files:
    f = open(f"{'transactions'}/{i}")
    l.append(json.loads(f.read()))
a = l.copy()

def first_task():
    print("ПЕРВОЕ ЗАДАНИЕ")
    from get_block.get_block_by_index_linear import get_block_by_index_linear
    from get_block.get_block_by_idnex_binary import get_block_by_index_binary
    first = a[0]  # Искомый элемент находится в начале
    end = a[-1]  # Искомый элемент находится в конце
    mid = a[len(a) // 2]  # Искомый элемент находится в центре
    dvad = a[len(a) - 20]  # Искомый элемент находится на 20 месте с конца
    temp = [first, end, mid, dvad]

    print("ЛИНЕЙНЫЙ ПОИСК:")
    for i in temp:
        print(f"Линейный поиск индекса №{i['index']}: ", get_block_by_index_linear(a, i['index']), sep="\n", end="\n")

    print("-" * 100)

    print("ЛИНЕЙНЫЙ ПОИСК С ОТСОРТИРОВАННЫМ МАССИВОМ:")
    for i in temp:
        print(f"Линейный поиск индекса №{i['index']}: ", get_block_by_index_linear(sorted(a, key=lambda x: x['index']), i['index']), sep="\n", end="\n")

    print("-" * 100)

    print("БИНАРНЫЙ ПОИСК:")
    for i in temp:
        print(f"Бинарный поиск индекса №{i['index']}: ", get_block_by_index_binary(a, i['index']), sep="\n", end="\n")

def second_task():
    print("\nВТОРОЕ ЗАДАНИЕ")
    from sort.bubble_sort import bubble_sort
    from sort.selection_sort import selection_sort
    print(f"НЕОТСОРТИРОВАННЫЙ МАССИВ:\n{a}")
    print(f"СОРТИРОВКА ПУЗЫРЬКОМ:\n{bubble_sort(a)}")
    print(f"СОРТИРОВКА ОТБОРОМ:\n{selection_sort(a)}")


def third_task():
    print("\nТРЕТЬЕ ЗАДАНИЕ")
    from datetime import datetime, date
    count_of_transactions = 0
    ct = 0
    third = sorted(a, key=lambda x: x['index'])
    miners = dict()

    for i in third:
        count_of_transactions += len(i['transactions'])
        ct += len(list(filter(lambda x: x['from'] != "SYSTEM" and i['index'] != 0, i['transactions'])))
        print(f"Номер блока: {i['index']}. Количество транзакций (с учётом SYSTEM): {len(i['transactions'])}")
    print(f"Общее количество транзакций: {count_of_transactions} (с учётом SYSTEM); {ct} (без учёта SYSTEM)\n")

    list_of_values = []
    list_of_transactions = []

    for i in third: # Суммарное количество вознаграждений
        if i["index"] == 0:
            continue
        list_of_values.append(i["transactions"][-1]["value"])
        if i['transactions'][-1]['to'] not in miners:
            miners[i['transactions'][-1]['to']] = 0 # Добавление майнера в словарь
        miners[i['transactions'][-1]['to']] += i['transactions'][-1]['value'] # Добавление награжденй
    miners = sorted(miners.items(), key=lambda x: x[1])
    list_of_values = sorted(list_of_values)

    print(f"Самое низкое (суммарное) вознаграждение (у майнера): {miners[0]}\nСамое высокое (суммарное) вознаграждение (у майнера): {miners[-1]}\n")
    print(f"Самое низкое вознаграждение (в целом): {list_of_values[0]}\nСамое высокое вознаграждение (в целом): {list_of_values[-1]}\n")

    for i in third:
        if i["index"] == 0:
            continue
        for j in i["transactions"]:
            if j['from'] == "SYSTEM":
                continue
            list_of_transactions.append(j["value"])
    print(f"Среднее значение перевода в транзакциях (награждения не учитываются): {sum(list_of_transactions)/len(list_of_transactions)}")

    minutes = {}

    for i in third:
        minute = datetime.fromtimestamp(i['timestamp']).minute
        if minute not in minutes:
            minutes[minute] = 0
        else:
            minutes[minute] += 1

    print("\nМИНУТЫ:")
    for key, val in minutes.items():
        print(f"{key} м.: {val} зн.")

first_task()
second_task()
third_task()