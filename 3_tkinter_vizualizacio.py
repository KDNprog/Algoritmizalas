import tkinter as tk
from time import sleep

MOD = 10**9 + 7

def visualize_count_ways(n):
    # Tkinter ablak létrehozása
    window = tk.Tk()
    window.title("Dobások vizualizációja - Dinamikus Programozás")
    canvas = tk.Canvas(window, width=1000, height=700, bg="white")
    canvas.pack()
    
    # Alap méretek
    cell_size = 40
    x_start, y_start = 100, 100
    dp_start_y = 500  # DP tömb elhelyezése
    dice_colors = ["red", "blue", "green", "orange", "purple", "brown"]
    
    # Dobások táblázatának inicializálása
    dice_table = [[None for _ in range(6)] for _ in range(n + 1)]
    for dice in range(6):  # Dobások oszlopainak címe
        x = x_start + dice * cell_size
        y = y_start - cell_size
        canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=dice_colors[dice])
        canvas.create_text(x + cell_size // 2, y + cell_size // 2, text=str(dice + 1), font=("Helvetica", 12), fill="white")
    
    # Táblázat cellák létrehozása
    for i in range(1, n + 1):  # Sorok
        for dice in range(6):  # Oszlopok
            x = x_start + dice * cell_size
            y = y_start + i * cell_size
            rect = canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="white")
            text = canvas.create_text(x + cell_size // 2, y + cell_size // 2, text="0", font=("Helvetica", 10))
            dice_table[i][dice] = (rect, text)
    
    # DP tömb inicializálása külön sorban
    dp_cells = []
    for i in range(n + 1):
        x = x_start + i * cell_size
        rect = canvas.create_rectangle(x, dp_start_y, x + cell_size, dp_start_y + cell_size, fill="lightgray")
        text = canvas.create_text(x + cell_size // 2, dp_start_y + cell_size // 2, text="0", font=("Helvetica", 12))
        dp_cells.append((rect, text))
    
    # Dinamikus programozás számítása
    dp = [0] * (n + 1)
    dp[0] = 1
    canvas.itemconfig(dp_cells[0][1], text="1", fill="blue")
    canvas.update()
    sleep(1)

    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                # Frissített értékek kiemelése
                canvas.itemconfig(dice_table[i][j - 1][0], fill="yellow")
                canvas.update()
                sleep(0.3)

                # Dobás alapján számított érték
                current_value = int(canvas.itemcget(dice_table[i][j - 1][1], "text"))
                new_value = (current_value + dp[i - j]) % MOD
                canvas.itemconfig(dice_table[i][j - 1][1], text=str(new_value))

                # DP frissítése
                dp[i] = (dp[i] + dp[i - j]) % MOD
                canvas.itemconfig(dp_cells[i][1], text=str(dp[i]))
                canvas.update()
                sleep(0.3)

                # Kiemelés visszaállítása
                canvas.itemconfig(dice_table[i][j - 1][0], fill="white")
    
    # Eredmény megjelenítése
    result_text = f"Eredmény: {dp[n]} módon érhetjük el az {n}-t"
    canvas.create_text(500, 650, text=result_text, font=("Helvetica", 16), fill="black")
    window.mainloop()

# Bemenet
n = int(input("Add meg az n értékét: "))
visualize_count_ways(n)
