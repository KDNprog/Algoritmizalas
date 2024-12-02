# Apartmanok kiosztása - Feladat megoldása

**Megoldási stratégia:**

- Rendezzük a pályázók és a lakások méreteit növekvő sorrendbe!
- Kezdjük el bejárni mindkét listát!
  - Ha a jelenlegi lakás mérete az elfogadható tartományba esik, párosítsuk őket, és lépjünk a következő pályázóra és lakásra!
  - Ha a lakás túl kicsi, lépjünk a következő lakásra!
  - Ha a pályázó túl nagy méretű lakást kíván, lépjünk a következő pályázóra!
- Folytassuk, amíg az egyik lista végére nem érünk!

## A mohó stratégia

A mohó algoritmusok alapelve, hogy minden lépésben az aktuális helyzet alapján a lehető legjobb döntést hozzák meg, anélkül hogy későbbi lépésekre tekintettel lennének.

**_Miért jó ehhez a feladathoz a mohó stratégia?_**

1. **Döntési szabály**:
   - Minden pályázónál a lehető legkisebb, de elfogadható méretű lakást választjuk ki.
   - Ez azért előnyös, mert így maximalizáljuk annak az esélyét, hogy a további pályázók számára is marad elfogadható lakás.
2. **Egyszerű párosítás**:
   - Ha egy lakás nem felel meg a jelenlegi pályázónak, akkor az algoritmus továbbhalad a következő pályázóra vagy lakásra, és nem tér vissza az előző döntésekhez.
3. **Optimalitás a lokális döntésekből**:
   - A döntések lokálisan optimálisak (minden pályázó a neki leginkább megfelelő szabad lakást kapja), és ez globálisan is a legtöbb pályázó kielégítését eredményezi.

**Példák a mohó döntésekre:**

- Ha egy lakásméret pontosan megfelel egy pályázó kívánságának, azt azonnal kiosztjuk (nem halogatjuk a döntést, mert más pályázónak nem biztos, hogy ugyanaz a lakás megfelelne).
- Ha egy lakásméret túl nagy vagy túl kicsi egy pályázó számára, az algoritmus továbbhalad, mert az adott lakás nem járulhat hozzá a célhoz.

**_Miért működik jól a mohó stratégia itt?_**

A probléma szerkezete olyan, hogy a mohó döntések optimalitáshoz vezetnek:

- A pályázók és lakások sorrendbe állítása biztosítja, hogy a legkisebb elfogadható lakást párosítjuk a pályázóval.
- Egy pályázó elfogad egy lakást, ha az méretben megfelel, így a párosítások száma maximalizálható anélkül, hogy más lehetőségeket kihasználatlanul hagynánk.

## A feladat megoldásának menete

### 1. Bemenet beolvasása

_Bemenet:_

    n, m, k = map(int, input().split())

Mit jelent ez?

- **n**: a pályázók száma.
- **m**: a lakások száma.
- **k**: a megengedett méretkülönbség (tolerancia).

Ezeket egyetlen sorból olvassuk be, és egész számokká alakítjuk.

    applicants = list(map(int, input().split()))
    apartments = list(map(int, input().split()))

Mit jelent ez?

- A második sorban a pályázók által kívánt lakásméretek **(applicants)** találhatók.
- A harmadik sorban a lakások tényleges méretei **(apartments)** találhatók.
- A **map(int, input().split())** minden számot egy listába helyez, amelyeket egész számokká alakítunk.

### 2. Adatok előkészítése

    applicants.sort()
    apartments.sort()

Mit csinál ez?

- A pályázók kívánságait **(applicants)** és a lakások méreteit **(apartments)** növekvő sorrendbe rendezi.
- Ez szükséges ahhoz, hogy a két lista elemein hatékonyan végighaladjunk egyetlen menetben.

### 3. Kezdeti változók beállítása

    i = j = matches = 0

Mit jelent ez?

- **i**: index a pályázók listájában.
- **j**: index a lakások listájában.
- **matches**: az eddig megtalált párosítások száma.

### 4. Lakások és pályázók párosítása

    while i < n and j < m:

Mit csinál ez?

- Amíg vannak feldolgozatlan pályázók ($i<n$) és lakások ($j<m$), az algoritmus folytatódik.
- Ez biztosítja, hogy az algoritmus ne lépjen ki a listák határain túl.

**4.1. Elfogadható párosítás keresése**

    if abs(applicants[i] - apartments[j]) <= k:

- Ellenőrzi, hogy a jelenlegi pályázó **(applicants[i])** és a lakás **(apartments[j])** méretkülönbsége **k**-n belül van-e.

_Ha igen:_

    matches += 1
    i += 1
    j += 1

- Növeli a párosítások számát **(matches)**.
- Továbblép a következő pályázóra **(i)** és lakásra **(j)**.

**4.2. Amikor a pályázó túl kicsi méretet kíván**

    elif applicants[i] < apartments[j] - k:
        i += 1

- Ha a pályázó által kívánt lakásméret ($applicants[i]$) túl kicsi ahhoz, hogy bármely lakást elfogadhasson ($apartments[j]−k$):
  - Csak a pályázók listájában lép tovább ($i+ =1$).

**4.3. Amikor a lakás túl kicsi a pályázónak**

    else:
        j += 1

- Ha a jelenlegi lakás mérete ($apartments[j]$) túl kicsi a pályázó számára:
  - Csak a lakások listájában lép tovább ($j+=1$).

### 5. Eredmény kiíratása

    print(matches)

Mit csinál ez?

- Kiírja a találatok (párosítások) számát.

## Példa működés közben

_Bemenet:_

    4 3 5
    60 45 80 60
    30 60 75

**Rendezett adatok:**

- $applicants=[45,60,60,80]$
- $apartments=[30,60,75]$

**Algoritmus menete:**

- **Kezdés**: $i=0,j=0,matches=0$

  - $∣45−30∣>5 → j+=1$

- **Most**: $i=0,j=1$
  - $∣45−60∣≤5 → matches=1,i+=1,j+=1$
- **Most**: $i=1,j=2$
  - $∣60−75∣≤5 → matches=2,i+=1,j+=1$
- **Most**: $i=2,j=3$
  - Lakások elfogytak → vége.

**Eredmény:** $matches=2$

### 6. Időbonyolultság

- **Rendezés**: $O(n\log ⁡n + m\log ⁡m)$

- **Párosítás keresése**: $O(n + m)$

- **Teljes**: $O(n\log ⁡n + m\log ⁡m)$

**_Miért működik hatékonyan?_**

A rendezés miatt az algoritmus mindig a legkisebb aktuálisan elfogadható párosításokat keresi, és egyetlen átfutással megoldja a feladatot, ezért hatékony és egyszerű.
