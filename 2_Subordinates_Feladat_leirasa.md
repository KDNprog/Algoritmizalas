# Beosztottak - Feladat leírása

**Feladat:**

Egy **vállalati hierarchiában** (fa struktúra) minden dolgozóra ki kell számolni, hogy hány **alárendeltje (beosztottja)** van (közvetlen és közvetett alárendeltek együtt).

## Bemenet

- Az első sor tartalmazza az alkalmazottak számát: $n$.

  - Az alkalmazottak sorszámozása: $1,2,…,n$.
  - Az 1-es alkalmazott a vállalat vezérigazgatója (gyökér).

- A második sor $n−1$ egész számot tartalmaz, ahol a $k$-adik szám azt jelenti, hogy ki az $k+1$-edik alkalmazott közvetlen felettese.

## Kimenet

A kimenetben $n$ szám szerepeljen: minden $i$-edik szám az $i$-edik alkalmazott alárendeltjeinek száma.

## Feltételek

$$1 \leq n\leq 2 \cdot 10^5$$

## Példa

_Bemenet:_

    5
    1 1 2 3

_Kimenet:_

    4 1 1 0 0

## Magyarázat

- Az 1-es dolgozónak 4 alárendeltje van (közvetlenül 2 és 3, közvetve pedig 4 és 5).
- A 2-es dolgozónak 1 alárendeltje van (a 4-es dolgozó).
- A 3-as dolgozónak 1 alárendeltje van (az 5-ös dolgozó).
- A 4-es és 5-ös dolgozóknak nincsenek alárendeltjei.
