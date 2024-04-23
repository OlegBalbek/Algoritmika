import os, json
import datetime
files = []
l = []
files += os.listdir('transactions')
for i in files:
    f = open(f"{'transactions'}/{i}")
    l.append(json.loads(f.read()))
a = l.copy()

def third_task():
    print("Агрегатные вычисления")

    # Подсчет количества транзакций в каждом блоке и общего количества транзакций
    count_of_transactions = 0
    bolt = 0
    three = sorted(a, key=lambda x: x['index'])
    miners = dict()

    for i in three:
        count_of_transactions += len(i['transactions'])
        bolt += len(list(filter(lambda x: x['from'] != "SYSTEM" and i['index'] != 0, i['transactions'])))
        print(f"Номер блока: {i['index']}. Количество транзакций (с учётом SYSTEM): {len(i['transactions'])}")
    print(f"Общее количество транзакций: {count_of_transactions} (с учётом SYSTEM); {bolt} (без учёта SYSTEM)\n")

    # Нахождение самого низкого и самого высокого суммарного вознаграждения у майнеров
    list_of_values = []
    list_of_transactions = []

    for i in three:
        if i["index"] == 0:
            continue
        list_of_values.append(i["transactions"][-1]["value"])
        if i['transactions'][-1]['to'] not in miners:
            miners[i['transactions'][-1]['to']] = 0
        miners[i['transactions'][-1]['to']] += i['transactions'][-1]['value']
    miners = sorted(miners.items(), key=lambda x: x[1])
    list_of_values = sorted(list_of_values)

    print(f"Самое низкое (суммарное) вознаграждение (у майнера): {miners[0]}\nСамое высокое (суммарное) вознаграждение (у майнера): {miners[-1]}\n")
    print(f"Самое низкое вознаграждение (в целом): {list_of_values[0]}\nСамое высокое вознаграждение (в целом): {list_of_values[-1]}\n")

    # Подсчет среднего значения перевода в транзакциях (без учета награждений)
    for i in three:
        if i["index"] == 0:
            continue
        for j in i["transactions"]:
            if j['from'] == "SYSTEM":
                continue
            list_of_transactions.append(j["value"])
    print(f"Среднее значение перевода в транзакциях (награждения не учитываются): {sum(list_of_transactions)/len(list_of_transactions)}")

    # Подсчет количества транзакций в каждую минуту
    minutes = {}

    for i in three:
        minute = datetime.fromtimestamp(i['timestamp']).minute
        if minute not in minutes:
            minutes[minute] = 0
        else:
            minutes[minute] += 1

    print("\nМинуты:")
    for key, val in minutes.items():
        print(f"{key} м.: {val} зн.")

third_task()