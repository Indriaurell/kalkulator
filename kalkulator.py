import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Imup")
        self.root.geometry("360x520")
        self.root.configure(bg="#FFD6E8")  # pink pastel background

        self.expression = ""
        self.current = ""

        # DISPLAY
        self.display = tk.Label(root, text="0", anchor="e",
                                bg="#FFEBF2", fg="#8A4F6D",
                                font=("Segoe UI", 32, "bold"),
                                padx=20, pady=25,
                                bd=0, relief="ridge")
        self.display.pack(fill="both")

        # LAYOUT BUTTONS
        btns = [
            ["%", "CE", "C", "⌫"],
            ["1/x", "x²", "√x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="]
        ]

        frame = tk.Frame(root, bg="#FFD6E8")
        frame.pack(expand=True, fill="both")

        # Color theme
        num_color = "#FFBBD0"
        op_color = "#FF9EC2"
        spec_color = "#FF8CB8"
        equal_color = "#FF6FA8"
        text_color = "#7A3E5C"

        for r, row in enumerate(btns):
            for c, txt in enumerate(row):

                # PILIH WARNA TOMBOL
                if txt in "0123456789":
                    bg = num_color
                elif txt in ["+", "−", "×", "÷"]:
                    bg = op_color
                elif txt == "=":
                    bg = equal_color
                else:
                    bg = spec_color

                btn = tk.Button(
                    frame, text=txt,
                    font=("Segoe UI", 20, "bold"),
                    fg=text_color, bg=bg,
                    bd=0, activebackground="#FFC9DA",
                    relief="flat",
                    command=lambda x=txt: self.button(x)
                )

                btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)
                btn.configure(height=2)

        for i in range(6):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)

    # Format angka 4 digit
    def fmt(self, n):
        n = round(n, 4)
        if float(n).is_integer():
            return str(int(n))
        return f"{n:.4f}".rstrip("0").rstrip(".")

    # Update display
    def update_display(self, txt):
        self.display.config(text=txt)

    # Button logic
    def button(self, label):

        # Angka
        if label.isdigit():
            self.current += label
            self.update_display(self.current)
            return

        # Titik
        if label == ".":
            if "." not in self.current:
                self.current += "."
            self.update_display(self.current)
            return

        # CE
        if label == "CE":
            self.current = ""
            self.update_display("0")
            return

        # C
        if label == "C":
            self.current = ""
            self.expression = ""
            self.update_display("0")
            return

        # Backspace
        if label == "⌫":
            self.current = self.current[:-1]
            self.update_display(self.current if self.current else "0")
            return

        # Persen
        if label == "%":
            if self.current:
                val = float(self.current) / 100
                self.current = self.fmt(val)
                self.update_display(self.current)
            return

        # ±
        if label == "±":
            if self.current:
                if self.current.startswith("-"):
                    self.current = self.current[1:]
                else:
                    self.current = "-" + self.current
                self.update_display(self.current)
            return

        # Reciprocal
        if label == "1/x":
            try:
                val = float(self.current)
                res = self.fmt(1 / val)
                self.current = res
                self.update_display(res)
            except:
                self.update_display("Error")
            return

        # Square
        if label == "x²":
            try:
                val = float(self.current)
                res = self.fmt(val * val)
                self.current = res
                self.update_display(res)
            except:
                self.update_display("Error")
            return

        # Square Root
        if label == "√x":
            try:
                val = float(self.current)
                res = self.fmt(math.sqrt(val))
                self.current = res
                self.update_display(res)
            except:
                self.update_display("Error")
            return

        # Operator
        if label in ("+", "−", "×", "÷"):
            if self.current:
                self.expression += self.current
                self.current = ""

            py = {"+": "+", "−": "-", "×": "*", "÷": "/"}[label]

            if self.expression and self.expression[-1] in "+-*/":
                self.expression = self.expression[:-1] + py
            else:
                self.expression += py

            self.update_display(label)
            return

        # Sama Dengan
        if label == "=":
            try:
                expr = self.expression + self.current
                expr = expr.replace("×", "*").replace("÷", "/")
                result = eval(expr)

                result = self.fmt(result)

                self.update_display(result)
                self.expression = ""
                self.current = result
            except:
                self.update_display("Error")
                self.expression = ""
                self.current = ""
            return


# RUN
root = tk.Tk()
app = Calculator(root)
root.mainloop()