from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("200x220+500+200")


# Event handlers
def input_char(char):
    if char == "=":
        variable.set(str(calculate_value(variable.get().replace(" ","").replace("\n","").replace(",","."))))
    elif char == "CE":
        variable.set("")
    else:
        variable.set(variable.get() + char)


def calculate_value(expression):
    left_value = "null"
    while len(expression) != 0:
        index = 0
        if left_value == "null":
            while not exist_operator(expression[index]):
                index += 1
            left_value = float(expression[:index])
            expression = expression[index:]
            index = 0
        operator = expression[index]
        expression = expression[(index+1):]
        while (index != len(expression)) and (not exist_operator(expression[index])):
            index += 1
        right_value = float(expression[:index])
        expression = expression[index:]
        left_value = make_operation(left_value, operator, right_value)
    return left_value


def make_operation(left_value, operator, right_value):
    if operator == "-":
        return left_value - right_value
    if operator == "+":
        return left_value + right_value
    if operator == "*":
        return left_value * right_value
    if operator == "/":
        return left_value / right_value
    return "null"


def exist_operator(operator):
    return (operator == "+") or (operator == "-") or (operator == "*") or (operator == "/")


# Calculate string
variable = StringVar()

# Form elements
ent = Entry(textvariable=variable, width=30)
ent.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
btn = Button(text="7")
btn.bind("<Button-1>", lambda event: input_char("7"))
btn.grid(row=1, column=0, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="8")
btn.bind("<Button-1>", lambda event: input_char("8"))
btn.grid(row=1, column=1, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="9")
btn.bind("<Button-1>", lambda event: input_char("9"))
btn.grid(row=1, column=2, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="4")
btn.bind("<Button-1>", lambda event: input_char("4"))
btn.grid(row=2, column=0, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="5")
btn.bind("<Button-1>", lambda event: input_char("5"))
btn.grid(row=2, column=1, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="6")
btn.bind("<Button-1>", lambda event: input_char("6"))
btn.grid(row=2, column=2, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="1")
btn.bind("<Button-1>", lambda event: input_char("1"))
btn.grid(row=3, column=0, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="2")
btn.bind("<Button-1>", lambda event: input_char("2"))
btn.grid(row=3, column=1, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="3")
btn.bind("<Button-1>", lambda event: input_char("3"))
btn.grid(row=3, column=2, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="0")
btn.bind("<Button-1>", lambda event: input_char("0"))
btn.grid(row=4, column=0, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="-")
btn.bind("<Button-1>", lambda event: input_char("-"))
btn.grid(row=4, column=1, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="+")
btn.bind("<Button-1>", lambda event: input_char("+"))
btn.grid(row=4, column=2, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="=")
btn.bind("<Button-1>", lambda event: input_char("="))
btn.grid(row=4, column=3, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="/")
btn.bind("<Button-1>", lambda event: input_char("/"))
btn.grid(row=3, column=3, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="*")
btn.bind("<Button-1>", lambda event: input_char("*"))
btn.grid(row=2, column=3, ipadx=10, ipady=6, padx=5, pady=5)
btn = Button(text="CE")
btn.bind("<Button-1>", lambda event: input_char("CE"))
btn.grid(row=1, column=3, ipadx=10, ipady=6, padx=5, pady=5)

root.mainloop()