import tkinter as tk
from tkinter import messagebox, scrolledtext

# Luhn algorithm implementation
def luhn_checksum(card_number: str) -> bool:
    digits = [int(d) for d in card_number]
    total = 0
    for i, d in enumerate(reversed(digits), start=1):
        if i % 2 == 0:
            doubled = d * 2
            total += doubled - 9 if doubled > 9 else doubled
        else:
            total += d
    return total % 10 == 0

# Generate valid Luhn-matching numbers based on partial input
def find_luhn_matches(bin_prefix: str, last4: str, sample_limit: int = 10):
    matches = []
    total_checked = 0
    total_valid = 0

    for i in range(1000000):
        middle = f"{i:06d}"
        card_number = bin_prefix + middle + last4
        total_checked += 1
        if luhn_checksum(card_number):
            total_valid += 1
            if len(matches) < sample_limit:
                matches.append(card_number)

    return total_checked, total_valid, matches

# Function triggered by GUI button
def run_luhn_search():
    bin_prefix = entry_bin.get().strip()
    last4 = entry_last4.get().strip()
    try:
        sample_limit = int(entry_sample.get().strip())
        if len(bin_prefix) != 6 or len(last4) != 4:
            raise ValueError("BIN must be 6 digits and last4 must be 4 digits.")

        checked, valid, matches = find_luhn_matches(bin_prefix, last4, sample_limit)
        output.delete('1.0', tk.END)
        output.insert(tk.END, f"Checked: {checked:,}\nValid Luhn matches: {valid:,}\n\n")
        for card in matches:
            output.insert(tk.END, card + "\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Luhn Brute-force Trainer (Educational Use Only)")
root.geometry("500x400")

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="First 6 digits (BIN):").grid(row=0, column=0, sticky='e')
entry_bin = tk.Entry(frame)
entry_bin.grid(row=0, column=1)

tk.Label(frame, text="Last 4 digits:").grid(row=1, column=0, sticky='e')
entry_last4 = tk.Entry(frame)
entry_last4.grid(row=1, column=1)

tk.Label(frame, text="Sample count:").grid(row=2, column=0, sticky='e')
entry_sample = tk.Entry(frame)
entry_sample.insert(0, "10")
entry_sample.grid(row=2, column=1)

tk.Button(root, text="Find Valid Numbers", command=run_luhn_search).pack(pady=10)

output = scrolledtext.ScrolledText(root, width=60, height=15)
output.pack(padx=10, pady=10)

root.mainloop()
