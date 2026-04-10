# Analiza uzyskanych danych 
Z pośród dostępnych artrbutów możemy wyróżnic parę, które nie są wykorzystywane i wpływają negatywnie na czytelność danych.

# Analiza sezonowości rozkładu przetargów

# Analiza rozkładu przetargów względem dzedzin

# Analiza rozkładu przetargów względem innych czynników
## Wstęp
Nie ma dostępnych danych udziału **miasta Warszawy** w ogólnym PKB kraju. Jedyne dostępne dane przedstawiają udział **Regionu Warszawskiego Stołecznego** według podziału **NUTS 2**. Przekształcenie danych uzyskanych z platformy eZamówienia na system **NUTS 2** mogłoby doprowadzić do złej alokacji jednostek samorządu terytorialnego ze względu na oryginalną strukturę danych zawierających `organizationProvince`, które przedstawia województwo zamawiającego oraz `organizationCity`, które przedstawia miejscowość zamawiającego. Ze względu na skalę wynikającą z ilości miejscowości wchodzących w skład **Regionu Warszawskiego Stołecznego**, a jednocześnie małą precyzyjność oryginalnych danych przedstawiających lokalizację przetargu w odniesieniu do uładu administracyjnego konwersja danych do formatu **NUTS 2** i wzbogacenie ich o dane odnośnie populacji w gmianch wchodzących w skład **Regionu Warszawskiego Stołecznego** obarczone jest zbyt dużym ryzykiem złej agregacji dancyh podczas procesu konwersji. 
W związku z powyższym jedynie podczas analizy korelacji ilości populacji do ilości przetargów możliwe było wyłączeniem miasta Warszawy jako osobnej jednostki.

## Przedstawienie wyników
### Liczba przetargów względem PKB województw
Liczba przetargów w województwie jest wysoce skorelowana ze wskaźnikiem PKB danego województwa.
Współczynnik Pearsona `r=0.974` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacj `R²=0.949` wskazuje, że model liniowy bardzo dobrze opisuje zróżnicowanie liczby przetargów w oparciu o PKB.
Na wykresie widać, że województwo **Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów jak i PKB, ale jest niemal idealnie w osi trendu.
### Liczba przetargów względem populacji województw
Liczba przetargów w województwach jest również wysoce skorelowana z ilością mieszkańców w danych województwie, lecz nie tak mocno jak w przypadku PKB.
Współczynnik Pearsona `r=0.953` oznacza bardzo silną dodatnią korelację.
Współczynnik determinacj `R²=0.908` wskazuje, że model liniowy dobrze opisuje zróżnicowanie liczby przetargów w oparciu o populację.
Na wykresie widać, że również w tym przypadku województwo **Mazowieckie** wyraźnie odstaje od pozostałych elementów zbioru zarówno na osi reprezentującej liczbę przetargów jak i ludności, lecz tym razem jest znacznie oddale od linii trendu w kierunku większej liczby przetargów na osobę niż pozostałe elementy zbioru.
