# Analiza uzyskanych danych 
Z pośród dostępnych artrbutów `TenderType` oraz `procedureResult` wszędzie zawierały wartość NULL. Dodatkowo wszystkie przetargi w analizowanym zakresie posiadały taką samą wartość ????????? w kolumnie `isTenderAmountBelowEU`. W celu poprawy czytelnośći i integralności danych kolumny te zostały odrzucone.

# Analiza rozkładu przetargów
## CPV na dziedziny - co jest najpopularniejsze
## Top5 CPV - co jest dokładnie najpopularniejsze
## Top5 CPV w województwach - czy województwa wyglądają podobnie czy są jakieś zmiany?
## Top5 CPV overall w czasie - czy są zmiany najbardziej popularnych CPV? 
Czy we wszystkich województwach sytuacja się powtarza? Czy czasami są odstępstwa?+

# Analiza sezonowości rozkładu przetargów
Które dziedziny wykazują największe wahania, a jakie najmniejsze?

# Analiza rozkładu przetargów względem innych czynników
## Wstęp
Nie ma dostępnych danych udziału **miasta Warszawy** w ogólnym PKB kraju. Jedyne dostępne dane przedstawiają udział **Regionu Warszawskiego Stołecznego** według podziału **NUTS 2**. Przekształcenie danych uzyskanych z platformy eZamówienia na system **NUTS 2** mogłoby doprowadzić do złej alokacji jednostek samorządu terytorialnego ze względu na oryginalną strukturę danych zawierających `organizationProvince`, które przedstawia województwo zamawiającego oraz `organizationCity`, które przedstawia miejscowość zamawiającego. Ze względu na skalę wynikającą z ilości miejscowości wchodzących w skład **Regionu Warszawskiego Stołecznego**, a jednocześnie małą precyzyjność oryginalnych danych przedstawiających lokalizację przetargu w odniesieniu do uładu administracyjnego konwersja danych do formatu **NUTS 2** i wzbogacenie ich o dane odnośnie populacji w gmianch wchodzących w skład **Regionu Warszawskiego Stołecznego** obarczone jest zbyt dużym ryzykiem złej agregacji dancyh podczas procesu konwersji. 
W związku z powyższym jedynie podczas analizy korelacji ilości populacji do ilości przetargów możliwe było wyłączeniem miasta Warszawy jako osobnej jednostki.

## Przedstawienie wyników
### Liczba przetargów względem PKB województw
Liczba przetargów w województwie jest wysoce skorelowana ze wskaźnikiem PKB danego województwa.
Współczynnik Pearsona `r=0.974` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacji `R²=0.949` wskazuje, że model liniowy bardzo dobrze opisuje zróżnicowanie liczby przetargów w oparciu o PKB.
Na wykresie widać, że województwo **Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów jak i PKB, ale jest niemal idealnie w osi trendu.
### Liczba przetargów względem populacji województw
Liczba przetargów w województwach jest również wysoce skorelowana z ilością mieszkańców w danych województwie, lecz nie tak mocno jak w przypadku PKB.
Współczynnik Pearsona `r=0.953` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacji `R²=0.908` wskazuje, że model liniowy dobrze opisuje zróżnicowanie liczby przetargów w oparciu o populację.
Na wykresie widać, że również w tym przypadku **województwo Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów jak i ludności, lecz tym razem jest znacznie oddale od linii trendu w kierunku większej liczby przetargów na osobę niż pozostałe elementy zbioru.
### Liczba przetargów względem populacji województw z wykluczeniem Warszawy z województwa Mazowieckiego
Po odesparowaniu **miasta Warszawy** od reszty **województwa Mazowieckiego** ogólna korelacja spadła.
>Współczynnik Pearsona `r=0.874` oznacza 
>Współczynnik determinacji `R²=0.764` wskazuje, że

Pomimo tego, że korelacja spadła względem wykresu **Liczba przetargów względem populacji województw** na wykresie widać, że **województwo Mazowieckie** po wykluczeniu **miasta Warszawy** zbliżyło się do linii trendu oraz województwa zgromadzone są wokół linii trendu. Wyjąktiem pozostaje **miasto Warszawa**, które na tle zbioru wyróźnia się wysoką liczbą przetargów na osobę.
### Populacja względem PKB
W celu sprawdzenia zależności pomiędzy dwoma analizowanymi czynnikami stworzyłem wykres przedstawiający PKB województw w zestawieniu do populacji.
>Współczynnik Pearsona `r=0.951` oznacza 
>Współczynnik determinacji `R²=0.904` wskazuje, że

Liczba ludności rośnie w tym samym kierunku do PKB województwa. Warto zauważyć na tym wykresie również odmnienną pozycję **województwa Mazowieckiego**, którego PKB jest wyraźnie wyższe względem ludności niż w przypadku innych województw.
### Liczba przetargów względem PKB per capita
>Współczynnik Pearsona `r=0,880` oznacza 
>Współczynnik determinacji `R²=0.775` wskazuje, że

Pomimo realtywnie wysokich wartości współczynnika Pearsona i determinacji na wykresie widać znacznie większe rozproszenie elementów zbioru niż w poprzednich wykresach

# Podsumowanie
1. Opis danych
2. Opis popularności
3. Opis zmian w czasie
4. Czynniki zewnętrzne

# Wnioski
1. Do czego można wykorzystać badania i pracę?
2. Czy można przewidzieć co się będzie działo w przyszłości?
