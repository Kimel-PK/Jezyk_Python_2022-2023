# Zestaw 7

## Opis

Celem zestawu jest studium różnych algorytmów sortowania. Sortowanie to ważna część algorytmiki, zapewne powtarzana wiele razy na różnych przedmiotach, ale warto spróbować również w Pythonie. Materiał będzie prawdopodobnie omówiony na wykładzie, jest również mnóstwo informacji w sieci. Bardzo zachęcam, aby nie kopiować znalezionych rozwiązań (cudzego gotowego kodu), tylko poświęcić czas na zrozumienie strategii poszczególnych algorytmów oraz je zapisać.

Aby uatrakcyjnić analizę działania poszczególnych algorytmów, przygotowałem (na bazie kodu znalezionego w jednym z "samouczków") uproszczoną, acz efektowną wersję kodu, który tworzy wejściową tablicę z wartościami do posortowania oraz wykonuje animowaną wizualizację procesu sortowania w postaci zmieniającego się dynamicznie histogramu. Użyte są tu biblioteki `numpy` oraz `matplotlib`, do wykonania animacji użyta zostanie funkcja `FuncAnimation`.

Obliczenia numeryczne i wizualizacje w Pythonie często oparte są na kanonie bibliotek:

- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)

Jeżeli nie mamy ich zainstalowanych, możemy zainstalować je po kolei za pomocą:

```console
pip install <nazwa>
```

Dodatkowo zainstalowane będą wtedy wymagane pakiety zależne. W tym dokumencie zamieszczam tylko nieco komentarzy pomocnych do zrozumienia proponowanego kodu.

Podstawową zaletą biblioteki `NumPy` jest zaimplementowany w niej typ tablicy `ndarray`. Do naszych celów (sortowania) potrzebna będzie tablica jednowymiarowa, o jednorodnym rozkładzie indeksów oraz różnej liczbie wartości, rozłożonych losowo lub według jakiegoś uporządkowania. Po zaimportowaniu modułu, do stworzenia tablicy używamy funkcji `linspace`, podając zakres od-do:

![1](https://user-images.githubusercontent.com/57668948/208065680-fed5b2b0-8bf0-456e-918c-e478a2f7d698.png)

W ten sposób powstał obiekt tablicy `ndarray`, a domyślna liczba podziałów wynosi `50` i można ją określić jako trzeci parametr (pozycyjny, lub nazwany `num`):

![2](https://user-images.githubusercontent.com/57668948/208065704-6f8fc493-0ece-43ae-8a54-647b1ada9964.png)

Za pomocą parametru `dtype` można określić typ generowanych elementów, warto pamiętać, że `NumPy` używa swoje własne typy, na przykład `float64` lub `int64`. Powyższy przykład możemy zapisać:

![3](https://user-images.githubusercontent.com/57668948/208065727-11727e82-299f-482d-820b-12e736e1406e.png)

Odwrotną kolejność uzyskami zamieniając pierwsze dwa argumenty (można je podawać również jako argumenty nazwane, `start`, `stop`):

![4](https://user-images.githubusercontent.com/57668948/208065745-b65d56ef-f2e8-4ba6-84fe-40b461f9838a.png)

Jeśli chcemy wymieszać kolejność tych wartości, możemy to zrobić za pomocą `random.shuffle(tablica)`:

![5](https://user-images.githubusercontent.com/57668948/208065763-184467cc-aab8-4725-bc62-a0263ade161d.png)

W ten sposób generowane są zestawy liczb do badania algorytmów sortowania.

Do ich prezentacji posłuży submoduł `pyplot` z modułu `matplotlib`:

![6](https://user-images.githubusercontent.com/57668948/208065773-0db77102-bb71-41af-b50c-1d1f39418729.png)

Otrzymamy rysunek:

![7](https://user-images.githubusercontent.com/57668948/208065784-466e56c2-bb18-4a29-a214-20439b6d562b.png)

Wymaga on oczywiście pewnej "obróbki", ale szczegóły nie są w tym momencie istotne.

Omówię teraz strukturę przygotowanego kodu, na bazie którego należy testować oraz wizualizować działanie poszczególnych algorytmów sortowania, jak w zadaniach poniżej.

Kod składa się, dla zachowania większej czytelności, z dwóch plików. W pliku `mtablica.py` zdefiniowana jest pomocnicza klasa o nazwie `MonitorowanaTablica`, w jej funkcji `__init__` tworzone są, w zależności od trybu, różne tablice: `R` to wartości losowo ułożone, `S` to tablica już posortowana, `A` to tablica posortowana w odwrotnej kolejności, `T` to tablica trzech sekwencji posortowanych (czyli można powiedzieć, posortowana fragmentami). Należy, dla każdego algorytmu, uruchomić każdą z opcji i zobaczyć ile czasu oraz operacji było potrzebne do posortowania. Pozostałe szczegóły implementacji nie są konieczne do wykonania zadania, więc ich tu nie opisuję. Główny plik to `sort1.py`, który importuje potrzebne moduły oraz opisany wyżej typ tablicy. W pliku znajduje się kompletny kod z przykładowym algorytmem sortowania przez wstawianie. Po uruchomieniu, powinniśmy po chwili zobaczyć animację sortowania:

![8](https://user-images.githubusercontent.com/57668948/208065794-55f7bca0-1bd0-46a2-9be5-ef1f1a7d83d7.png)

a także wynik, na przykład:

```text
Sortowanie: Insertion
Tablica posortowana w czasie 18.4 ms. Liczba operacji: 3730.
```

Kod od linii `32` to szczegóły implementacji sposobu wyświetlania histogramu (np. funkcja `update` steruje kolorami poszczególnych słupków, operacja czytania zamienia słupek na zielony, a zapisu na czerwony), na samym końcu wywołana jest funkcja `FuncAnimation`, która akumuluje kolejne klatki w zmiennej `ani`, a całość jest wyświetlona poprzez `plt.show()`. Wynik animacji można też zapisać jako obrazki poszczególnych klatek i połączyć w film za pomocą jakiegoś programu.

Państwa zadaniem będzie implementacja różnych algorytmów sortowania, których kod należy umieścić w miejscu przykładowego kodu `Insertion Sort`. Dany algorytm można oczywiście zapisać w postaci funkcji.

Proszę zwrócić uwagę na pomiar czasu - zaczynający się od odczytu

```py
t0 = time.perf_counter()
```

a kończący się na

```py
delta_t = time.perf_counter() - t0
```

Proszę też dla każdego algorytmu zbadać różne przypadki danych początkowych, które ustawia się w linii:

```py
tablica = MonitorowanaTablica(0, 1000, N, "R") # zbadaj też opcje: "S", "A", "T"
```

## Zadania

Używając kod z pliku `sort1.py` oraz `mtablica.py`, proszę zaimplementować i przebadać następujące algorytmy sortowania.

1. [Bubble sort](https://ufkapano.github.io/algorytmy/lekcja16/bubblesort.html)
2. [Shell sort - np. wg Sedgewicka](https://ufkapano.github.io/algorytmy/lekcja16/shellsort.html)
3. [Merge sort](https://ufkapano.github.io/algorytmy/lekcja16/mergesort.html)
4. [Quick sort](https://ufkapano.github.io/algorytmy/lekcja16/quicksort.html)
5. [Tim sort](https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python)

Proszę, **oprócz kodu algorytmów**, koniecznie zapisać i wysłać **plik z wynikami pomiarowymi**. Może to być prosty plik ASCII, o takiej zawartości:

```text
Insert sort
R: Tablica posortowana w czasie 18.4 ms. Liczba operacji: 3730.
S: Tablica posortowana w czasie 0.6 ms. Liczba operacji: 98.
A: Tablica posortowana w czasie 81.2 ms. Liczba operacji: 7350.
T: Tablica posortowana w czasie 11.1 ms. Liczba operacji: 2254.

Bubble sort
R:
S:
A:
T:
```

i tak dalej.
