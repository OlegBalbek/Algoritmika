def get_block_by_index_linear(a, blocks):
    counter = 0
    for i in a:
        counter += 1
        if i['index'] == blocks:
            return f"Блок: {i}\nКоличество шагов: {counter}"
            break
    return "Не удалось найти блок"
