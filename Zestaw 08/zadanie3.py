import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości
okno.title("Zegar i kalendarz")
okno.geometry("600x400")
okno.resizable(False, False)

# utwórz StringVar()
date_time = StringVar()

def update_date_time():
	# dzien = i tak dalej... miesiac, rok, czas, dzien
	# czytamy datetime.today().strftime('%A')
	# kody https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
	day = datetime.today().strftime('%A')
	date = datetime.today().strftime('%d')
	month = datetime.today().strftime('%B')
	year = datetime.today().strftime('%Y')
	time = datetime.today().strftime('%H:%M:%S')
	
	# dt = dzien + ... + "\n" + ...
	dt = day + ", " + date + " " + month + " " + year + "\n" + time
	# ustaw za pomocą .set dt dla StringVar zrobinego powyżej
	date_time.set(dt)
	# ważne: rekurencyjne odświeżanie etykiety - patrz poniżej
	okno.after(1000, update_date_time)

# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania 
# date_time = Label(...
date_time_label = Label(okno, textvariable = date_time, font = ("Calibri", 25), bg = 'black', fg = 'white', width = 500, pady = 40)
date_time_label.pack(anchor = "center")

current_time = datetime.now()
# przyda się do kalendarza
# day = odczytaj przez .strftime('%d')
# month = 
# year = 
day = int(current_time.strftime('%d'))
month = int(current_time.strftime('%m'))
year = int(current_time.strftime('%Y'))

# utwórz cal = Calendar(...
calendar = Calendar(okno, font = ("Arial", 12), selectmode = 'day', year = year, month = month, day = day)
# wstaw przez .pack poniżej zegara
calendar.pack(anchor = "center", pady = 10)

update_date_time()

okno.mainloop()