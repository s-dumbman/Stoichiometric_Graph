import json
import numpy as np
import matplotlib.pyplot as plt

def load_banclip(filename="banclip.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    b2 = data["b2"]
    return b2

def load_fomulaclip(filename="fomulaclip.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    first_number = data["first_number"]
    second_number = data["second_number"]
    third_number = data["third_number"]
    return first_number, second_number, third_number

f1, f2, f3= load_fomulaclip()
b2 = load_banclip()
print('b2 : {}'.format(b2["volume"]))
print('f1 : {}'.format(f1))
print('f2 : {}'.format(f2))
    

def plot_function(x_range=(0, 2*(f1 / f2 * float(b2["volume"]))), n_points=1000):
    global f1, f2, f3, b2
    x = np.linspace(x_range[0], x_range[1], n_points)
    
    try:
        d = f1 / f2 * float(b2["volume"])

        y = np.zeros_like(x)

        mask1 = x <= d
        mask2 = x > d

        y[mask1] = (f3 / f1 * x[mask1])/(f3 / f1 * x[mask1] + b2["volume"] - f2 / f1 * x[mask1])
        y[mask2] = (f3 / f2 * float(b2["volume"]))/(f3 / f2 * float(b2["volume"]) + x[mask2] - f1 / f2 * float(b2["volume"]))

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"mol of C / mol of All (y)")
        plt.axvline(d, color='red', linestyle='--', label=f"x = {d:.2f} (limiting A)")
        plt.title(f"{f1}A + {f2}B → {f3}C - Anchor B : {b2["volume"]} mol")
        plt.xlabel("mol of A (x)")
        plt.ylabel("mol of C / mol of All (y)")
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

plot_function()

#       y[mask1] = f3 / f1 * x[mask1]
#       y[mask2] = f3 / f2 * float(b2["volume"])

#       y[mask1] = (f3 / f1 * x[mask1])/(f3 / f1 * x[mask1] + b2["volume"] - f2 / f1 * x[mask1])
#       y[mask2] = (f3 / f2 * float(b2["volume"]))/(f3 / f2 * float(b2["volume"]) + x[mask2] - f1 / f2 * float(b2["volume"]))