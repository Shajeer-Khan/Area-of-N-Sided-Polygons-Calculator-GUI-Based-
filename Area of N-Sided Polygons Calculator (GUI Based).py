#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from math import pi, tan

class PolygonAreaCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("N-Sided Polygon Area Calculator")

        # Input frame
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack()

        self.n_label = tk.Label(self.input_frame, text="Number of sides (n):")
        self.n_label.pack(side=tk.LEFT)

        self.n_entry = tk.Entry(self.input_frame, width=10)
        self.n_entry.pack(side=tk.LEFT)

        self.side_label = tk.Label(self.input_frame, text="Side length (s):")
        self.side_label.pack(side=tk.LEFT)

        self.side_entry = tk.Entry(self.input_frame, width=10)
        self.side_entry.pack(side=tk.LEFT)

        # Button frame
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.calculate_button = tk.Button(self.button_frame, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack(side=tk.LEFT)

        # Result frame
        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack()

        self.result_label = tk.Label(self.result_frame, text="Area:")
        self.result_label.pack(side=tk.LEFT)

        self.result_value = tk.Label(self.result_frame, text="")
        self.result_value.pack(side=tk.LEFT)

    def calculate_area(self):
        try:
            n = int(self.n_entry.get())
            s = float(self.side_entry.get())

            if n < 3:
                self.result_value.config(text="Error: n must be 3 or more")
                return

            area = (n * s**2) / (4 * tan(pi/n))
            self.result_value.config(text=f"{area:.2f}")
        except ValueError:
            self.result_value.config(text="Error: invalid input")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = PolygonAreaCalculator()
    calculator.run()

