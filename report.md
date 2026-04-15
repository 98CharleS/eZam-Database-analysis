# Dane wejściowe
Analizie poddano dane pobrane z portalu [eZamówienia BZP](https://ezamowienia.gov.pl/mo-client-board/bzp) 
za pomocą API ([eZam-Database-extraction](https://github.com/98CharleS/eZam-Database-extraction)), 
które zostały następnie sformatowane i opracowane 
([eZam-Database-formating](https://github.com/98CharleS/eZam-Database-formating)) 
w celu uzyskania standaryzacji, czytelności i możliwości obsługi w innych programach.
Zbiór danych liczy 517 840 elementów i obejmuje przetargi z okresu 01.01.2020–31.12.2025.
# Omówienie i analiza uzyskanych danych 
Z pośród dostępnych artrbutów `TenderType` oraz `procedureResult` wszędzie zawierały wartość NULL. Dodatkowo wszystkie przetargi w analizowanym zakresie posiadały taką samą wartość ????????? w kolumnie `isTenderAmountBelowEU`. W celu poprawy czytelnośći i integralności danych kolumny te zostały odrzucone.

# Analiza rozkładu przetargów
## Wstęp
W pobranych danych w kolumnie `cpvCode` znajdowało się wiele kodów CPV. Wynika to z charakterystyki struktury ogłoszeń o przetargach, gdzie wstępuje jeden główny kod CPV, następnie może występować wiele dodatkowych kodów CPV, których kluczowość dla całości przedmiotu przetargu może być zróżnicowana. 
Ze względu na to, że niemożliwa jest ocena istotności dodatkowego kodu CPV dla całości przetargu, a różna liczba dodatkowych kodów zaburzyłaby statystykę częstotliwości w odniesieniu do liczby przetargów, analizie poddano wyłącznie główny kod CPV dostępny w atrybutach każdego wpisu. Przyjęte podejście zapewnia standaryzację, spójność i czytelność wyników.
## CPV na dziedziny - co jest najpopularniejsze
## Top5 CPV - co jest dokładnie najpopularniejsze
## Top5 CPV w województwach - czy województwa wyglądają podobnie czy są jakieś zmiany?


# Analiza sezonowości rozkładu przetargów
## Top5 CPV overall w czasie - czy są zmiany najbardziej popularnych CPV? 
Czy we wszystkich województwach sytuacja się powtarza? Czy czasami są odstępstwa?+
## 1. Jak zmienia się ogólna liczba w czasie
## 2. Które dziedziny wykazują największe wahania, a jakie najmniejsze?

# Analiza rozkładu przetargów względem innych czynników
## Wstęp
Nie ma dostępnych danych udziału **miasta Warszawy** w ogólnym PKB kraju. Jedyne dostępne dane przedstawiają udział **Regionu Warszawskiego Stołecznego** według podziału **NUTS 2**. Przekształcenie danych uzyskanych z platformy eZamówienia na system **NUTS 2** mogłoby doprowadzić do złej alokacji jednostek samorządu terytorialnego ze względu na oryginalną strukturę danych zawierających `organizationProvince`, które przedstawia województwo zamawiającego, oraz `organizationCity`, które przedstawia miejscowość zamawiającego. Ze względu na skalę wynikającą z ilości miejscowości wchodzących w skład **Regionu Warszawskiego Stołecznego**, a jednocześnie małą precyzyjność oryginalnych danych przedstawiających lokalizację przetargu w odniesieniu do układu administracyjnego, konwersja danych do formatu **NUTS 2** i wzbogacenie ich o dane odnośnie do populacji w gminach wchodzących w skład **Regionu Warszawskiego Stołecznego** obarczone jest zbyt dużym ryzykiem złej agregacji danych podczas procesu konwersji.
W związku z powyższym jedynie podczas analizy korelacji liczby ludności do liczby przetargów możliwe było wyłączenie miasta Warszawy jako osobnej jednostki.

## Analiza danych
### Liczba przetargów względem PKB województw
Liczba przetargów w województwie jest wysoce skorelowana ze wskaźnikiem PKB danego województwa.
Współczynnik Pearsona `r=0.974` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacji `R²=0.949` wskazuje, że model liniowy bardzo dobrze opisuje zróżnicowanie liczby przetargów w oparciu o PKB.
Na wykresie widać, że województwo **Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów, jak i PKB, lecz jest niemal idealnie na linii trendu.

### Liczba przetargów względem populacji województw
Liczba przetargów w województwach jest również wysoce skorelowana z liczbą mieszkańców danego województwa, lecz nie tak mocno jak w przypadku PKB.
Współczynnik Pearsona `r=0.953` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacji `R²=0.908` wskazuje, że model liniowy dobrze opisuje zróżnicowanie liczby przetargów w oparciu o populację.
Na wykresie widać, że również w tym przypadku **województwo Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów, jak i liczbę ludności, lecz tym razem jest znacznie oddalone od linii trendu w kierunku większej liczby przetargów na osobę niż pozostałe elementy zbioru.

### Liczba przetargów względem populacji województw z wykluczeniem Warszawy z województwa Mazowieckiego
Po odseparowaniu **miasta Warszawy** od reszty **województwa Mazowieckiego** ogólna korelacja spadła.
Współczynnik Pearsona `r=0.874` oznacza silną dodatnią korelację, choć wyraźnie słabszą niż przy pełnych danych **województwa Mazowieckiego**.
Współczynnik determinacji `R²=0.764` wskazuje, że model liniowy wyjaśnia około 76% zmienności liczby przetargów w oparciu o populację — jest to spadek o ponad 14 punktów procentowych względem analizy bez podziału **województwa Mazowieckiego**.
Pomimo tego, że korelacja spadła względem wykresu **Liczba przetargów względem populacji województw**, na wykresie widać, że **województwo Mazowieckie** po wykluczeniu **miasta Warszawy** zbliżyło się do linii trendu, a pozostałe województwa skupiają się wokół niej. Wyjątkiem pozostaje **miasto Warszawa**, które na tle zbioru wyróżnia się wysoką liczbą przetargów na osobę.

### Populacja względem PKB
W celu sprawdzenia zależności pomiędzy dwoma analizowanymi czynnikami stworzono wykres przedstawiający PKB województw w zestawieniu z populacją.
Współczynnik Pearsona `r=0.951` oznacza bardzo silną dodatnią korelację między PKB a liczbą ludności województw.
Współczynnik determinacji `R²=0.904` wskazuje, że ponad 90% zmienności PKB można wyjaśnić samą liczbą mieszkańców, co potwierdza, że obie zmienne są silnie współzależne i nie stanowią niezależnych predyktorów liczby przetargów.
Liczba ludności rośnie w tym samym kierunku co PKB województwa. Warto zauważyć na tym wykresie również odmienną pozycję **województwa Mazowieckiego**, którego PKB jest wyraźnie wyższe względem liczby ludności niż w przypadku innych województw.

### Liczba przetargów względem PKB per capita
Współczynnik Pearsona `r=0.880` oznacza silną dodatnią korelację, jednak niższą niż w przypadku PKB absolutnego.
Współczynnik determinacji `R²=0.775` wskazuje, że model liniowy wyjaśnia około 78% zmienności liczby przetargów — wynik gorszy niż dla PKB całkowitego, co sugeruje, że sama zamożność per capita jest słabszym predyktorem aktywności przetargowej niż skala gospodarcza regionu.
Pomimo relatywnie wysokich wartości **współczynnika Pearsona i determinacji**, na wykresie widać znacznie większe rozproszenie elementów zbioru niż w poprzednich wykresach.

# Podsumowanie
1. Opis danych
2. Opis popularności
3. Opis zmian w czasie
4. Czynniki zewnętrzne
PKB jest najlepszym czynnikiem, na podstawie którego można przewidzieć liczbę przetargów. Wysoka korelacja liczby przetargów z PKB oznacza, że regiony o silniejszej gospodarce regionalnej generują więcej przetargów. Jest to logiczna zależność, lecz pokazuje, że aktywność przetargowa w Polsce pozostaje silnie skoncentrowana w najbardziej rozwiniętych gospodarczo regionach. Może to świadczyć o utrzymujących się dysproporcjach regionalnych pomimo licznych programów, takich jak **Program Operacyjny Polska Wschodnia 2014–2020 (PO PW)**, **Fundusze Europejskie dla Polski Wschodniej 2021–2027 (FEPW)** oraz **Regionalne Programy Operacyjne (RPO)** finansowane z funduszy UE, które miały na celu wyrównywanie dysproporcji rozwojowych między województwami.
Tezę o utrzymującej się koncentracji aktywności przetargowej potwierdzają wykresy liczby przetargów do liczby ludności, na których widać liniowy wzrost liczby przetargów wraz z liczbą ludności. Wyjątkiem pozostaje **miasto Warszawa**, które generuje znacznie więcej przetargów na osobę, niż wynikałoby to z trendu. Widać to dokładnie w zawyżonym wyniku **województwa Mazowieckiego** na wykresie drugim oraz na wykresie trzecim z wydzielonym **miastem Warszawa**, którego wartość dopasowania modelu (`R²=0.764`) jest o ponad 18 punktów procentowych niższa niż wykresu z całym **województwem Mazowieckim** (`R²=0.949`).
Anomalię związaną z zawyżonym wynikiem **województwa Mazowieckiego** widać również na wykresie czwartym, a dobitnie na wykresie piątym, gdzie pozostałe województwa reprezentują podobny poziom liczby przetargów i PKB per capita, skupiając się w lewym dolnym rogu, podczas gdy **województwo Mazowieckie** znajduje się odizolowane w przeciwnym. Słabsze dopasowanie modelu na wykresie piątym pokazuje, że sama zamożność per capita nie jest dobrym predyktorem liczby przetargów — liczy się przede wszystkim bezwzględna skala gospodarcza regionu.
W celu lepszego zbadania zasadności korelacji liczby przetargów z PKB należałoby wyłączyć **miasto Warszawę** lub **Warszawski Region Stołeczny** z **województwa Mazowieckiego**, co z przyczyn wyjaśnionych we wstępie nie zostało wykonane.

# Wnioski
1. Do czego można wykorzystać badania i pracę?
2. Czy można przewidzieć co się będzie działo w przyszłości?
