def selection_sort(arr):
    for i in range(len(arr)):
        m_i = i # Минимальный элемент
        for j in range(i+1, len(arr)):
            if arr[j]['index'] < arr[m_i]['index']: # Если меньше "минимального" элемента
                m_i = j # Минимальный элемент
        arr[i], arr[m_i] = arr[m_i], arr[i]  # Минимальный элемент встаёт в начало
    return arr
