# Kocka kombinációk - Feladat megoldása

A feladat célja, hogy meghatározzuk, hányféleképpen érhetjük el az **n** összeget, ha minden dobás egy kockával történik, és a dobás eredménye egy 1 és 6 közötti szám lehet. Az összeg eléréséhez több dobás is szükséges lehet, tehát a feladat alapvetően egy dinamikus programozásos problémát jelent.

A **dinamikus programozás** módszere jól alkalmazható ebben a problémában, mivel a megoldást **lépésről lépésre** építhetjük fel.

## A feladat megoldásának menete

### 1. Alapgondolat

A feladatot úgy tekinthetjük, hogy minden egyes számot (**1**-től **n**-ig) különböző módokon érhetünk el a kockadobások segítségével. Az egyik megoldás minden egyes **i** szám eléréséhez hozzáadja azokat az előző eredményeket, amelyek elérhetőek egy dobással.

### 2. Megoldás példán keresztül

**1. dp tömb**

- Az algoritmus alapja egy **dp** (dynamic programming) **tömb**.

- A **dp[i]** azt fogja tárolni, hogy hányféleképpen érhetjük el az **i** összeget.

- Az alapérték, hogy **dp[0] = 1**, mert a **0**-át pontosan egyféleképpen érhetjük el: nem dobunk.

Kezdetben az **dp tömb** így néz ki:

    dp = [1, 0, 0, 0, 0]  # dp[0] = 1, mert 0-t csak egyféleképpen érhetjük el (nem dobunk)

**2. Első lépés (i = 1)**

- Most próbáljuk elérni az **1**-es összeget.
- Mivel egy dobás lehet **1, 2, 3, 4, 5** vagy **6**, nézzük meg, hogy az **i = 1** értéket milyen módon érhetjük el:
  - Ha dobunk egy **1**-est, akkor elérhetjük az **1**-et.
  - Így a **dp[1]** értéke: **dp[1] = dp[1 - 1] = dp[0] = 1**.
  - Tehát **dp[1] = 1**.

Az **dp tömb** most így néz ki:

    dp = [1, 1, 0, 0, 0]  # 1-t csak egyféleképpen érhetjük el: 1

**3. Második lépés (i = 2)**

- Most nézzük meg, hogyan érhetjük el a **2**-t:
- Ha dobunk egy **1**-est, akkor a **2**-t úgy érhetjük el, hogy előtte elérjük a **1**-et. Azaz **dp[2] = dp[2 - 1] = dp[1]**.
- Ha dobunk egy **2**-est, akkor elérhetjük közvetlenül a **2**-t, tehát **dp[2] = dp[2 - 2] = dp[0].**
- Tehát **dp[2] = dp[1] + dp[0] = 1 + 1 = 2**.

Az **dp tömb** most így néz ki:

    dp = [1, 1, 2, 0, 0]  # 2-t kétféleképpen érhetjük el: 1 + 1, 2

**4. Harmadik lépés (i = 3)**

- Most próbáljuk elérni a **3**-as összeget.
- Ha dobunk egy **1**-est, akkor elérhetjük a **3**-at, ha előtte elértük a **2**-t. Tehát **dp[3] = dp[3 - 1] = dp[2]**.
- Ha dobunk egy **2**-est, akkor elérhetjük a **3**-at, ha előtte elértük az **1**-et. Tehát **dp[3] = dp[3 - 2] = dp[1]**.
- Ha dobunk egy **3**-ast, akkor közvetlenül elérhetjük a **3**-at, tehát **dp[3] = dp[3 - 3] = dp[0]**.
- Tehát **dp[3] = dp[2] + dp[1] + dp[0] = 2 + 1 + 1 = 4**.

Az **dp tömb** most így néz ki:

    dp = [1, 1, 2, 4, 0]  # 3-t négyféleképpen érhetjük el: 1 + 1 + 1, 1 + 2, 2 + 1, 3

**5. Negyedik lépés (i = 4)**

- Most próbáljuk elérni a **4**-es összeget:
- Ha dobunk egy **1**-est, akkor elérhetjük a **4**-et, ha előtte elértük a **3**-at. Tehát **dp[4] = dp[4 - 1] = dp[3]**.
- Ha dobunk egy **2**-est, akkor elérhetjük a **4**-et, ha előtte elértük a **2**-t. Tehát **dp[4] = dp[4 - 2] = dp[2]**.
- Ha dobunk egy **3**-ast, akkor elérhetjük a **4**-et, ha előtte elértük az **1**-et. Tehát **dp[4] = dp[4 - 3] = dp[1]**.
- Ha dobunk egy **4**-est, akkor közvetlenül elérhetjük a **4**-et, tehát **dp[4] = dp[4 - 4] = dp[0]**.
- Tehát **dp[4] = dp[3] + dp[2] + dp[1] + dp[0] = 4 + 2 + 1 + 1 = 8**.

Az **dp tömb** most így néz ki:

    dp = [1, 1, 2, 4, 8]  # 4-et nyolcféleképpen érhetjük el

**6. Az algoritmus alkalmazása nagyobb számra**

- Nézzük meg, hogyan alkalmazzuk ezt az algoritmust egy nagyobb számra, például **n = 6**.
- A folyamat ugyanúgy történik, végigmegyünk minden számról **1**-től **n**-ig, és az előző számokhoz adunk hozzá lehetőségeket.

## A kód magyarázata

A program alapvetően a fent leírt dinamikus programozást valósítja meg, ahol a **dp[i]** tárolja, hányféleképpen érhetjük el az **i** összeget.

    MOD = 10\*\*9 + 7

    def count_ways(n):
      dp = [0] * (n + 1)
      dp[0] = 1  # Alap: 0-hoz egyféleképpen elérhetjük (nem dobunk).

      for i in range(1, n + 1):
          for j in range(1, 7):  # Dobások: 1, 2, 3, 4, 5, 6
              if i - j >= 0:  # Csak akkor, ha i-j nem negatív
                  dp[i] = (dp[i] + dp[i - j]) % MOD  # Hozzáadjuk a lehetőségeket

      return dp[n]  # Az eredmény: hányféleképpen érhetjük el n-t

    # Bemenneti adat

    n = int(input())
    print(count_ways(n))
