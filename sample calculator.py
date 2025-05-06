import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.set(result)
        except Exception as e:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.StringVar()
entry_field = tk.Entry(root, textvar=entry, font="Arial 20")
entry_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Creating buttons using loops
for row in buttons:
    frame = tk.Frame(root)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
