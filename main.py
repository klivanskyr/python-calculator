import tkinter as tk #gui
import sympy #evaluation

input = ""

#appends key to end of input
def add_to_input(key) -> None:
    global input
    input += str(key)
    clear_text()
    equation.insert(1.0, input)

#clears the input
def clear_text() -> None:
    equation.delete(1.0, "end")

#evalulate the input
def evaluate_input() -> None:
    global input
    try:
        evaluation = str(int(sympy.sympify(input)))
        clear_text()
        equation.insert(1.0, evaluation)
        input = ""
    except:
        clear_text()
        equation.insert(1.0, "ERROR")
        pass



BTN_HT = 4
BNT_WT = 12
window = tk.Tk()
window.geometry("400x450")


###EQUATION TEXT
equation = tk.Text(height=2, width=22, font=("Arial", 24))
equation.grid(columnspan=5)

###DIGITS
digit_btns = []
for i in range(10):
    digit_btns.append(tk.Button(text=str(i), width=BNT_WT, height=BTN_HT, command=lambda i=i: add_to_input(i)))

for i, btn in enumerate(reversed(digit_btns[1:])):
    btn.grid(row=(i//3)+2, column=3-(i%3))

digit_btns[0].grid(row=5, column=2)

####OPERATIONS
ops = ["+", "-", "*", "/"]
op_btns = []
for op in ops:
    op_btns.append(tk.Button(text=op, width=BNT_WT, height=BTN_HT, command=lambda op=op: add_to_input(op)))

for i, btn in enumerate(op_btns):
    btn.grid(row=i+2 , column=4)

####Other
left_btn = tk.Button(text="(", width=BNT_WT, height=BTN_HT, command=lambda: add_to_input("("))
left_btn.grid(row=5, column=1)
right_btn = tk.Button(text=")", width=BNT_WT, height=BTN_HT, command=lambda: add_to_input(")"))
right_btn.grid(row=5, column=3)
equal_btn = tk.Button(text="=", width=2*BNT_WT, height=BTN_HT, command=evaluate_input)
equal_btn.grid(row=6, column=3, columnspan=2)
clear_btn = tk.Button(text="C", width=2*BNT_WT, height=BTN_HT, command=clear_text)
clear_btn.grid(row=6, column=1, columnspan=2)


window.mainloop()


