""" L5/3
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

    Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
    Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.
 """

import sys
vstup=sys.argv[1]
print(vstup)

soubor=open("auta.txt",  encoding='utf-8')
radky=[x.strip().split() for x in soubor if x !="\n"]
soubor.close()

print(radky)
kilometry=[float(km[1].replace(",",".")) for km in radky]
print(f"total najetych km:{sum(kilometry)}")

# 1 to samé
import sys
vstup = sys.argv[1]
print(vstup)

soubor = open(vstup, encoding="utf-8") 
radky = [x.strip().split() for x in soubor if x != "\n"]
soubor.close()

print(radky)
kilometry = [float(km[1].replace(",", ".")) for km in radky]
print(f"total najetych km: {sum(kilometry)}")
