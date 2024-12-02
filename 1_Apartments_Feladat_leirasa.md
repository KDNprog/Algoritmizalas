# Apartmanok kiosztása - Feladat leírása

**Feladat:**

Van **n** pályázó és **m** szabad lakás. A feladatunk az, hogy úgy osszuk szét a lakásokat, hogy **minél több pályázó kapjon lakást**.

Minden pályázónak van egy kívánt lakásmérete, akik minden olyan lakást elfogadnak, amelynek mérete elég közel van a kívánt mérethez (legfeljebb **k**-val tér el attól).

Azaz, ha egy pályázó kívánt lakásmérete x, akkor elfogad bármilyen lakást, amelynek mérete $x−k$ és $x+k$ között van.

## Bemenet

- Az első sor tartalmazza az **n** és **m** egész számokat, ahol:

  - **n**: a pályázók száma,
  - **m**: a szabad lakások száma,
  - **k**: a maximálisan megengedett eltérés a kívánt és tényleges lakás mérete között.

- A második sorban **n** egész szám van:

  - **a₁, a₂, ..., aₙ**: a pályázók által kívánt lakásméretek.

- A harmadik sorban **m** egész szám található:
  - **b₁, b₂, ..., bₘ**: a lakások méretei.

## Kimenet

A program egyetlen egész számot adjon meg: azon pályázók számát, akik kapnak lakást.

## Feltételek

$$1 \leq n, m \leq 2 \cdot 10^5$$
$$0 \leq k \leq 10^9$$
$$1 \leq a_i, b_i \leq 10^9$$

## Példa

_Bemenet:_

    4 3 5
    60 45 80 60
    30 60 75

_Kimenet:_

    2

## Magyarázat

A cél az, hogy a pályázókat és a lakásokat úgy párosítsuk össze, hogy:

- egy lakást legfeljebb egy pályázó fogadhat el,
- egy pályázó legfeljebb egy lakást kaphat,
- a pályázó elfogad egy lakást, ha annak mérete az általa kívánt tartományba ($x−k$ és $x+k$ közé) esik.

A példában:

- A 4 jelentkező kívánt lakásmérete: **[60, 45, 80, 60]**
- A 3 szabad lakás mérete: **[30, 60, 75]**
- A maximális eltérés (k): 5
- A pályázók a következő tartományokban fogadják el a lakásokat (k = 5 miatt):
  - Az 1. pályázó: **[55, 65]**
  - A 2. pályázó: **[40, 50]**
  - A 3. pályázó: **[75, 85]**
  - A 4. pályázó: **[55, 65]**

**Megoldás:**

A pályázók által elfogadható lakások:

- Az 1. pályázó (60) elfogad egy 55 és 65 közé eső lakást.

  **Találat**: 60-as lakást kapja.

- A 2. pályázó (45) elfogad egy 40 és 50 közé eső lakást.

  **Találat**: nem talál megfelelő lakást.

- A 3. pályázó (80) elfogad egy 75 és 85 közé eső lakást.

  **Találat**: 75-ös lakást kapja.

- A 4. pályázó (60) elfogad egy 55 és 65 közé eső lakást.

  **Találat**: nem talál több szabad lakást.

Az eredmény: **2** pályázó (1. és 3.) kap lakást.
