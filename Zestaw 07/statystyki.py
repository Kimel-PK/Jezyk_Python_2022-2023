# uruchamia wszystkie algorytmy sortowania na wszystkich przypadkach tablic
# wyniki zapisuje do pliku statystyki.txt

import time
from mtablica import MonitorowanaTablica

from bubble_sort import bubble_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from tim_sort import tim_sort

N = 50  # liczba elementów, można zmieniać

# zbiór algorytmów i typów tablic
tablice = ["R", "S", "A", "T"]
sortowanie = [
    ["Bubble sort", bubble_sort],
    ["Shell sort", shell_sort],
    ["Merge sort", merge_sort],
    ["Quick sort", quick_sort],
    ["Tim sort", tim_sort]
]

f = open("statystyki.txt", "w")

for sortuj in sortowanie :
    
    f.write(f"{sortuj[0]}\n")
    for typ in tablice :
        tablica = MonitorowanaTablica(0, 1000, N, typ)
        
        t0 = time.perf_counter()
        sortuj[1](tablica)
        delta_t = time.perf_counter() - t0
        
        f.write(f"{typ}: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.\n")
    f.write ("\n")

f.close()