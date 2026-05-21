# Dane wejściowe
Analizie poddano dane pobrane z portalu [eZamówienia BZP](https://ezamowienia.gov.pl/mo-client-board/bzp) 
za pomocą API ([eZam-Database-extraction](https://github.com/98CharleS/eZam-Database-extraction)), 
które zostały następnie sformatowane i opracowane 
([eZam-Database-formating](https://github.com/98CharleS/eZam-Database-formating)) 
w celu uzyskania standaryzacji, czytelności i możliwości obsługi w innych programach.
Zbiór danych liczy 517 840 elementów i obejmuje przetargi z okresu 01.01.2020–31.12.2025.
# Omówienie i analiza uzyskanych danych 
Z pośród dostępnych artrbutów `TenderType` oraz `procedureResult` wszędzie zawierały wartość NULL. Są to atrybuty, które w bazie danych pozostają nieużywane. Dodatkowo wszystkie przetargi w analizowanym zakresie posiadały taką samą wartość `True` w kolumnie `isTenderAmountBelowEU`. Wartość tego atrybutu określa czy wartość przetargu była poniżej wartości **[progu Unijnego](https://www.gov.pl/web/uzp/aktualne-progi-unijne-oraz-ich-rownowartosci-w-zlotych-na-lata-2026-2027)**. Same wartości `True` oznaczają, że wszystkie przetargi z analizowanego zbioru były poniżej **progu Unijnego**.  W celu poprawy czytelnośći i integralności danych, wyżej wspomniane kolumny zostały odrzucone.

# Analiza rozkładu przetargów
## Wstęp
W pobranych danych w kolumnie `cpvCode` znajdowało się wiele kodów CPV. Wynika to z charakterystyki struktury ogłoszeń o przetargach, gdzie wstępuje jeden główny kod CPV, następnie może występować wiele dodatkowych kodów CPV, których kluczowość dla całości przedmiotu przetargu może być zróżnicowana. 
Ze względu na to, że niemożliwa jest ocena istotności dodatkowego kodu CPV dla całości przetargu, a różna liczba dodatkowych kodów zaburzyłaby statystykę częstotliwości w odniesieniu do liczby przetargów, analizie poddano wyłącznie główny kod CPV dostępny w atrybutach każdego wpisu. Przyjęte podejście zapewnia standaryzację, spójność i czytelność wyników.

## Analiza rozkładu kodów CPV

<img width="2117" height="1314" alt="image" src="https://github.com/user-attachments/assets/4655b18d-7fd7-4c8f-9918-7c6096da2900" />

W analizowanej bazie danych wystepuje **5047** kodów CPV. Widoczna jest bardzo duża dysproporcja pomiędzy liczbą przetargów podlegająych pod poszczególne kody CPV. **51,79%** wszystkich kodów CPV wystąpiło **mniej niż 10 razy** w bazie danych, **mniej niż 100 razy** wystąpiło aż **87,18%** kodów CPV, a **mniej niż 1 000 razy** wystąpiło aż **98,18%** zbioru. 
Wszystkie kody CPV, które stanowią w zbiorze 1% lub więcej przedstawia poniższa tabela:

| Kod CPV | Nazwa | Liczba przetargów | Udział % |
|---------|-------|-------------------|----------|
| **45000000-7** | Roboty budowlane | 58 906 | **11,38%** |
| 45200000-8 | Roboty drogowe | 9 423 | 1,82% |
| 45231000-6 | Roboty w zakresie budowy dróg | 9 148 | 1,77% |
| 71200000-3 | Usługi inżynierskie w zakresie projektowania | 8 356 | 1,61% |
| 79700000-3 | Usługi ochroniarskie | 6 220 | 1,20% |
| 45300000-9 | Roboty remontowe i renowacyjne | 5 944 | 1,15% |
| 45243000-0 | Roboty w zakresie nawierzchni dróg | 5 160 | 1,00% 

Najpopularniejszy kod CPV - "**45000000-7 Roboty budowlane**" wystąpił jako główny kod CPV w **58 906** przetargach co stanowiło **11,38%** wszystkich przetargów ze zbioru. Następny najpopularniejszy kod **45200000-8 Roboty drogowe** wystąpił w **9 423** przetargach co było liczbą ponad **6-krotnie mniejszą**. Różnice pomiędzy ilościami przetargów z danymi kodami CPV maleją wraz ze spadkiem liczby przetargów.
Taki rozkład danych świadczy o tym, że zbiór charakteryzuje się rozkładem silnie prawoskośnym z długim ogonem.

## Analiza rozkładu działów przetargów

**Kody CPV** są dokładnym przedstawieniem tematyki przetargu, lecz ze względu szczegółówość jest ich bardzo wiele i dzielą wszystkie przetargi na wąskie zakresy, które są ciężkie do przedstawienia wizualnego i generalizacji. Dla uproszczenia **kody CPV zaagregowano w 45 działów** obejmujące szerszy zakres. Działy przyjęto zgodnie z obowiązującym podziałem wynikającym z [Rozporządzenie Komisji (WE) nr 213/2008 z dnia 28 listopada 2007 r ](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32008R0213).

<img width="2114" height="1306" alt="image" src="https://github.com/user-attachments/assets/ea3247d3-7a2c-4988-bc0a-b1541c2fec86" />

10 najliczniejszych działów przedstawia poniższa tabela:

| Kod | Nazwa | Liczba przetargów | Udział % |
|-----|-------|-------------------|----------|
| **45** | Roboty budowlane | 167 010 | **32,25%** |
| 33 | Sprzęt medyczny i farmaceutyczny | 39 843 | 7,69% |
| 71 | Usługi architektoniczne i inżynieryjne | 31 379 | 6,06% |
| 90 | Usługi środowiskowe i sanitarne | 23 543 | 4,55% |
| 15 | Artykuły spożywcze i napoje | 22 319 | 4,31% |
| 9 | Produkty naftowe, paliwa i energia | 20 268 | 3,91% |
| 34 | Sprzęt transportowy i pojazdy | 19 757 | 3,82% |
| 30 | Sprzęt komputerowy i biurowy | 19 462 | 3,76% |
| 79 | Usługi biznesowe i doradcze | 15 855 | 3,06% |
| 39 | Meble i wyposażenie wnętrz | 14 948 | 2,89% |

Najwięcej przetargów dotyczyło działu **Roboty budowlane**, który skupiał **32,25%** wszystkich przetargów i stanowił wyraźnego lidera zestawienia. Potwierdza to obserwacje z poprzedniej analizy, w której **kody CPV** związane z robotami budowlanymi również dominowały pod względem liczebności. Pomiędzy pierwszym a drugim miejscem wystąpiła istotna dysproporcja – kolejny dział, **Sprzęt medyczny i farmaceutyczny**, skupiał **7,69%** przetargów, co oznacza, że był **4,19-krotnie mniej liczny niż lider**. Różnica ta, choć znacząca, jest wyraźnie mniejsza niż analogiczna dysproporcja zaobserwowana na poziomie pojedynczych **kodów CPV**, gdzie lider przewyższał następnika ponad 6-krotnie.
Dalsze pozycje rankingu zajmowały działy: **Usługi architektoniczne i inżynieryjne (6,06%), Usługi środowiskowe i sanitarne (4,55%)** oraz **Artykuły spożywcze i napoje (4,31%)**. Różnice pomiędzy kolejnymi działami w tej części zestawienia są już znacznie mniejsze i stopniowo maleją wraz ze spadkiem liczby przetargów. Działy zajmujące pozycje od 6. do 10. – **Produkty naftowe, paliwa i energia, Sprzęt transportowy i pojazdy, Sprzęt komputerowy i biurowy, Usługi biznesowe i doradcze oraz Meble i wyposażenie wnętrz –** skupiały odpowiednio od **3,91% do 2,89%** przetargów, tworząc relatywnie zwartą grupę o zbliżonych udziałach.
Zjawisko mniejszego rozwarstwienia wynika z naturalnego efektu agregacji – grupowanie kodów CPV w działy niweluje ekstremalne różnice widoczne przy bardziej szczegółowym poziomie klasyfikacji. Rozkład tych danych również wykazuje charakter silnie prawoskośny z długim ogonem, co oznacza, że zdecydowana większość przetargów koncentruje się w nielicznych działach, podczas gdy pozostałe kategorie – w tym **Usługi związane z przemysłem naftowym** z zaledwie 18 przetargami – stanowią marginalny udział w zbiorze.

W dalszej analize stosowany będzie podział zarówno na **działy jak i kody CPV** w zależności od indywidualnej szczegółowści analizowanego zagadeniania.

## Róznice pomiędzy województwami

### Najpopularniejsze kody w województwach

<img width="1106" height="724" alt="obraz" src="https://github.com/user-attachments/assets/0305f33c-e0e2-46fe-ac50-f6f182213e22" />
<img width="809" height="424" alt="obraz" src="https://github.com/user-attachments/assets/239a2ee7-1d66-4157-a0f3-75dfe94cad87" />

We wszystkich województwach najliczniejszym **kodem CPV** były **Roboty budowlane**, które stanowiły od 51,5% do aż 69,9% wszystkich przetargów z grupy 5 najliczniejszych i skupiły łącznie 58 906 przetargów.
Następnym pod względem liczebności jest **kod CPV Budowa dróg**, który w pozycjach od 2 do 5 wystąpił w 11 z 16 województw skupiając łącznie 7427 przetargów. Zaraz za tym kodem wystąpił kod **Roboty drogowe**, który wystąpił również w 11 województwach na pozycjach od 2 do 5 i skupił 7403 przetargów. Również podobny, choć nieco mniejszy wynik obserwujemy w przypadku **kodu CPV Usługi projektowania**. Skupił 7034 przetargi i wystąpił tak samo w 11 województwach na pozycjach od 2 do 5.

### Odchylenie pomiędzy województwami
Matematyczna analiza struktury kodów w wojwództwach przedstawiająca główne tendencje oraz województwa z największym odchyleniem od średniej. 

### 2021

<img width="1219" height="726" alt="obraz" src="https://github.com/user-attachments/assets/59ba843c-bdc2-478a-b9ba-7d75d787e63e" />

Rok 2021 stanowił pierwszą pełną edycję systemu przetargowego funkcjonującego w reżimie znowelizowanego Prawa zamówień publicznych, obowiązującego od 1 stycznia 2021 r. W strukturze zamówień dominował kod CPV **45000000-7** (**roboty budowlane**), przy czym wolumeny przetargów były zróżnicowane przestrzennie — od 1168 postępowań w województwie **mazowieckim** do 248 w **podlaskim**. Na dalszych pozycjach rankingów regionalnych utrwaliły się kategorie infrastruktury drogowej (CPV **45233120-6**, **45233140-2**), usług inżynieryjnych (**71320000-7**) oraz ochrony osób i mienia (**79710000-4**). Wyraźna specyfika regionalna objawiała się m.in. dominacją usług szkoleniowych w województwie **lubelskim** (CPV **80500000-9**, 103 postępowania) — co koresponduje z intensywnym współfinansowaniem projektów z Europejskiego Funduszu Społecznego w tamtym okresie — oraz obecnością usług odśnieżania w **Małopolsce** (**90620000-9**, 134 postępowania), odzwierciedlającą warunki geograficzne regionu.

### 2022

<img width="1214" height="724" alt="obraz" src="https://github.com/user-attachments/assets/f17f2ac6-1545-48f1-bde9-48d74f102082" />

Rok 2022 przyniósł we wszystkich analizowanych województwach wyraźne zwiększenie wolumenu postępowań przetargowych. W **Mazowieckiem** liczba przetargów budowlanych wzrosła z 1168 do 1971, w **Dolnośląskiem** — z 684 do 1053, a w **Śląskiem** — z 972 do 1454. Wzrost ten można interpretować jako skumulowany efekt: odblokowania inwestycji wstrzymanych w dobie pandemii COVID-19, absorbcji środków z Krajowego Planu Odbudowy oraz przesuniętego w czasie uruchomienia perspektywy finansowej UE 2021–2027. Charakterystycznym novum roku 2022 było masowe pojawienie się kodu CPV **30213100-6** (**komputery przenośne**) w wielu województwach jednocześnie — **Dolnośląskiem** (118), **Kujawsko-Pomorskiem** (101), **Lubuskiem** (54), **Warmińsko-Mazurskiem** (77), **Zachodniopomorskiem** (80) i **Wielkopolskiem** (161). Zjawisko to niemal z pewnością wiązało się z centralnie koordynowanym programem wyposażenia szkół w sprzęt komputerowy. Odnotowano również wzrost aktywności w zakresie zamówień na urządzenia komputerowe (**30200000-1**) — m.in. w **Podkarpackiem** (126) i **Podlaskiem** (66).

### 2023

<img width="1213" height="725" alt="obraz" src="https://github.com/user-attachments/assets/e44a4f0d-3b9e-4684-b2c4-ebb24a2cd457" />

W roku 2023 nastąpiła częściowa korekta wolumenu po szczytowym roku poprzednim. W województwie **mazowieckim** liczba przetargów budowlanych nieznacznie spadła z 1971 do 1861, a w **śląskim** — z 1454 do 1148. Równocześnie jednak w województwie **lubelskim** zaobserwowano dynamiczny wzrost kategorii drogowych (CPV **45233120-6**: wzrost z 149 do 214; CPV **45233000-9**: wzrost ze 143 do 187), co może świadczyć o przesunięciu priorytetów inwestycyjnych w kierunku infrastruktury transportowej na wschodniej flance kraju. Pojawiające się w strukturze zamówień kody CPV **33100000-1** (**urządzenia medyczne**) w **Dolnośląskiem** (111) i **Kujawsko-Pomorskiem** (69) wskazują na kontynuację doposażania placówek ochrony zdrowia, zapoczątkowanego jeszcze w reakcji na pandemię. Kategoria usług ochroniarskich (**79710000-4**) umocniła swoją pozycję w rankingach większości województw.

### 2024

<img width="1216" height="728" alt="obraz" src="https://github.com/user-attachments/assets/ce24d1ec-72be-494c-8f42-62f3fba05d9d" />

W roku 2024 wolumeny przetargów utrzymały się na poziomach porównywalnych z rokiem poprzednim, przy czym wyraźne ożywienie zanotowało **Mazowieckie** (powrót do 1979 postępowań budowlanych) i **Łódzkie** (wzrost z 809 do 951). Istotnym sygnałem jakościowej zmiany struktury popytu był dynamiczny wzrost zamówień na usługi ubezpieczeniowe (CPV **66510000-8**) w województwie **kujawsko-pomorskim** — z 146 do 212 — co może odzwierciedlać rosnącą świadomość zarządzania ryzykiem w sektorze publicznym. W **Małopolskiem** po raz pierwszy w czołówce rankingu znalazły się produkty farmaceutyczne (CPV **33600000-6**, 187 postępowań), co wpisuje się w systematyczne zwiększanie aktywności przetargowej szpitali regionalnych. Warta odnotowania jest również wyraźna obecność robót remontowych (CPV **45453000-7**) w strukturach zamówień **Mazowieckiego** (292) i **Wielkopolskiego** (159) — co może sugerować, że dotychczasowy nacisk na nowe inwestycje zaczyna być uzupełniany przez systematyczne utrzymanie istniejącej infrastruktury.

### 2025

<img width="1211" height="724" alt="obraz" src="https://github.com/user-attachments/assets/7e84bcfe-b486-45f1-8f79-9d1b274c362d" />

Dane za rok 2025 ujawniają dwie wyraziste tendencje jakościowe. Po pierwsze, kod CPV **31122000-7** (**jednostki prądotwórcze**) pojawił się nagle i z wysokimi wolumenami w województwach: **lubelskim** (109), **podlaskim** (79), **warmińsko-mazurskim** (70) oraz **łódzkim** (129). Koncentracja geograficzna tego popytu — silna na wschodzie i północnym wschodzie kraju — wskazuje na związek z kontekstem geopolitycznym (bezpośrednie sąsiedztwo z Ukrainą i Białorusią) oraz z realizacją programów wzmacniania odporności infrastrukturalnej. Po drugie, pozycja CPV **80000000-4** (**usługi edukacyjne i szkoleniowe**) zanotowała znaczący wzrost w województwach: **lubuskim** (138), **śląskim** (183), **łódzkim** (146) i **lubelskim** (110). Może to świadczyć o intensywnej absorpcji środków z Europejskiego Funduszu Społecznego Plus w ramach bieżącej perspektywy finansowej. Warty uwagi jest również wzrost liczby przetargów na samochody osobowe (CPV **34110000-1**) w kilku województwach (**kujawsko-pomorskie**, **lubuskie**, **zachodniopomorskie**), co może odzwierciedlać odroczone decyzje o odnowieniu flot pojazdów publicznych po latach cięć inwestycyjnych.

### Legenda

<img width="1036" height="675" alt="obraz" src="https://github.com/user-attachments/assets/f2af6d88-c725-4257-bf38-5a7f67df0322" />

### Podsumowanie

W całym analizowanym okresie kod CPV **45000000-7** zajmował bezwzględnie pierwszą pozycję we wszystkich województwach i we wszystkich latach, przy czym udział tej pozycji CPV w rankingach był na tyle przeważający, że uzasadnia traktowanie jej nie jako jednej z kategorii zamówień, lecz jako konstytutywnej cechy polskiego rynku zamówień publicznych. Wartości bezwzględne były przy tym silnie skorelowane z wielkością demograficzno-ekonomiczną regionów: **Mazowieckie** i **Śląskie** konsekwentnie odnotowywały wolumeny kilkukrotnie wyższe niż województwa o mniejszym potencjale gospodarczym (**Lubuskie**, **Opolskie**, **Świętokrzyskie**).

Systematyczny wzrost wolumenu przetargów na usługi projektowania inżynieryjnego (CPV **71320000-7**) w latach 2021–2025 może być interpretowany jako wskaźnik wyprzedzający przyszłych inwestycji budowlanych — faza projektowania poprzedza realizację o jeden do kilku lat. Obserwacja ta sugeruje, że rynek zamówień publicznych w Polsce nie wykazuje jeszcze oznak nasycenia w segmencie infrastrukturalnym.

Trwałe różnice w składzie pozycji CPV między województwami odzwierciedlają nie tylko warunki geograficzne (odśnieżanie w **Małopolsce** i **Podkarpaciu**, infrastruktura drogowa we wschodniej Polsce), lecz również strukturę instytucjonalną zamawiających — koncentrację szpitali klinicznych (produkty farmaceutyczne i wyroby medyczne w **Małopolsce** i **Śląskiem**), obecność dużych instytucji edukacyjnych (usługi szkoleniowe w **Lubelskim** i **Łódzkim**) czy aktywność samorządów metropolitalnych (ochrona i remonty w **Mazowieckiem**).

Analiza danych wskazuje, że polska struktura zamówień publicznych jest wrażliwa na zewnętrzne impulsy systemowe: zakupy sprzętu ICT dla szkół w 2022 r., wzrost zapotrzebowania na agregaty prądotwórcze w kontekście geopolitycznym w 2025 r. czy intensyfikacja usług szkoleniowych w związku z absorpcją EFS+. Zjawisko to świadczy o wysokiej reaktywności rynku zamówień na decyzje podejmowane na poziomie centralnym lub unijnym, co może być postrzegane zarówno jako cecha adaptacyjna systemu, jak i sygnał ograniczonej autonomii strategicznej zamawiających regionalnych.

# Analiza sezonowości rozkładu przetargów
<img width="1261" height="721" alt="obraz" src="https://github.com/user-attachments/assets/b6bceb05-1fa1-423e-a48e-e63c494535c0" />

## Top5 CPV overall w czasie - czy są zmiany najbardziej popularnych CPV? 
Czy we wszystkich województwach sytuacja się powtarza? Czy czasami są odstępstwa?+
## 1. Jak zmienia się ogólna liczba w czasie
## 2. Które dziedziny wykazują największe wahania, a jakie najmniejsze?

# Analiza rozkładu przetargów względem innych czynników
## Wstęp
Nie ma dostępnych danych udziału **miasta Warszawy** w ogólnym PKB kraju. Jedyne dostępne dane przedstawiają udział **Regionu Warszawskiego Stołecznego** według podziału **NUTS 2**. Przekształcenie danych uzyskanych z platformy eZamówienia na system **NUTS 2** mogłoby doprowadzić do złej alokacji jednostek samorządu terytorialnego ze względu na oryginalną strukturę danych zawierających `organizationProvince`, które przedstawia województwo zamawiającego, oraz `organizationCity`, które przedstawia miejscowość zamawiającego. Ze względu na skalę wynikającą z ilości miejscowości wchodzących w skład **Regionu Warszawskiego Stołecznego**, a jednocześnie małą precyzyjność oryginalnych danych przedstawiających lokalizację przetargu w odniesieniu do układu administracyjnego, konwersja danych do formatu **NUTS 2** i wzbogacenie ich o dane odnośnie populacji w gminach wchodzących w skład **Regionu Warszawskiego Stołecznego** obarczone jest zbyt dużym ryzykiem złej agregacji danych podczas procesu konwersji.
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
