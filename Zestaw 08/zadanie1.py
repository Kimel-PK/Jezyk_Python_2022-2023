import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry = Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

# <ChatGPT>
def evaluate_expression(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == "+":
                result = op1 + op2
            elif char == "-":
                result = op1 - op2
            elif char == "×":
                result = op1 * op2
            elif char == "/":
                result = op1 / op2
            stack.append(result)
    return stack.pop()

def infix_to_postfix(expression):
    precedence = {'+':1,'-':1,'×':2,'/':2,'^':3}
    operators = []
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char in '+-×/^':
            while operators and precedence[char]<=precedence.get(operators[-1],0):
                postfix.append(operators.pop())
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()
    while operators:
        postfix.append(operators.pop())
    return ''.join(postfix)

# </ChatGPT>

buttons = ["7", "8", "9", "/", "4", "5", "6", "×", "1", "2", "3", "-", "C", "0", "=", "+"]
row = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
column = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

for i in range (len (buttons)):
    btn = Button (okno, text=buttons[i], padx = 20, pady = 10)
    btn['font'] = myFont
    btn.grid(row=row[i], column=column[i])

def mouse_button_release (event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert (len (ans_entry.get ()), text)

    if text in "+-×/":
        if len (ans_entry.get ()) == 0:
            return
        
        if ans_entry.get ()[len (ans_entry.get ()) - 1] in "+-×/":
            ans_entry.delete (len(ans_entry.get ()) - 1)
        
        ans_entry.insert (len (ans_entry.get ()), text)

    if text == "C":
        ans_entry.delete (0, "end")

    if text == "=":
        # jakieś obliczenia
        wynik = int (evaluate_expression (infix_to_postfix (ans_entry.get ())))
        ans_entry.delete (0, "end")
        ans_entry.insert (0, wynik)

# sposób na reakcję 
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
