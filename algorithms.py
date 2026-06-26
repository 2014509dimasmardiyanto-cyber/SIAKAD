def insertion_sort_nim(data):
    """Mengurutkan NIM dari kecil ke besar (Ascending)"""
    arr = data.copy()
    for i in range(1, len(arr)):
        kunci = arr[i]
        j = i - 1
        while j >= 0 and arr[j]['nim'] > kunci['nim']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = kunci
    return arr

def bubble_sort_ipk(data):
    """Mengurutkan IPK dari besar ke kecil (Descending)"""
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['ipk'] < arr[j + 1]['ipk']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def linear_search_nama(data, keyword):
    """Mencari potongan nama"""
    return [d for d in data if keyword.lower() in d['nama'].lower()]

def binary_search_nim(data, nim_target):
    """Mencari NIM spesifik (Data harus urut)"""
    arr = insertion_sort_nim(data) # Urutkan dulu
    kiri, kanan = 0, len(arr) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah]['nim'] == nim_target:
            return [arr[tengah]]
        elif arr[tengah]['nim'] < nim_target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return []