import tkinter as tk
from tkinter import ttk
from black_scholes import BS

class BSCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('BS Calculator')
        self.geometry('400x600')
        self.configure(bg='#2C3E50')  # Dark blue background

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TLabel', background='#2C3E50', foreground='white', font=('Arial', 12))
        self.style.configure('TEntry', fieldbackground='#34495E', foreground='white', font=('Arial', 12))
        self.style.configure('TButton', background='#3498DB', foreground='white', font=('Arial', 12, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20 20 20 20", style='TFrame')
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        labels = ['Spot', 'Strike', 'Rate', 'Days', 'Vol', 'Multiplier']
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(main_frame, text=label).grid(column=0, row=i, sticky=tk.W, pady=5)
            entry = ttk.Entry(main_frame, width=20)
            entry.grid(column=1, row=i, sticky=(tk.W, tk.E), pady=5)
            self.entries[label.lower()] = entry

        default_values = {'spot': 1800, 'strike': 1800, 'rate': 0.01, 'days': 30, 'vol': 0.2, 'multiplier': 100}
        for key, value in default_values.items():
            self.entries[key].insert(0, value)

        calculate_button = ttk.Button(main_frame, text="Calculate", command=self.calculate)
        calculate_button.grid(column=0, row=len(labels), columnspan=2, pady=20)

        self.result_text = tk.Text(main_frame, height=10, width=40, bg='#34495E', fg='white', font=('Courier', 12))
        self.result_text.grid(column=0, row=len(labels)+1, columnspan=2, pady=10)

    def calculate(self):
        try:
            values = {key: float(entry.get()) for key, entry in self.entries.items()}
            bs = BS(values['spot'], values['strike'], values['rate'], values['days'], values['vol'], values['multiplier'])

            results = [
                f"Call Price: {bs.call_price()}",
                f"Put Price: {bs.put_price()}",
                f"Call Delta: {bs.call_delta():.4f}",
                f"Put Delta: {bs.put_delta():.4f}",
                f"Gamma: {bs.call_gamma():.4f}",
                f"Vega: {bs.call_vega():.4f}",
                f"Call Theta: {bs.call_theta():.4f}",
                f"Put Theta: {bs.put_theta():.4f}",
                f"Call Rho: {bs.call_rho():.4f}",
                f"Put Rho: {bs.put_rho():.4f}"
            ]

            self.result_text.delete(1.0, tk.END)
            for result in results:
                self.result_text.insert(tk.END, result + '\n')

        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app = BSCalculatorApp()
    app.mainloop()
