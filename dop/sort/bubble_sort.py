def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):  # Потому что последний элемент - наибольший
            if arr[j]['index'] > arr[j+1]['index']:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Смещаем наибольшие элементы вправо
    return arr
