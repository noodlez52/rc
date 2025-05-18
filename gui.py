import tkinter as tk
from tkinter import ttk, messagebox
from circuits import RCCircuit
import sqlite3

def build_gui():
    db = sqlite3.connect("data.db")
    db.execute("CREATE TABLE IF NOT EXISTS rc_data (R REAL, C REAL, tau REAL)")

    root = tk.Tk()
    root.title("RC Calculator")

    tk.Label(root, text="Resistance (Ω)").grid(row=0, column=0)
    r_entry = tk.Entry(root); r_entry.grid(row=0, column=1)
    tk.Label(root, text="Capacitance (F)").grid(row=1, column=0)
    c_entry = tk.Entry(root); c_entry.grid(row=1, column=1)

    result = tk.StringVar(value="𝜏 = ? s")
    tk.Label(root, textvariable=result, font=("Arial", 14)).grid(row=2, columnspan=2, pady=10)

    def calculate():
        try:
            R, C = float(r_entry.get()), float(c_entry.get())
            circuit = RCCircuit(R, C)
            circuit.save(db)
            result.set(f"𝜏 = {circuit.tau:.4g} s")
        except ValueError:
            messagebox.showerror("Error", "Enter numbers!!")

    ttk.Button(root, text="Compute", command=calculate).grid(row=3, columnspan=2, pady=5)
    root.mainloop()

if __name__ == "__main__":
    build_gui()
