import tkinter as tk
from tkinter import messagebox
import timeit
import random

def counting_sort(arr, text_widget=None):
    if not arr:
        return arr

    # Step 1: Find the maximum element in the array
    k = max(arr)

    # Step 2: Initialize the count array
    c = [0] * (k + 1)

    # Step 3: Count the elements in the original array
    for i in range(len(arr)):
        c[arr[i]] += 1

    if text_widget:
        text_widget.insert(tk.END, f"Counting array: {c}\n")

    # Step 4: Reconstruct the sorted array
    j = 0
    for i in range(len(c)):
        while c[i] > 0:
            arr[j] = i
            j += 1
            c[i] -= 1

    if text_widget:
        text_widget.insert(tk.END, f"Sorted output (Counting Sort): {arr}\n")

    return arr

def merge_sort(arr, text_widget=None):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], text_widget)
    right_half = merge_sort(arr[mid:], text_widget)

    merged = merge(left_half, right_half, text_widget)
    return merged

def merge(left, right, text_widget=None):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    if text_widget:
        text_widget.insert(tk.END, f"Merged array: {result}\n")
    
    return result

def hibrida_merge_counting_sort(arr, text_widget=None):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Memasukkan pesan ketika menggunakan counting sort pada bagian kiri
    if text_widget:
        text_widget.insert(tk.END, f"Penggunaan Counting Sort (Kiri): {arr[:mid]}\n")

    kiri = counting_sort(arr[:mid], text_widget)

    # Memasukkan pesan ketika menggunakan counting sort pada bagian kanan
    if text_widget:
        text_widget.insert(tk.END, f"Penggunaan Counting Sort (Kanan): {arr[mid:]}\n")

    kanan = counting_sort(arr[mid:], text_widget)

    # Memasukkan pesan ketika memulai proses penggabungan
    if text_widget:
        text_widget.insert(tk.END, f"Proses Penggabungan: Kiri - {kiri}, Kanan - {kanan}\n")

    hasil = gabung(kiri, kanan, text_widget)
    return hasil

def gabung(kiri, kanan, text_widget=None):
    hasil = []
    i = j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    if text_widget:
        text_widget.insert(tk.END, f"Langkah-langkah Gabung: {hasil}\n")
    return hasil

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
        text_widget_hibrida.delete(1.0, tk.END)  # Hapus output sebelumnya untuk hybrid
        waktu_mulai = timeit.default_timer()
        arr_terurut_hibrida = hibrida_merge_counting_sort(hibrida_arr, text_widget_hibrida)
        waktu_selesai = timeit.default_timer()
        hasil_var_hibrida.set(f"Array Terurut Hibrida: {arr_terurut_hibrida}")
        waktu_var_hibrida.set(f"Kompleksitas Waktu (Hibrida): {waktu_selesai - waktu_mulai:.10f} detik")
        
        # Counting Sort
        counting_arr = arr.copy()
        text_widget_counting.delete(1.0, tk.END)  # Hapus output sebelumnya untuk counting sort
        waktu_mulai = timeit.default_timer()
        arr_terurut_counting = counting_sort(counting_arr, text_widget_counting)
        waktu_selesai = timeit.default_timer()
        hasil_var_counting.set(f"Array Terurut Counting Sort: {arr_terurut_counting}")
        waktu_var_counting.set(f"Kompleksitas Waktu (Counting Sort): {waktu_selesai - waktu_mulai:.10f} detik")
        
        # Merge Sort
        merge_arr = arr.copy()
        text_widget_merge.delete(1.0, tk.END)  # Hapus output sebelumnya untuk merge sort
        waktu_mulai = timeit.default_timer()
        arr_terurut_merge = merge_sort(merge_arr, text_widget_merge)
        waktu_selesai = timeit.default_timer()
        hasil_var_merge.set(f"Array Terurut Merge Sort: {arr_terurut_merge}")
        waktu_var_merge.set(f"Kompleksitas Waktu (Merge Sort): {waktu_selesai - waktu_mulai:.10f} detik")

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

tk.Label(app, text="Langkah-langkah Sort Gabungan (Hybrid) Merge-Counting:", wraplength=300).pack(pady=5)
text_widget_hibrida = tk.Text(app, wrap=tk.WORD, height=5, width=50)
text_widget_hibrida.pack(pady=5)

hasil_var_counting = tk.StringVar()
hasil_tampil_counting = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_counting, wraplength=400).pack(pady=5)

waktu_var_counting = tk.StringVar()
tk.Label(app, textvariable=waktu_var_counting, wraplength=400).pack(pady=5)

tk.Label(app, text="Langkah-langkah Counting Sort:", wraplength=400).pack(pady=5)
text_widget_counting = tk.Text(app, wrap=tk.WORD, height=5, width=50)
text_widget_counting.pack(pady=5)

hasil_var_merge = tk.StringVar()
hasil_tampil_merge = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_merge, wraplength=400).pack(pady=5)

waktu_var_merge = tk.StringVar()
tk.Label(app, textvariable=waktu_var_merge, wraplength=400).pack(pady=5)

tk.Label(app, text="Langkah-langkah Merge Sort:", wraplength=400).pack(pady=5)
text_widget_merge = tk.Text(app, wrap=tk.WORD, height=5, width=50)
text_widget_merge.pack(pady=5)

app.mainloop()
