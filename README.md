# bootstrap.py

## A program funkciója

A program képes párhuzamosan több adathalmazt párhuzamosan bármekkora mennyiségben bootstrapelni, a bemenetet és kimenetet szabadon változtatni.

## Használat

A program egy .csv fájlt vár el bemenetként, aminek az alapértelmezett neve input.csv, a kimenetet pedig az output.csv fájl tartalmazza. A program soronként kezeli az adathalmazt.

A bemenet és kimenet opciókat az `-i:fájlnév`, illetve az `--Input=fájlnév`, valamint az `-o:fájlnév` és `--Output=fájlnév` flagekkel lehet állítani.

Ezen kívül elérhető a `-h`/`--Help` flag, ami ennek az összefoglalónak a kompakt verziója.

A program a bemenet sikeres megnyitása és olvasása után kéri a felhasználótól az új adathalmaz méretét. Ezután több interakcióra nincs szükség.