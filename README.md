# KalendarzDlaSmieci
Jest to program w języku Python, który generuje plik kalendarza z wydarzeniami dotyczącymi wywozu śmieci.
<br /><br />
Oprócz samego programu w języku Python dołączony jest także skrypt .bat pozwalący uruchomić program w systemie Windows oraz 3 puste pliki tekstowe dla odpowiednich typów śmieci.<br />
* Dom_Bio.txt - pusty plik do wypełnienia datami dla odpadów zielonych
* Dom_Pet.txt - pusty plik do wypełnienia datami dla odpadów typu papier, szkło, metale i tworzywa sztuczne
* Dom_Smieci.txt - pusty plik do wypełnienia datami dla odpadów zmieszanych
# Windows
W celu uruchomienia programu należy zainstalować aplikację Python ze sklepy Microsoft Store.<br />
# Instukcja dotycząca plików tekstowych
* Każda linijka pliku tekstowego to miesiąc, czyli 5 linijka to maj.
* Liczby oddzielamy spacjami.
* Np. 2 18 30
* Np. 2(spacja)18(spacja)30
* Na końcu nie zostawiamy spacji ani linii.
<br /><br />
# Edycja
W celu personalizacji generowanego kalendarza należy:
* Utworzyć nowy lub zmienić nazwę plików tekstowych
* Otworzyc plik z rozszerzeniem .py w programie do edycji tekstu
* Zmienić f2 = open("Dom_Pet.txt", "r") np. na f2 = open("Makulatura.txt", "r")
* Zmienić addToFile("Dom Pet",f2,rok) na addToFile("Makulatura",f2,rok)
* f0, f1, f2... to odpowienie zmienne do plików, które nie mogą się powtarzać, a f0 to plik generowanego kalendarza
<!-- end of the list -->
<br />
Po zaimportowaniu kalendarza należy pamiętać o ustawieniu powiadomień.
