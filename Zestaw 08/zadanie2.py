import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
# dodać tytuł, rozmiar
okno.title("PDF Viewer")
okno.geometry("400x400")

# dodać widget Text i umieściś z jakimś marginesem
text = tk.Text(okno, bg='white', fg='black', font=('Arial', 12), wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   okno.destroy()

# utworzyć widget Menu i jego strukturę jak na rysunku
menubar = tk.Menu(okno)
filemenu = tk.Menu(menubar, tearoff=0)
# Open powinno wołać open_pdf
filemenu.add_command(label="Open", command=open_pdf)
# Clear powinno wołać clear_text
filemenu.add_command(label="Clear", command=clear_text)
# Quit powinno wołać quit_app
filemenu.add_command(label="Quit", command=quit_app)

menubar.add_cascade(label="File", menu=filemenu)
okno.config(menu=menubar)

okno.mainloop()