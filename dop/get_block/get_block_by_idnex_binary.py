def get_block_by_index_binary(a, blocks):
    a = sorted(a, key=lambda x: x['index'])
    counter = 0
    low = 0
    high = len(a) - 1
    while low <= high:
        counter += 1
        mid = (low + high) // 2
        if a[mid]['index'] == blocks:
            return f"Блок: {a[mid]}\nКоличество шагов: {counter}"
        elif blocks > a[mid]['index']:
            low = mid + 1
        else:
            high = mid - 1
    return "Не удалось найти блок"
