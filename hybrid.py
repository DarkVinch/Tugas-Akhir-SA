import tkinter as tk
from tkinter import messagebox
import timeit
import random
import tracemalloc

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

        # Start memory tracing
        tracemalloc.start()

        # Start timing
        waktu_mulai = timeit.default_timer()
        arr_terurut_hibrida = hibrida_merge_counting_sort(hibrida_arr, text_widget_hibrida)
        waktu_selesai = timeit.default_timer()

        # Stop memory tracing
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        hasil_var_hibrida.set(f"Array Terurut Hibrida: {arr_terurut_hibrida}")
        waktu_var_hibrida.set(f"Kompleksitas Waktu (Hibrida): {waktu_selesai - waktu_mulai:.10f} detik")
        memori_var_hibrida.set(f"Penggunaan Memori (Hibrida): {peak / 1024:.2f} KB")

    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan bilangan bulat yang valid dipisahkan oleh koma untuk array.")

def tampilkan_hasil():
    if hasil_var_hibrida.get():
        hasil_tampil_hibrida.set(hasil_var_hibrida.get())
    else:
        messagebox.showinfo("Informasi", "Lakukan proses pengurutan terlebih dahulu sebelum menampilkan hasil.")

app = tk.Tk()
app.title("Sort Gabungan (Hybrid) Merge-Counting")

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

memori_var_hibrida = tk.StringVar()
tk.Label(app, textvariable=memori_var_hibrida, wraplength=400).pack(pady=5)

tk.Label(app, text="Langkah-langkah Sort Gabungan (Hybrid) Merge-Counting:", wraplength=300).pack(pady=5)
text_widget_hibrida = tk.Text(app, wrap=tk.WORD, height=10, width=50)
text_widget_hibrida.pack(pady=5)

app.mainloop()
