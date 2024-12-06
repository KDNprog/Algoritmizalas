# Kocka kombinációk - Feladat leírása

Ez a feladat egy klasszikus dinamikus programozási probléma, amelynek célja, hogy meghatározzuk, hányféleképpen érhetjük el az **n**-et, ha egy **dobókocka** segítségével próbáljuk meg összeadni azt. A dobókocka dobásai mindig egy 1 és 6 közötti számot adnak eredményül.

## Feladat

Adott egy **dobókocka**, amely egyetlen dobás alkalmával **1** és **6** közötti számot adhat (beleértve a 1-et és 6-ot). A célunk, hogy kiszámoljuk, hányféleképpen érhetjük el az **n** összegét azzal, hogy egy vagy több dobást hajtunk végre, és minden dobás után a kapott számokat összeadjuk.

### Példa

Ha $n=3$, akkor a következő módokon érhetjük el a 3-as összegét:

- $1+1+1$
- $1+2$
- $2+1$
- $3$

Ez összesen 4 különböző módot jelent, tehát a válasz **4**.

## Bemenet

- Egyetlen sorban egy egész szám: **n**.

## Kimenet

- Kiírja a $10^9+7$ modulo módok számát.

## Feltételek

$$1 \leq n \leq 10^6$$

## Példa

_Bemenet:_

    3

_Kimenet:_

    4

## Magyarázat

A cél az, hogy megszámoljuk, hányféleképpen érhetjük el az **n** összeget kockadobásokkal. Minden dobás egy értéket ad vissza 1 és 6 között, tehát minden egyes dobás eredménye 1, 2, 3, 4, 5 vagy 6 lehet.

Az összeg eléréséhez egy vagy több dobás szükséges. A válaszban minden számot a $10^9+7$ modulos művelettel kell visszaadni, hogy a válasz ne legyen túl nagy.

A probléma lényege, hogy **dinamikus programozással** kell kiszámolnunk, hogy hányféleképpen érhetjük el a kívánt **n** összeget kockadobásokkal.
