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

## Top5 CPV w województwach - czy województwa wyglądają podobnie czy są jakieś zmiany?

<img width="1106" height="724" alt="obraz" src="https://github.com/user-attachments/assets/0305f33c-e0e2-46fe-ac50-f6f182213e22" />
<img width="809" height="424" alt="obraz" src="https://github.com/user-attachments/assets/239a2ee7-1d66-4157-a0f3-75dfe94cad87" />


### 2021

<img width="1219" height="726" alt="obraz" src="https://github.com/user-attachments/assets/59ba843c-bdc2-478a-b9ba-7d75d787e63e" />

### 2022

<img width="1214" height="724" alt="obraz" src="https://github.com/user-attachments/assets/f17f2ac6-1545-48f1-bde9-48d74f102082" />

### 2023

<img width="1213" height="725" alt="obraz" src="https://github.com/user-attachments/assets/e44a4f0d-3b9e-4684-b2c4-ebb24a2cd457" />

### 2024

<img width="1216" height="728" alt="obraz" src="https://github.com/user-attachments/assets/ce24d1ec-72be-494c-8f42-62f3fba05d9d" />

### 2025

<img width="1211" height="724" alt="obraz" src="https://github.com/user-attachments/assets/7e84bcfe-b486-45f1-8f79-9d1b274c362d" />

### Legenda

<img width="1036" height="675" alt="obraz" src="https://github.com/user-attachments/assets/f2af6d88-c725-4257-bf38-5a7f67df0322" />

### Tabela zbiorcza

|   Rok | Województwo         | Kod CPV    | Opis CPV                                                                                                                                  |   Liczba przetargów |
|------:|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------|--------------------:|
|  2021 | Dolnośląskie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 684 |
|  2021 | Dolnośląskie        | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 109 |
|  2021 | Dolnośląskie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 108 |
|  2021 | Dolnośląskie        | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                  79 |
|  2021 | Dolnośląskie        | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  76 |
|  2022 | Dolnośląskie        | 45000000-7 | Roboty budowlane                                                                                                                          |                1053 |
|  2022 | Dolnośląskie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 166 |
|  2022 | Dolnośląskie        | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                 155 |
|  2022 | Dolnośląskie        | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 131 |
|  2022 | Dolnośląskie        | 30213100-6 | Komputery przenośne                                                                                                                       |                 118 |
|  2023 | Dolnośląskie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 869 |
|  2023 | Dolnośląskie        | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 132 |
|  2023 | Dolnośląskie        | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                 113 |
|  2023 | Dolnośląskie        | 33100000-1 | Urządzenia medyczne                                                                                                                       |                 111 |
|  2023 | Dolnośląskie        | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 102 |
|  2024 | Dolnośląskie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 980 |
|  2024 | Dolnośląskie        | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 129 |
|  2024 | Dolnośląskie        | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 119 |
|  2024 | Dolnośląskie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 114 |
|  2024 | Dolnośląskie        | 15100000-9 | Produkty zwierzęce, mięso i produkty mięsne                                                                                               |                  91 |
|  2025 | Dolnośląskie        | 45000000-7 | Roboty budowlane                                                                                                                          |                1144 |
|  2025 | Dolnośląskie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 121 |
|  2025 | Dolnośląskie        | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 116 |
|  2025 | Dolnośląskie        | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  97 |
|  2025 | Dolnośląskie        | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                  97 |
|  2021 | Kujawsko-pomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 575 |
|  2021 | Kujawsko-pomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 100 |
|  2021 | Kujawsko-pomorskie  | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                  82 |
|  2021 | Kujawsko-pomorskie  | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  65 |
|  2021 | Kujawsko-pomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                  63 |
|  2022 | Kujawsko-pomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 811 |
|  2022 | Kujawsko-pomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 120 |
|  2022 | Kujawsko-pomorskie  | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                 118 |
|  2022 | Kujawsko-pomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                 113 |
|  2022 | Kujawsko-pomorskie  | 30213100-6 | Komputery przenośne                                                                                                                       |                 101 |
|  2023 | Kujawsko-pomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 659 |
|  2023 | Kujawsko-pomorskie  | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                 146 |
|  2023 | Kujawsko-pomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 143 |
|  2023 | Kujawsko-pomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                  97 |
|  2023 | Kujawsko-pomorskie  | 33100000-1 | Urządzenia medyczne                                                                                                                       |                  69 |
|  2024 | Kujawsko-pomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 710 |
|  2024 | Kujawsko-pomorskie  | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                 212 |
|  2024 | Kujawsko-pomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                 100 |
|  2024 | Kujawsko-pomorskie  | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  98 |
|  2024 | Kujawsko-pomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  78 |
|  2025 | Kujawsko-pomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 788 |
|  2025 | Kujawsko-pomorskie  | 66510000-8 | Usługi ubezpieczeniowe                                                                                                                    |                 215 |
|  2025 | Kujawsko-pomorskie  | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  78 |
|  2025 | Kujawsko-pomorskie  | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  76 |
|  2025 | Kujawsko-pomorskie  | 34110000-1 | Samochody osobowe                                                                                                                         |                  71 |
|  2021 | Lubelskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 383 |
|  2021 | Lubelskie           | 80500000-9 | Usługi szkoleniowe                                                                                                                        |                 103 |
|  2021 | Lubelskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                  89 |
|  2021 | Lubelskie           | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                  85 |
|  2021 | Lubelskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  81 |
|  2022 | Lubelskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 805 |
|  2022 | Lubelskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                 152 |
|  2022 | Lubelskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 149 |
|  2022 | Lubelskie           | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                 143 |
|  2022 | Lubelskie           | 80530000-8 | Usługi szkolenia zawodowego                                                                                                               |                 116 |
|  2023 | Lubelskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 696 |
|  2023 | Lubelskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 214 |
|  2023 | Lubelskie           | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                 187 |
|  2023 | Lubelskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                 169 |
|  2023 | Lubelskie           | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                  97 |
|  2024 | Lubelskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 799 |
|  2024 | Lubelskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 125 |
|  2024 | Lubelskie           | 90500000-2 | Usługi związane z odpadami                                                                                                                |                 109 |
|  2024 | Lubelskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 103 |
|  2024 | Lubelskie           | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                  94 |
|  2025 | Lubelskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 706 |
|  2025 | Lubelskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 125 |
|  2025 | Lubelskie           | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 110 |
|  2025 | Lubelskie           | 31122000-7 | Jednostki prądotwórcze                                                                                                                    |                 109 |
|  2025 | Lubelskie           | 80500000-9 | Usługi szkoleniowe                                                                                                                        |                 100 |
|  2021 | Lubuskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 266 |
|  2021 | Lubuskie            | 45233140-2 | Roboty drogowe                                                                                                                            |                  54 |
|  2021 | Lubuskie            | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  39 |
|  2021 | Lubuskie            | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  33 |
|  2021 | Lubuskie            | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  31 |
|  2022 | Lubuskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 439 |
|  2022 | Lubuskie            | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  91 |
|  2022 | Lubuskie            | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  57 |
|  2022 | Lubuskie            | 30213100-6 | Komputery przenośne                                                                                                                       |                  54 |
|  2022 | Lubuskie            | 45233140-2 | Roboty drogowe                                                                                                                            |                  54 |
|  2023 | Lubuskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 397 |
|  2023 | Lubuskie            | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  87 |
|  2023 | Lubuskie            | 45233140-2 | Roboty drogowe                                                                                                                            |                  50 |
|  2023 | Lubuskie            | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  47 |
|  2023 | Lubuskie            | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                  45 |
|  2024 | Lubuskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 352 |
|  2024 | Lubuskie            | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                  55 |
|  2024 | Lubuskie            | 45233140-2 | Roboty drogowe                                                                                                                            |                  49 |
|  2024 | Lubuskie            | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  45 |
|  2024 | Lubuskie            | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  43 |
|  2025 | Lubuskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 332 |
|  2025 | Lubuskie            | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 138 |
|  2025 | Lubuskie            | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  63 |
|  2025 | Lubuskie            | 34110000-1 | Samochody osobowe                                                                                                                         |                  57 |
|  2025 | Lubuskie            | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  46 |
|  2021 | Mazowieckie         | 45000000-7 | Roboty budowlane                                                                                                                          |                1168 |
|  2021 | Mazowieckie         | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 358 |
|  2021 | Mazowieckie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 232 |
|  2021 | Mazowieckie         | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 200 |
|  2021 | Mazowieckie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 195 |
|  2022 | Mazowieckie         | 45000000-7 | Roboty budowlane                                                                                                                          |                1971 |
|  2022 | Mazowieckie         | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 441 |
|  2022 | Mazowieckie         | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 307 |
|  2022 | Mazowieckie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 275 |
|  2022 | Mazowieckie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 267 |
|  2023 | Mazowieckie         | 45000000-7 | Roboty budowlane                                                                                                                          |                1861 |
|  2023 | Mazowieckie         | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 414 |
|  2023 | Mazowieckie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 290 |
|  2023 | Mazowieckie         | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 274 |
|  2023 | Mazowieckie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 272 |
|  2024 | Mazowieckie         | 45000000-7 | Roboty budowlane                                                                                                                          |                1979 |
|  2024 | Mazowieckie         | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 318 |
|  2024 | Mazowieckie         | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 312 |
|  2024 | Mazowieckie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 292 |
|  2024 | Mazowieckie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 231 |
|  2025 | Mazowieckie         | 45000000-7 | Roboty budowlane                                                                                                                          |                1886 |
|  2025 | Mazowieckie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 347 |
|  2025 | Mazowieckie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 347 |
|  2025 | Mazowieckie         | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 287 |
|  2025 | Mazowieckie         | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 243 |
|  2021 | Małopolskie         | 45000000-7 | Roboty budowlane                                                                                                                          |                 615 |
|  2021 | Małopolskie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 222 |
|  2021 | Małopolskie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 200 |
|  2021 | Małopolskie         | 90620000-9 | Usługi odśnieżania                                                                                                                        |                 134 |
|  2021 | Małopolskie         | 45233142-6 | Roboty w zakresie naprawy dróg                                                                                                            |                 116 |
|  2022 | Małopolskie         | 45000000-7 | Roboty budowlane                                                                                                                          |                 942 |
|  2022 | Małopolskie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 288 |
|  2022 | Małopolskie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 246 |
|  2022 | Małopolskie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 172 |
|  2022 | Małopolskie         | 90620000-9 | Usługi odśnieżania                                                                                                                        |                 150 |
|  2023 | Małopolskie         | 45000000-7 | Roboty budowlane                                                                                                                          |                 868 |
|  2023 | Małopolskie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 271 |
|  2023 | Małopolskie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 240 |
|  2023 | Małopolskie         | 45233142-6 | Roboty w zakresie naprawy dróg                                                                                                            |                 156 |
|  2023 | Małopolskie         | 90620000-9 | Usługi odśnieżania                                                                                                                        |                 148 |
|  2024 | Małopolskie         | 45000000-7 | Roboty budowlane                                                                                                                          |                 891 |
|  2024 | Małopolskie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 228 |
|  2024 | Małopolskie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 191 |
|  2024 | Małopolskie         | 33600000-6 | Produkty farmaceutyczne                                                                                                                   |                 187 |
|  2024 | Małopolskie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 186 |
|  2025 | Małopolskie         | 45000000-7 | Roboty budowlane                                                                                                                          |                 954 |
|  2025 | Małopolskie         | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 244 |
|  2025 | Małopolskie         | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 194 |
|  2025 | Małopolskie         | 45233140-2 | Roboty drogowe                                                                                                                            |                 191 |
|  2025 | Małopolskie         | 33600000-6 | Produkty farmaceutyczne                                                                                                                   |                 157 |
|  2021 | Opolskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 266 |
|  2021 | Opolskie            | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  43 |
|  2021 | Opolskie            | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  38 |
|  2021 | Opolskie            | 09310000-5 | Elektryczność                                                                                                                             |                  37 |
|  2021 | Opolskie            | 45200000-9 | Roboty budowlane w zakresie wznoszenia kompletnych obiektów budowlanych lub ich części oraz roboty w zakresie inżynierii lądowej i wodnej |                  29 |
|  2022 | Opolskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 451 |
|  2022 | Opolskie            | 09310000-5 | Elektryczność                                                                                                                             |                  64 |
|  2022 | Opolskie            | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  50 |
|  2022 | Opolskie            | 33140000-3 | Materiały medyczne                                                                                                                        |                  46 |
|  2022 | Opolskie            | 30200000-1 | Urządzenia komputerowe                                                                                                                    |                  45 |
|  2023 | Opolskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 318 |
|  2023 | Opolskie            | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                  44 |
|  2023 | Opolskie            | 33140000-3 | Materiały medyczne                                                                                                                        |                  41 |
|  2023 | Opolskie            | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  41 |
|  2023 | Opolskie            | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  39 |
|  2024 | Opolskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 345 |
|  2024 | Opolskie            | 33140000-3 | Materiały medyczne                                                                                                                        |                  54 |
|  2024 | Opolskie            | 45233000-9 | Roboty w zakresie konstruowania, fundamentowania oraz wykonywania nawierzchni autostrad, dróg                                             |                  39 |
|  2024 | Opolskie            | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  36 |
|  2024 | Opolskie            | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  36 |
|  2025 | Opolskie            | 45000000-7 | Roboty budowlane                                                                                                                          |                 415 |
|  2025 | Opolskie            | 33140000-3 | Materiały medyczne                                                                                                                        |                  50 |
|  2025 | Opolskie            | 15000000-8 | Żywność, napoje, tytoń i produkty pokrewne                                                                                                |                  47 |
|  2025 | Opolskie            | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  44 |
|  2025 | Opolskie            | 45233140-2 | Roboty drogowe                                                                                                                            |                  42 |
|  2021 | Podkarpackie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 592 |
|  2021 | Podkarpackie        | 45233142-6 | Roboty w zakresie naprawy dróg                                                                                                            |                 116 |
|  2021 | Podkarpackie        | 45233222-1 | Roboty budowlane w zakresie układania chodników i asfaltowania                                                                            |                 109 |
|  2021 | Podkarpackie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  93 |
|  2021 | Podkarpackie        | 45233140-2 | Roboty drogowe                                                                                                                            |                  87 |
|  2022 | Podkarpackie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 868 |
|  2022 | Podkarpackie        | 45233140-2 | Roboty drogowe                                                                                                                            |                 165 |
|  2022 | Podkarpackie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 138 |
|  2022 | Podkarpackie        | 30200000-1 | Urządzenia komputerowe                                                                                                                    |                 126 |
|  2022 | Podkarpackie        | 45233142-6 | Roboty w zakresie naprawy dróg                                                                                                            |                 125 |
|  2023 | Podkarpackie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 806 |
|  2023 | Podkarpackie        | 45233140-2 | Roboty drogowe                                                                                                                            |                 192 |
|  2023 | Podkarpackie        | 45233222-1 | Roboty budowlane w zakresie układania chodników i asfaltowania                                                                            |                 124 |
|  2023 | Podkarpackie        | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  88 |
|  2023 | Podkarpackie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  88 |
|  2024 | Podkarpackie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 879 |
|  2024 | Podkarpackie        | 45233140-2 | Roboty drogowe                                                                                                                            |                 161 |
|  2024 | Podkarpackie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 125 |
|  2024 | Podkarpackie        | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  94 |
|  2024 | Podkarpackie        | 90620000-9 | Usługi odśnieżania                                                                                                                        |                  85 |
|  2025 | Podkarpackie        | 45000000-7 | Roboty budowlane                                                                                                                          |                 734 |
|  2025 | Podkarpackie        | 45233140-2 | Roboty drogowe                                                                                                                            |                 145 |
|  2025 | Podkarpackie        | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 140 |
|  2025 | Podkarpackie        | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  91 |
|  2025 | Podkarpackie        | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  86 |
|  2021 | Podlaskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 248 |
|  2021 | Podlaskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 116 |
|  2021 | Podlaskie           | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  52 |
|  2021 | Podlaskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  40 |
|  2021 | Podlaskie           | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  39 |
|  2022 | Podlaskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 447 |
|  2022 | Podlaskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 189 |
|  2022 | Podlaskie           | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  75 |
|  2022 | Podlaskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  70 |
|  2022 | Podlaskie           | 30200000-1 | Urządzenia komputerowe                                                                                                                    |                  66 |
|  2023 | Podlaskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 400 |
|  2023 | Podlaskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 191 |
|  2023 | Podlaskie           | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  99 |
|  2023 | Podlaskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  81 |
|  2023 | Podlaskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                  59 |
|  2024 | Podlaskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 402 |
|  2024 | Podlaskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 199 |
|  2024 | Podlaskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  81 |
|  2024 | Podlaskie           | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  77 |
|  2024 | Podlaskie           | 09135100-5 | Olej opałowy                                                                                                                              |                  69 |
|  2025 | Podlaskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 386 |
|  2025 | Podlaskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 107 |
|  2025 | Podlaskie           | 31122000-7 | Jednostki prądotwórcze                                                                                                                    |                  79 |
|  2025 | Podlaskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  73 |
|  2025 | Podlaskie           | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  72 |
|  2021 | Pomorskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 514 |
|  2021 | Pomorskie           | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 111 |
|  2021 | Pomorskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 106 |
|  2021 | Pomorskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                  86 |
|  2021 | Pomorskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  85 |
|  2022 | Pomorskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 809 |
|  2022 | Pomorskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 131 |
|  2022 | Pomorskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 129 |
|  2022 | Pomorskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                 121 |
|  2022 | Pomorskie           | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 114 |
|  2023 | Pomorskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 704 |
|  2023 | Pomorskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 112 |
|  2023 | Pomorskie           | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  98 |
|  2023 | Pomorskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  95 |
|  2023 | Pomorskie           | 45233140-2 | Roboty drogowe                                                                                                                            |                  94 |
|  2024 | Pomorskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 727 |
|  2024 | Pomorskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 122 |
|  2024 | Pomorskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 103 |
|  2024 | Pomorskie           | 15800000-6 | Różne produkty spożywcze                                                                                                                  |                  87 |
|  2024 | Pomorskie           | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  83 |
|  2025 | Pomorskie           | 45000000-7 | Roboty budowlane                                                                                                                          |                 605 |
|  2025 | Pomorskie           | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 160 |
|  2025 | Pomorskie           | 15800000-6 | Różne produkty spożywcze                                                                                                                  |                  90 |
|  2025 | Pomorskie           | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  86 |
|  2025 | Pomorskie           | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  76 |
|  2021 | Warmińsko-mazurskie | 45000000-7 | Roboty budowlane                                                                                                                          |                 322 |
|  2021 | Warmińsko-mazurskie | 45233140-2 | Roboty drogowe                                                                                                                            |                 120 |
|  2021 | Warmińsko-mazurskie | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  93 |
|  2021 | Warmińsko-mazurskie | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  49 |
|  2021 | Warmińsko-mazurskie | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  44 |
|  2022 | Warmińsko-mazurskie | 45000000-7 | Roboty budowlane                                                                                                                          |                 433 |
|  2022 | Warmińsko-mazurskie | 45233140-2 | Roboty drogowe                                                                                                                            |                 136 |
|  2022 | Warmińsko-mazurskie | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 123 |
|  2022 | Warmińsko-mazurskie | 30213100-6 | Komputery przenośne                                                                                                                       |                  77 |
|  2022 | Warmińsko-mazurskie | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  73 |
|  2023 | Warmińsko-mazurskie | 45000000-7 | Roboty budowlane                                                                                                                          |                 382 |
|  2023 | Warmińsko-mazurskie | 45233140-2 | Roboty drogowe                                                                                                                            |                 137 |
|  2023 | Warmińsko-mazurskie | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 110 |
|  2023 | Warmińsko-mazurskie | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  74 |
|  2023 | Warmińsko-mazurskie | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  56 |
|  2024 | Warmińsko-mazurskie | 45000000-7 | Roboty budowlane                                                                                                                          |                 422 |
|  2024 | Warmińsko-mazurskie | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 104 |
|  2024 | Warmińsko-mazurskie | 45233140-2 | Roboty drogowe                                                                                                                            |                  93 |
|  2024 | Warmińsko-mazurskie | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  79 |
|  2024 | Warmińsko-mazurskie | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  70 |
|  2025 | Warmińsko-mazurskie | 45000000-7 | Roboty budowlane                                                                                                                          |                 313 |
|  2025 | Warmińsko-mazurskie | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  95 |
|  2025 | Warmińsko-mazurskie | 31122000-7 | Jednostki prądotwórcze                                                                                                                    |                  70 |
|  2025 | Warmińsko-mazurskie | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  63 |
|  2025 | Warmińsko-mazurskie | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  61 |
|  2021 | Wielkopolskie       | 45000000-7 | Roboty budowlane                                                                                                                          |                 727 |
|  2021 | Wielkopolskie       | 45233140-2 | Roboty drogowe                                                                                                                            |                 251 |
|  2021 | Wielkopolskie       | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 158 |
|  2021 | Wielkopolskie       | 45233142-6 | Roboty w zakresie naprawy dróg                                                                                                            |                  81 |
|  2021 | Wielkopolskie       | 60100000-9 | Usługi w zakresie transportu drogowego                                                                                                    |                  80 |
|  2022 | Wielkopolskie       | 45000000-7 | Roboty budowlane                                                                                                                          |                1063 |
|  2022 | Wielkopolskie       | 45233140-2 | Roboty drogowe                                                                                                                            |                 293 |
|  2022 | Wielkopolskie       | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 204 |
|  2022 | Wielkopolskie       | 30200000-1 | Urządzenia komputerowe                                                                                                                    |                 161 |
|  2022 | Wielkopolskie       | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                 127 |
|  2023 | Wielkopolskie       | 45000000-7 | Roboty budowlane                                                                                                                          |                 904 |
|  2023 | Wielkopolskie       | 45233140-2 | Roboty drogowe                                                                                                                            |                 289 |
|  2023 | Wielkopolskie       | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 190 |
|  2023 | Wielkopolskie       | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                 126 |
|  2023 | Wielkopolskie       | 60100000-9 | Usługi w zakresie transportu drogowego                                                                                                    |                 108 |
|  2024 | Wielkopolskie       | 45000000-7 | Roboty budowlane                                                                                                                          |                 994 |
|  2024 | Wielkopolskie       | 45233140-2 | Roboty drogowe                                                                                                                            |                 279 |
|  2024 | Wielkopolskie       | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 159 |
|  2024 | Wielkopolskie       | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 140 |
|  2024 | Wielkopolskie       | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 130 |
|  2025 | Wielkopolskie       | 45000000-7 | Roboty budowlane                                                                                                                          |                 920 |
|  2025 | Wielkopolskie       | 45233140-2 | Roboty drogowe                                                                                                                            |                 228 |
|  2025 | Wielkopolskie       | 33100000-1 | Urządzenia medyczne                                                                                                                       |                 151 |
|  2025 | Wielkopolskie       | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 140 |
|  2025 | Wielkopolskie       | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                 114 |
|  2021 | Zachodniopomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 365 |
|  2021 | Zachodniopomorskie  | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  47 |
|  2021 | Zachodniopomorskie  | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  46 |
|  2021 | Zachodniopomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                  43 |
|  2021 | Zachodniopomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  42 |
|  2022 | Zachodniopomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 752 |
|  2022 | Zachodniopomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  92 |
|  2022 | Zachodniopomorskie  | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  91 |
|  2022 | Zachodniopomorskie  | 30213100-6 | Komputery przenośne                                                                                                                       |                  80 |
|  2022 | Zachodniopomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                  73 |
|  2023 | Zachodniopomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 563 |
|  2023 | Zachodniopomorskie  | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  91 |
|  2023 | Zachodniopomorskie  | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  75 |
|  2023 | Zachodniopomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  71 |
|  2023 | Zachodniopomorskie  | 45233140-2 | Roboty drogowe                                                                                                                            |                  63 |
|  2024 | Zachodniopomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 555 |
|  2024 | Zachodniopomorskie  | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  75 |
|  2024 | Zachodniopomorskie  | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  69 |
|  2024 | Zachodniopomorskie  | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  68 |
|  2024 | Zachodniopomorskie  | 45453000-7 | Roboty remontowe i renowacyjne                                                                                                            |                  64 |
|  2025 | Zachodniopomorskie  | 45000000-7 | Roboty budowlane                                                                                                                          |                 484 |
|  2025 | Zachodniopomorskie  | 45233220-7 | Roboty w zakresie nawierzchni dróg                                                                                                        |                  67 |
|  2025 | Zachodniopomorskie  | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  65 |
|  2025 | Zachodniopomorskie  | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  58 |
|  2025 | Zachodniopomorskie  | 34110000-1 | Samochody osobowe                                                                                                                         |                  51 |
|  2021 | Łódzkie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 522 |
|  2021 | Łódzkie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 118 |
|  2021 | Łódzkie             | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 101 |
|  2021 | Łódzkie             | 45231300-8 | Roboty budowlane w zakresie budowy wodociągów i rurociągów do odprowadzania ścieków                                                       |                  65 |
|  2021 | Łódzkie             | 90500000-2 | Usługi związane z odpadami                                                                                                                |                  52 |
|  2022 | Łódzkie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 858 |
|  2022 | Łódzkie             | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 170 |
|  2022 | Łódzkie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 160 |
|  2022 | Łódzkie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 108 |
|  2022 | Łódzkie             | 45231300-8 | Roboty budowlane w zakresie budowy wodociągów i rurociągów do odprowadzania ścieków                                                       |                 101 |
|  2023 | Łódzkie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 809 |
|  2023 | Łódzkie             | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 159 |
|  2023 | Łódzkie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 157 |
|  2023 | Łódzkie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 101 |
|  2023 | Łódzkie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  71 |
|  2024 | Łódzkie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 951 |
|  2024 | Łódzkie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 130 |
|  2024 | Łódzkie             | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 127 |
|  2024 | Łódzkie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  87 |
|  2024 | Łódzkie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  83 |
|  2025 | Łódzkie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 882 |
|  2025 | Łódzkie             | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 146 |
|  2025 | Łódzkie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 143 |
|  2025 | Łódzkie             | 30200000-1 | Urządzenia komputerowe                                                                                                                    |                 137 |
|  2025 | Łódzkie             | 31122000-7 | Jednostki prądotwórcze                                                                                                                    |                 129 |
|  2021 | Śląskie             | 45000000-7 | Roboty budowlane                                                                                                                          |                 972 |
|  2021 | Śląskie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 111 |
|  2021 | Śląskie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 110 |
|  2021 | Śląskie             | 15000000-8 | Żywność, napoje, tytoń i produkty pokrewne                                                                                                |                 102 |
|  2021 | Śląskie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                  92 |
|  2022 | Śląskie             | 45000000-7 | Roboty budowlane                                                                                                                          |                1454 |
|  2022 | Śląskie             | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 203 |
|  2022 | Śląskie             | 15000000-8 | Żywność, napoje, tytoń i produkty pokrewne                                                                                                |                 196 |
|  2022 | Śląskie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 191 |
|  2022 | Śląskie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 165 |
|  2023 | Śląskie             | 45000000-7 | Roboty budowlane                                                                                                                          |                1148 |
|  2023 | Śląskie             | 15000000-8 | Żywność, napoje, tytoń i produkty pokrewne                                                                                                |                 203 |
|  2023 | Śląskie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 180 |
|  2023 | Śląskie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 178 |
|  2023 | Śląskie             | 15800000-6 | Różne produkty spożywcze                                                                                                                  |                 132 |
|  2024 | Śląskie             | 45000000-7 | Roboty budowlane                                                                                                                          |                1270 |
|  2024 | Śląskie             | 15000000-8 | Żywność, napoje, tytoń i produkty pokrewne                                                                                                |                 169 |
|  2024 | Śląskie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 164 |
|  2024 | Śląskie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 127 |
|  2024 | Śląskie             | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                 125 |
|  2025 | Śląskie             | 45000000-7 | Roboty budowlane                                                                                                                          |                1374 |
|  2025 | Śląskie             | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                 183 |
|  2025 | Śląskie             | 79710000-4 | Usługi ochroniarskie                                                                                                                      |                 151 |
|  2025 | Śląskie             | 45233140-2 | Roboty drogowe                                                                                                                            |                 140 |
|  2025 | Śląskie             | 15800000-6 | Różne produkty spożywcze                                                                                                                  |                 124 |
|  2021 | Świętokrzyskie      | 45000000-7 | Roboty budowlane                                                                                                                          |                 277 |
|  2021 | Świętokrzyskie      | 45233140-2 | Roboty drogowe                                                                                                                            |                 104 |
|  2021 | Świętokrzyskie      | 33140000-3 | Materiały medyczne                                                                                                                        |                  66 |
|  2021 | Świętokrzyskie      | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  56 |
|  2021 | Świętokrzyskie      | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  54 |
|  2022 | Świętokrzyskie      | 45000000-7 | Roboty budowlane                                                                                                                          |                 520 |
|  2022 | Świętokrzyskie      | 45233140-2 | Roboty drogowe                                                                                                                            |                 108 |
|  2022 | Świętokrzyskie      | 33140000-3 | Materiały medyczne                                                                                                                        |                  85 |
|  2022 | Świętokrzyskie      | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  82 |
|  2022 | Świętokrzyskie      | 60100000-9 | Usługi w zakresie transportu drogowego                                                                                                    |                  68 |
|  2023 | Świętokrzyskie      | 45000000-7 | Roboty budowlane                                                                                                                          |                 392 |
|  2023 | Świętokrzyskie      | 45233140-2 | Roboty drogowe                                                                                                                            |                 134 |
|  2023 | Świętokrzyskie      | 33140000-3 | Materiały medyczne                                                                                                                        |                 103 |
|  2023 | Świętokrzyskie      | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  80 |
|  2023 | Świętokrzyskie      | 45233120-6 | Roboty w zakresie budowy dróg                                                                                                             |                  69 |
|  2024 | Świętokrzyskie      | 45000000-7 | Roboty budowlane                                                                                                                          |                 387 |
|  2024 | Świętokrzyskie      | 45233140-2 | Roboty drogowe                                                                                                                            |                 110 |
|  2024 | Świętokrzyskie      | 33140000-3 | Materiały medyczne                                                                                                                        |                 101 |
|  2024 | Świętokrzyskie      | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                  95 |
|  2024 | Świętokrzyskie      | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  77 |
|  2025 | Świętokrzyskie      | 45000000-7 | Roboty budowlane                                                                                                                          |                 392 |
|  2025 | Świętokrzyskie      | 45233140-2 | Roboty drogowe                                                                                                                            |                 112 |
|  2025 | Świętokrzyskie      | 71320000-7 | Usługi inżynieryjne w zakresie projektowania                                                                                              |                 104 |
|  2025 | Świętokrzyskie      | 33140000-3 | Materiały medyczne                                                                                                                        |                  98 |
|  2025 | Świętokrzyskie      | 80000000-4 | Usługi edukacyjne i szkoleniowe                                                                                                           |                  72 |

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
