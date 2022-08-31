# bootstrap.py

## A program funkciója

A program képes párhuzamosan több adathalmazt párhuzamosan bármekkora mennyiségben bootstrapelni, a bemenetet és kimenetet szabadon változtatni.

## Használat

A program egy pontosvesszővel elválaszott .csv fájlt vár el bemenetként, a kimenet ugyanilyen formájú. A program soronként kezeli az adathalmazt.

A bemeneti fájl nevét a program futás közben kéri a felhasználótól, a kimeneti fájl neve pedig *bemenet*_rep_*méret*.csv formátumú.

A bemeneti fájl első oszlopa azonosítókból állhat, ezeket a program nem változtatja. A fájlban az adatok csak egész számok lehetnek.

Ezen kívül elérhető a `-h`/`--Help` flag, ami ennek az összefoglalónak a kompakt verziója.

A `-d`/`--Debug` flag diagnosztikai üzeneteket jelenít meg a program futása közben

A program a bemenet sikeres megnyitása és olvasása után kéri a felhasználótól az új adathalmaz méretét. Ezután több interakcióra nincs szükség.

## Dependencies

A felhasznált csomagok:

- numpy
- matplotlib.pyplot

pip segítségével telepíthetők: `pip install numpy`

A matplotlib.pyplot csomag a végső programban nem szerepel, a fejlesztéshez és ellenőrzéshez használtam.

## Forráskód szerkesztése

A kész program forráskódja a [final](./final/) könyvtárban elérhető python file, de a repository tartalmazza a [source](./source/) mappában a fejlesztéshez és ellenőrzéshez használt fájlokat, és fejléceket is.

## Licenszek

A numpy 3 pontos BSD licensszel van publikálva, ez a program pedig GNU GPLv3 licensszel. További információ a dokumentációban található.