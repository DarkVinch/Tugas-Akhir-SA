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

        # Counting Sort
        counting_arr = arr.copy()
        text_widget_counting.delete(1.0, tk.END)  # Hapus output sebelumnya untuk counting sort

        # Start memory tracing
        tracemalloc.start()

        # Start timing
        waktu_mulai = timeit.default_timer()
        arr_terurut_counting = counting_sort(counting_arr, text_widget_counting)
        waktu_selesai = timeit.default_timer()

        # Stop memory tracing
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        hasil_var_counting.set(f"Array Terurut Counting Sort: {arr_terurut_counting}")
        waktu_var_counting.set(f"Kompleksitas Waktu (Counting Sort): {waktu_selesai - waktu_mulai:.10f} detik")
        memori_var_counting.set(f"Penggunaan Memori (Counting Sort): {peak / 1024:.2f} KB")

    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan bilangan bulat yang valid dipisahkan oleh koma untuk array.")

def tampilkan_hasil():
    if hasil_var_counting.get():
        hasil_tampil_counting.set(hasil_var_counting.get())
    else:
        messagebox.showinfo("Informasi", "Lakukan proses pengurutan terlebih dahulu sebelum menampilkan hasil.")

app = tk.Tk()
app.title("Counting Sort")

tk.Label(app, text="Masukkan jumlah elemen untuk array acak:").pack(pady=5)
entry_jumlah = tk.Entry(app, width=20)
entry_jumlah.pack(pady=5)

tk.Button(app, text="Buat Array Acak", command=buat_array_acak).pack(pady=5)

tk.Label(app, text="Masukkan array (dipisahkan oleh koma):").pack(pady=5)
entry_array = tk.Entry(app, width=50)
entry_array.pack(pady=5)

tk.Button(app, text="Urutkan", command=urutkan_array).pack(pady=20)

tk.Button(app, text="Tampilkan Hasil", command=tampilkan_hasil).pack(pady=20)

hasil_var_counting = tk.StringVar()
hasil_tampil_counting = tk.StringVar()
tk.Label(app, textvariable=hasil_tampil_counting, wraplength=400).pack(pady=5)

waktu_var_counting = tk.StringVar()
tk.Label(app, textvariable=waktu_var_counting, wraplength=400).pack(pady=5)

memori_var_counting = tk.StringVar()
tk.Label(app, textvariable=memori_var_counting, wraplength=400).pack(pady=5)

tk.Label(app, text="Langkah-langkah Counting Sort:", wraplength=400).pack(pady=5)
text_widget_counting = tk.Text(app, wrap=tk.WORD, height=10, width=50)
text_widget_counting.pack(pady=5)

app.mainloop()
