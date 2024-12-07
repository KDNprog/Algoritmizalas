# Beosztottak - Feladat megoldása

**Megoldási stratégia:**

- A probléma lényege, hogy egy **fa struktúrában**, amely egy **vállalati hierarchiát** modellez, minden csomóponthoz (**alkalmazotthoz**) ki kell számítani, hogy hány közvetett és közvetlen **alárendeltje** van.
- A fa szerkezetének gyökere a vállalat igazgatója.
- Mivel a fa természetes hierarchikus struktúra, a megoldás rekurzív stratégia alkalmazásával hatékonyan megvalósítható.

## Stratégiai lépések

1. **Hierarchia modellezése gráfként**:

   - A bemenetben minden alkalmazott $2$-től $n$-ig megkapja a közvetlen főnökének az indexét.
   - Ebből egy **szomszédsági listát** (gráf-reprezentációt) építünk, ahol minden csomópont (főnök) a gyerekeire mutat.

2. **Alárendeltségek kiszámítása DFS-sel:**:

   - A **mélységi keresés** (DFS) segítségével számítjuk ki az alárendeltek számát:
   - Minden csomópont alárendeltségeinek száma a gyerekei alárendeltségeinek összegéből és saját magából áll.
   - Ez természetesen rekurzív, mert minden csomópont eredménye a gyerekeinek eredményére épül.

3. **Eredmények kiírása**:

   - Az összes csomópont alárendeltségeit egy listában tároljuk, és az eredményt a lista megfelelő szeletének kiírásával adjuk meg.

## A feladat megoldásának menete

### 1. Gráf építése

    tree = defaultdict(list)
    for i in range(n - 1):
      tree[bosses[i]].append(i + 2)  # Az alkalmazottak száma 2-től indul

- A **tree** egy szomszédsági listát tárol. Minden főnök (csomópont) a gyerekei (beosztottai) indexeire mutat.
- A bemenetben a főnökök listájából **(bosses[i])** tudjuk, hogy a $i+2$ csomópont melyik főnök alá tartozik.

**Példa bemenetre:**

$bosses = [1, 1, 2, 3]$

Ez azt jelenti, hogy:

- A 2-es és 3-as csomópontok 1 alá tartoznak.
- A 4-es csomópont 2 alá tartozik.
- Az 5-ös csomópont 3 alá tartozik.

Ez alapján a **tree** így néz ki:

    tree = {
      1: [2, 3],
      2: [4],
      3: [5]
    }

### 2. Rekurzív DFS

    def dfs(node, tree, subordinates):
        for child in tree[node]:
            subordinates[node] += dfs(child, tree, subordinates)  # Gyerekek alárendeltségeinek hozzáadása
        return subordinates[node] + 1  # Saját magát is számolja

A **dfs** függvény minden csomópont (**node**) esetén:

- Végigmegy az összes gyereken (**tree[node]**).
- Minden gyerekre meghívja magát rekurzívan, hogy számolja ki az adott gyerek alárendeltjeinek számát.
- Az összegzett eredményhez hozzáadja saját magát, és ezt visszaadja a szülő csomópontnak.

A számolt eredményeket a **subordinates** listában tároljuk.

### 3. DFS elindítása

    subordinates = [0] \* (n + 1) # Alárendeltségek tárolása, kezdetben minden csomópontnál 0
    dfs(1, tree, subordinates) # Rekurzió indítása az 1-es csomóponttal (gyökér)

- A **subordinates** listában indexenként tároljuk az alárendeltek számát.
- Az 1-es csomópont a gyökér, itt kezdjük a keresést.

### 4. Eredmények kiírása

    print(" ".join(map(str, subordinates[1:])))

- Az eredmény a **subordinates** lista $1$-től $n$-ig terjedő részében található. Ez az összes alkalmazott alárendeltségeit tartalmazza.

## Példa bemenet és futás

_Bemenet_

    5
    1 1 2 3

Kód futása

**1. Gráf építése:**

        tree = {
            1: [2, 3],
            2: [4],
            3: [5]
        }

**2. DFS kiszámítása:**

- **dfs(1):**
  - Bejárja a 2-es és 3-as csomópontokat.
  - **dfs(2):**
    - Bejárja a 4-es csomópontot.
    - **dfs(4)** visszaadja 1-et (nincs gyereke).
    - **dfs(2)** visszaadja 2-t (1 + 1 saját magát).
  - **dfs(3):**
    - Bejárja az 5-ös csomópontot.
    - **dfs(5)** visszaadja 1-et (nincs gyereke).
    - **dfs(3)** visszaadja 2-t (1 + 1 saját magát).
  - **dfs(1)** visszaadja 5-öt (2 + 2 + 1 saját magát).

**3. Alárendeltségek tárolása:**

    subordinates = [0, 4, 1, 1, 0, 0]

**4. Eredmény kiírása:**

_Kimenet_

    4 1 1 0 0

**Magyarázat**

- Az 1-es csomópontnak 4 alárendeltje van (2, 3, 4, 5).
- A 2-es és 3-as csomópontoknak egy-egy alárendeltje van (4 és 5).
- A 4-es és 5-ös csomópontoknak nincs alárendeltje.

## Összegzés

- A kód hatékonyan oldja meg a problémát $O(n)$ időben.
- A DFS stratégia természetesen illeszkedik a fa struktúrájához.
- A megoldás egyszerű, olvasható, és könnyen skálázható nagyobb bemenetekre is.
