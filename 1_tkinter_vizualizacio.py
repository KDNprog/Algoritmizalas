import tkinter as tk
from time import sleep

def visualize_allocation(applicants, apartments, k):
    # Tkinter ablak létrehozása
    window = tk.Tk()
    window.title("Pályázók és lakások vizualizáció")

    # Canvas (rajzfelület) beállítása
    canvas = tk.Canvas(window, width=800, height=400, bg="white")
    canvas.pack()

    # Pályázók és lakások oszlopainak kezdő pozíciói
    applicant_x = 200
    apartment_x = 600
    y_start = 50
    step = 50

    # Pályázók és lakások rajzolása
    applicant_ids = []
    apartment_ids = []
    
    for i, size in enumerate(applicants):
        rect = canvas.create_rectangle(applicant_x - 30, y_start + i * step - 20,
                                       applicant_x + 30, y_start + i * step + 20,
                                       fill="lightblue")
        text = canvas.create_text(applicant_x, y_start + i * step, text=str(size))
        applicant_ids.append((rect, text))
    
    for j, size in enumerate(apartments):
        rect = canvas.create_rectangle(apartment_x - 30, y_start + j * step - 20,
                                       apartment_x + 30, y_start + j * step + 20,
                                       fill="lightgreen")
        text = canvas.create_text(apartment_x, y_start + j * step, text=str(size))
        apartment_ids.append((rect, text))

    # Kétmutatós algoritmus vizualizációja
    i = j = matches = 0
    while i < len(applicants) and j < len(apartments):
        canvas.update()
        sleep(1)  # Lassítás az animációhoz
        
        # Kiemeljük az aktuálisan vizsgált elemeket
        canvas.itemconfig(applicant_ids[i][0], outline="red", width=3)
        canvas.itemconfig(apartment_ids[j][0], outline="red", width=3)

        if abs(applicants[i] - apartments[j]) <= k:
            # Sikeres párosítás
            matches += 1
            canvas.itemconfig(applicant_ids[i][0], fill="blue")
            canvas.itemconfig(apartment_ids[j][0], fill="blue")
            i += 1
            j += 1
        elif applicants[i] < apartments[j] - k:
            # Párosítás sikertelen, pályázó nem talál megfelelőt
            canvas.itemconfig(applicant_ids[i][0], fill="gray")
            i += 1
        else:
            # Párosítás sikertelen, lakás nem talál megfelelő pályázót
            canvas.itemconfig(apartment_ids[j][0], fill="gray")
            j += 1

        # Visszaállítjuk az alap állapotot
        canvas.itemconfig(applicant_ids[i - 1][0], outline="black", width=1)
        canvas.itemconfig(apartment_ids[j - 1][0], outline="black", width=1)

    # Eredmény kijelzése
    result_text = f"Sikeres párosítások száma: {matches}"
    canvas.create_text(400, 350, text=result_text, font=("Helvetica", 16), fill="black")

    # Program futtatása
    window.mainloop()

# Tesztadatok
applicants = [60, 45, 80, 60]
apartments = [30, 60, 75]
k = 5

# Adatok rendezése
applicants.sort()
apartments.sort()

# Vizualizáció indítása
visualize_allocation(applicants, apartments, k)
