import tkinter as tk
from tkinter import messagebox
import timeit
import random

def counting_sort(arr, count_steps=False):
    if not arr:
        return arr, 0

    langkah = 0

    # Step 1: Find the maximum element in the array
    k = max(arr)

    # Step 2: Initialize the count array
    c = [0] * (k + 1)

    # Step 3: Count the elements in the original array
    for i in range(len(arr)):
        c[arr[i]] += 1
        langkah += 1

    # Step 4: Reconstruct the sorted array
    j = 0
    for i in range(len(c)):
        while c[i] > 0:
            arr[j] = i
            j += 1
            c[i] -= 1
            langkah += 1

    return arr, langkah

def merge_sort(arr, count_steps=False):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_steps = merge_sort(arr[:mid], count_steps)
    right_half, right_steps = merge_sort(arr[mid:], count_steps)

    merged, merge_steps = merge(left_half, right_half)
    total_steps = left_steps + right_steps + merge_steps
    return merged, total_steps

def merge(left, right):
    result = []
    i = j = 0
    langkah = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        langkah += 1

    result.extend(left[i:])
    result.extend(right[j:])
    langkah += len(left) - i + len(right) - j
    return result, langkah

def hibrida_merge_counting_sort(arr, count_steps=False):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    kiri, langkah_kiri = counting_sort(arr[:mid], count_steps)
    kanan, langkah_kanan = counting_sort(arr[mid:], count_steps)

    hasil, langkah_gabung = gabung(kiri, kanan)
    total_steps = langkah_kiri + langkah_kanan + langkah_gabung
    return hasil, total_steps

def gabung(kiri, kanan):
    hasil = []
    i = j = 0
    langkah = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
        langkah += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    langkah += len(kiri) - i + len(kanan) - j
    return hasil, langkah

def buat_array_acak():
    try:
        n = int(entry_jumlah.get())
        arr_acak = [random.randint(0, 1000) for _ in range(n)]
        entry_array.delete(0, tk.END)
        entry_array.insert(0, ','.join(map(str, arr_acak)))
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan jumlah elemen yang valid.")

def urutkan_array():
    try:
        arr = list(map(int, entry_array.get().split(',')))
        
        # Hybrid Merge-Counting Sort
        hibrida_arr = arr.copy()
        waktu_mulai = timeit.default_timer()
        arr_terurut_hibrida, langkah_hibrida = hibrida_merge_counting_sort(hibrida_arr, True)
        waktu_selesai = timeit.default_timer()
        hasil_var_hibrida.set(f"Array Terurut Hibrida: {arr_terurut_hibrida}")
        waktu_var_hibrida.set(f"Kompleksitas Waktu (Hibrida): {waktu_selesai - waktu_mulai:.10f} detik")
        langkah_var_hibrida.set(f"Jumlah Langkah (Hibrida): {langkah_hibrida}")
        
        # Counting Sort
        counting_arr = arr.copy()
        waktu_mulai = timeit.default_timer()
        arr_terurut_counting, langkah_counting = counting_sort(counting_arr, True)
        waktu_selesai = timeit.default_timer()
        hasil_var_counting.set(f"Array Terurut Counting Sort: {arr_terurut_counting}")
        waktu_var_counting.set(f"Kompleksitas Waktu (Counting Sort): {waktu_selesai - waktu_mulai:.10f} detik")
        langkah_var_counting.set(f"Jumlah Langkah (Counting Sort): {langkah_counting}")
        
        # Merge Sort
        merge_arr = arr.copy()
        waktu_mulai = timeit.default_timer()
        arr_terurut_merge, langkah_merge = merge_sort(merge_arr, True)
        waktu_selesai = timeit.default_timer()
        hasil_var_merge.set(f"Array Terurut Merge Sort: {arr_terurut_merge}")
        waktu_var_merge.set(f"Kompleksitas Waktu (Merge Sort): {waktu_selesai - waktu_mulai:.10f} detik")
        langkah_var_merge.set(f"Jumlah Langkah (Merge Sort): {langkah_merge}")

    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan bilangan bulat yang valid dipisahkan oleh koma untuk array.")

def tampilkan_hasil():
    if hasil_var_hibrida.get() and hasil_var_counting.get() and hasil_var_merge.get():
        hasil_tampil_hibrida.set(hasil_var_hibrida.get())
        hasil_tampil_counting.set(hasil_var_counting.get())
        hasil_tampil_merge.set(hasil_var_merge.get())
    else:
        messagebox.showinfo("Informasi", "Lakukan proses pengurutan terlebih dahulu sebelum menampilkan hasil.")

app = tk.Tk()
app.title("Sort Gabungan (Hybrid) Merge-Counting vs Counting Sort vs Merge Sort")

tk.Label(app, text="Masukkan jumlah elemen untuk array acak:").pack(pady=5)
entry_jumlah = tk.Entry(app, width=20)
entry_jumlah.pack(pady=5)

tk.Button(app, text="Buat Array Acak", command=buat_array_acak).pack(pady=5)

tk.Label(app, text="Masukkan array (dipisahkan oleh koma):").pack(pady=5)
entry_array = tk.Entry(app, width=50)
entry_array.pack(pady=5)

tk.Button(app, text="Urutkan", command=urutkan_array).pack(pady=20)

tk.Button(app, text="Tampilkan Hasil", command=tampilkan_hasil).pack(pady=20)

hasil_var_hibrida = tk.StringVar()
hasil_tampil_hibrida = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_hibrida, wraplength=400).pack(pady=5)

waktu_var_hibrida = tk.StringVar()
tk.Label(app, textvariable=waktu_var_hibrida, wraplength=400).pack(pady=5)

langkah_var_hibrida = tk.StringVar()
tk.Label(app, textvariable=langkah_var_hibrida, wraplength=400).pack(pady=5)

hasil_var_counting = tk.StringVar()
hasil_tampil_counting = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_counting, wraplength=400).pack(pady=5)

waktu_var_counting = tk.StringVar()
tk.Label(app, textvariable=waktu_var_counting, wraplength=400).pack(pady=5)

langkah_var_counting = tk.StringVar()
tk.Label(app, textvariable=langkah_var_counting, wraplength=400).pack(pady=5)

hasil_var_merge = tk.StringVar()
hasil_tampil_merge = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_merge, wraplength=400).pack(pady=5)

waktu_var_merge = tk.StringVar()
tk.Label(app, textvariable=waktu_var_merge, wraplength=400).pack(pady=5)

langkah_var_merge = tk.StringVar()
tk.Label(app, textvariable=langkah_var_merge, wraplength=400).pack(pady=5)

app.mainloop()
