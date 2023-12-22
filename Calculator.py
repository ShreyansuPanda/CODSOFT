import tkinter as tk

calculation = ""

def add_to_calculation(symbols):
    global calculation
    calculation += str(symbols)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error!")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("500x420")
root.title("Calculator")
root.resizable(False, False)

text_result = tk.Text(root, height=6, width=30, font=("Arial", 24))
text_result.grid(columnspan=7)

button_params = {
    "width": 8,
    "height": 1,
    "font": ("Arial", 14)
}

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), **button_params)
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), **button_params)
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), **button_params)
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), **button_params)
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), **button_params)
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), **button_params)
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), **button_params)
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), **button_params)
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), **button_params)
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), **button_params)
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), **button_params)
btn_plus.grid(row=2, column=4)
btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), **button_params)
btn_sub.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), **button_params)
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), **button_params)
btn_div.grid(row=5, column=4)
btn_o = tk.Button(root, text="(", command=lambda: add_to_calculation("("), **button_params)
btn_o.grid(row=5, column=1)
btn_c = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), **button_params)
btn_c.grid(row=5, column=3)
btn_ac = tk.Button(root, text="AC", command=clear_field, **button_params)
btn_ac.grid(row=6, column=1)
btn_eq = tk.Button(root, text="=", command=evaluate_calculation, **button_params)
btn_eq.grid(row=6, column=3)
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), **button_params)
btn_dot.grid(row=6, column=2)
btn_mol = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), **button_params)
btn_mol.grid(row=6, column=4)

root.mainloop()
