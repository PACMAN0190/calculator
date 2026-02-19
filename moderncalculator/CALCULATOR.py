import tkinter as tk
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")
display = tk.Entry(root, font=("Arial", 32), bd=0, bg="#1e1e1e", fg="#FFD700", justify="right")
display.pack(expand=True, fill="both", padx=10, pady=(20, 10))

def on_click(key):
    if key == "C":
        display.delete(0, tk.END)
    elif key == "⌫":
        display.delete(len(display.get())-1, tk.END)
    elif key == "=":
        try:
            expr = display.get().replace("×", "*").replace("÷", "/")
            display.delete(0, tk.END)
            display.insert(0, str(eval(expr)))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, key)
buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]
for i, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
    for j, button in enumerate(row):
        # Determine color
        color = "#FFD700" if button in ["+", "-", "×", "÷", "="] else "#2d2d2d"
        fg_color = "black" if button in ["+", "-", "×", "÷", "="] else "white"
        
        # Button width for "0"
        if button == "0" and i == 4:
            b = tk.Button(frame, text=button, bg=color, fg=fg_color, font=("Arial", 20),
                          bd=0, command=lambda t=button: on_click(t))
            b.pack(side="left", expand=True, fill="both", padx=(0,5))
            
            # Add empty space next to "0" to simulate double-width
            dummy = tk.Label(frame, bg="#1e1e1e")
            dummy.pack(side="left", expand=True, fill="both", padx=(5,0))
        else:
            b = tk.Button(frame, text=button, bg=color, fg=fg_color, font=("Arial", 20),
                          bd=0, command=lambda t=button: on_click(t))
            b.pack(side="left", expand=True, fill="both", padx=5)

# ------------------ Run App ------------------
root.mainloop()

