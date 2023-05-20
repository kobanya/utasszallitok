Utasszállító repülőgépek
A két világháború közötti időszak volt a repülés hőskora. 1933-ban a Boeing cég készítette
247-es gép volt a világ első modern utasszállító repülője, melynek közel 300 km/h lett a
csúcssebessége, vagyis gyorsabb volt, mint a kor legtöbb harci repülője. Ebben a feladatban az
1950-1990 között nagyobb darabszámban gyártott utasszállító repülőgéptípusok adataival1 kell
feladatokat megoldania. Megoldásában vegye figyelembe a következőket: <br>
• A képernyőre írást igénylő feladatok eredményének megjelenítése előtt írja a képernyőre a
feladat sorszámát (például: 4. feladat)! <br><br>
• Az egyes feladatokban a kiírásokat a minta szerint készítse el!<br>
• Az ékezetmentes kiírások is elfogadottak.<br>
• Az azonosítókat kis- és nagybetűkkel is kezdheti.<br>
• A program megírásakor az állományban lévő adatok helyes szerkezetét nem kell 
ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.<br>
• A megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemeneti adatok
mellett is helyes eredményt adjon. <br>
Az UTF-8 kódolású utasszallitok.txt forrásállomány tartalmazza soronként a
repülőgéptípusok adatait, melyeket pontosvesszővel választottuk el:
• típus: A repülőgéptípus neve, szöveges, például: Airbus A300<br>
• év: Az első repülés éve, egész, például: 1972<br>
• utas: Szállítható utasok száma, szöveges, például: 218 vagy 150-179 <br>
• személyzet: Személyzet létszáma, szöveges, például: 3 vagy 4-5<br>
• utazósebesség: Utazósebesség [km/h], egész, például: 911<br>
• felszállótömeg: Felszállótömeg [kg], egész, például: 142000<br>
• fesztáv: Fesztáv [m], valós, például: 44,84 <br><br>
1. Készítsen konzolos alkalmazást a következő feladatok megoldására, melynek projektjét
Utasszallitok néven mentse el!<br>
2. Forráskódjában tegye elérhetővé a java.txt vagy a csharp.txt állományból a
Sebessegkategoria osztályt definiáló kódrészletet!<br>
......................................... osztály:......<br>
3. Olvassa be az utasszallitok.txt állományban lévő adatokat és tárolja el egy olyan
adatszerkezetben, ami a további feladatok megoldására alkalmas! Az állományban
legfeljebb 100 sor lehet. Tárolja el minden repülőgéptípushoz a sebességkategória adatot
(elég szöveges típusú adatként) az előző feladatban elérhetővé tett osztály használatával!
Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza és a fesztáv valós típusú
adatban az egész és a tört rész elválasztásához vessző karaktert használtunk a forrásban.<br>
4. Határozza meg és írja ki a képernyőre a forrásállományban lévő adatsorok 
(repülőgéptípusok) darabszámát!<br>
5. Határozza meg és írja ki a képernyőre a Boeing vállalat által gyártott repülőgéptípusok
darabszámát! Feltételezheti, hogy minden általuk gyártott típus neve a „Boeing”
szórészlettel kezdődik. <br>
6. Határozza meg azt a repülőgéptípust, amely a legtöbb utas szállítására volt alkalmas! Ha az
utasok száma „tól-ig” formában (például: 150-179) van megadva, akkor mindig az „ig”
értéket használja az összehasonlításnál! A típus adatait a feladat végén található minta szerint
írja a képernyőre! Feltételezheti, hogy nem alakult ki az élen holtverseny!<br>
7. Határozza meg, hogy melyik sebességkategóriából nem található repülőgéptípus a
forrásállományban! A sebességkategória neveket ennek
a Sebessegkategoria
osztályban
az oldalnak az alján találja!
találja. Ha több sebességkategóriából nincs repülőgéptípus, akkor a kategórianeveket
szóközzel elválasztva írja a képernyőre egymás mellé. Ha minden sebességkategóriából
található repülőgéptípus, akkor a „Minden sebességkategóriából van repülőgéptípus.”
szöveg jelenjen meg!<br>
8. Készítsen utasszallitok_new.txt néven szöveges állományt a feladat végén található
minta szerint, melynek szerkezete, fejlécsora és adattartalma megegyezik az
utasszallitok.txt állományéval, a következő különbségekkel: <br>
a. Az utasok számánál „tól-ig” érték esetén csak az „ig” érték kerüljön az új állományba.<br>
b. A személyzet számánál is a „tól-ig” érték esetén csak az „ig” érték kerüljön az
állományba.<br>
c. A felszállótömeg tonnában kifejezve, tetszőleges módszerrel egész értékre kerekítve
kerüljön az adatsorokba. (1 kg = 0,001 t).<br>
d. A fesztávolság láb mértékegységgel kifejezve, tetszőleges módszerrel egész értékre
kerekítve kerüljön az adatsorokba. (1 m = 3,2808 láb)<br>
9. Készítsen grafikus alkalmazást, melynek a projektjét MachKalkulatorGUI néven mentse
Sebességkategóriák<br>
el, melynek segítségével egy repülőgép Pitot-cső rendszerű nyomásérzékelő műszerével
mért nyomásadatok alapján a Mach-számot határozhatjuk meg szubszonikus sebesség
2
if esetén!
(Utazosebesseg
< 500)
--> "Alacsony sebességű";
else if (Utazosebesseg < 1000) --> "Szubszonikus";
else if (Utazosebesseg < 1200) --> "Transzszonikus";
else
--> "Szuperszonikus"