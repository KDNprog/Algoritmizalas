import tkinter as tk
from collections import defaultdict

# DFS függvény az alárendeltségek kiszámításához
def dfs(node, tree, subordinates):
    for child in tree[node]:
        subordinates[node] += dfs(child, tree, subordinates)
    return subordinates[node] + 1

# Tkinter rajzoló függvény a fa vizualizációjához
def draw_tree(canvas, tree, subordinates, node, x, y, x_step, y_step):
    if node not in tree:
        return

    for i, child in enumerate(tree[node]):
        child_x = x + (i - len(tree[node]) / 2) * x_step
        child_y = y + y_step

        # Vonal rajzolása a szülőtől a gyerekhez
        canvas.create_line(x, y, child_x, child_y, fill="black")

        # Gyerekek rekurzív kirajzolása
        draw_tree(canvas, tree, subordinates, child, child_x, child_y, x_step / 2, y_step)

    # Csomópont rajzolása
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
    canvas.create_text(x, y, text=f"{node}\n{subordinates[node]}", font=("Arial", 10))

# Tkinter ablak inicializálása
def visualize_hierarchy(n, bosses):
    # Gráf építése
    tree = defaultdict(list)
    for i in range(n - 1):
        tree[bosses[i]].append(i + 2)

    # Beosztottak számának kiszámítása
    subordinates = [0] * (n + 1)
    dfs(1, tree, subordinates)

    # Tkinter ablak létrehozása
    root = tk.Tk()
    root.title("Vállalati hierarchia")

    # Vászon létrehozása a rajzoláshoz
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    # Fa kirajzolása
    draw_tree(canvas, tree, subordinates, 1, 400, 50, 150, 100)

    # Tkinter futtatása
    root.mainloop()

# Bemenet olvasása
if __name__ == "__main__":
    # Példa bemenet
    n = 5
    bosses = [1, 1, 2, 3]

    # Hierarchia vizualizálása
    visualize_hierarchy(n, bosses)
