# Opis danych i wnioski
## Opis danych
1. Dane zawierały sporo błędów m.in.: <br>
    a) Ponad 200 000 zduplikowanych wierszy <br>
    b) Błędne współrzędne geograficzne <br>
    c) Błędne typy samochodów <br>
    d) Błędne powody wypadków <br>
    e) Brak dzielnic i kodów pocztowych w niektórych przypadkach <br>
    f) niepotrzebne białe znaki w nazwach ulic
2. Dane nie wskazują jednoznacznie kto jest sprawcą wypadku ani która przyczyna wypadku spowodowały zgon lub rany. <br>
3. Dzielnice przypisane do niektórych rekordów nie pokrywają się z ich współrzędnymi geograficznymi.
4. Do wyliczeń np. jakie jest najczęstszy powód wypadku, zastosowałem tzw. atrybucję wielokrotną tzn., <br>
Jeśli do danego id wypadku było przypisane 3 samochody i są również 3 powody wypadku i w ramach tego wypadku<br>
zginęła 1 osoba, to do wszystkich 3 powodów wypadku przypisane zostanie, że zginęła 1 osoba. Alternatywą byłaby <br>
tzw. atrybucja frakcyjna, jednakże w wypadku tych danych zdecydowałem się na pierwszą opcję.
## Wnioski
1. Około 60% wypadków ma przypisane nieokreślony powód wypadku. Pozostałe powody wypadków są mocno rozdrobione jedynie<br>
roztargnienie ma większy udział tzn. 12%. Pozostałe powody wypadków nie przekraczają 3%. W celu lepszego zrozumienia<br>
danych można w przyszłości zastosować grupowanie typów wypadku.
2. Wyliczając najniebezpieczniejsze powody urazów i zgonów, wyliczyłem według wzoru: <br>
suma zabitych lub rannych / suma liczby wypadków. <br>
Według tych wyliczeń najniebezpieczniejsze powody urazów to:<BR>
PEDESTRIAN/BICYCLIST/OTHER PEDESTRIAN ERROR/CONFUSION <BR>
UNSAFE SPEED	<BR>
TRAFFIC CONTROL DISREGARDED	<BR>
a najniebezpieczniejsze powody zgonów to: <br>
ILLNESS		<BR>
UNSAFE SPEED		<BR>
PEDESTRIAN/BICYCLIST/OTHER PEDESTRIAN ERROR/CONFUSION		<BR>
3. Najczęściej w wypadkach drogowych brały udział samochody z rodzajem: <br>
PASSENGER VEHICLE<br>
SPORT UTILITY / STATION WAGON<br>
SEDAN<br>
STATION WAGON/SPORT UTILITY VEHICLE<br>
4. Występują miejsca, w których ilość wypadków jest wysoka (powyżej 100 wypadków pod jednymi współżędnymi), ale<br>
odpowiadają ona za nie wielką ilość wypadków (około 6,5%). Miejsca, gdzie było, od 1 do 10 wypadków odpowiadają za<br>
około 25% wszystkich wypadków.