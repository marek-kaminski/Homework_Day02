
"""""""""
6) Stworzenie "programu nakładki" na dotychczasowe programiki.
   Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
   Sugeruje by każdy "podprogram był oddzielną funkcją".
   Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram" - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )
   Przykład przy uruchomieniu:
   "
   Witaj w Multitool Python Program by iSA - wersja beta ;)
   Wybierz program który cię interesuje:
   1) Rysowanie kwadratu o zadanych parametrach
   2) Rysowanie piramidy o określonej wysokości
   3) Rozmienianie pieniędzy
   4) Przeliczanie F->C
   5) Przeliczanie C->F
   6) ...
   7) ...
   R) Wybierz program losowo bo nie wiem czego szukam:)
   X) Wyjście z programu
   Twój wybór: _
"""""""""

interface = float(input("Witaj w multitoolu zrobionym w pythonie. \n"
                  "Tutaj masz do wyboru wszystkie programy dotejpory zrobione.\n"
                  "Podaj który program chcesz wybrać:\n"
                  "1) Zamina temperatury z C na F i na odwrót.\n"
                  "2) Obliczanie pola koła\n"
                  "3) Podanie pierwszej i ostatniej cyfry danego numeru\n"
                  "4) Rysowanie kwadratu\n"
                  "5) Zamiana liczb binarnych na zwykłe\n"
                  "6) Sprawdzanie liczb parzystych\n"
                  "7) Sprawdzanie dzielności przez 3, 5 lub 7\n"
                  "8) Sprawdzanie dzielności przez 3 i 5 i 7\n"
                  "9) Szukanie roku przestępnego\n"
                  "10) Rysowanie tabeli do  listy \n"
                  "11) Wydawanie reszty\n"
                  "12) Rysowanie piramidy\n"
                  "13) Kalkulator psiego wieku\n"
                  "14) Losowy program, jeszcze nie dizała\n"
                  "Podaj liczbę: "))


# Zadanie 1   przepisanie dotychczasowych proagramów z pierwszego zadania domowego z wykorzystaniem
# definiowania własnych funkcji i wytycznych powyżej


def hw_conversion_temperature():
    start = input("Jaką temperaturę chcesz podać? Stopnie Farenheita  czy celsjusza? (F/C)")
    if start == "F":
        input_temperature = input("Podaj temperaturę")
        input_temperature_float = float(input_temperature)
        temperature = (5 / 9) * (input_temperature_float - 32)
        end = "To będzie dokładnie "
        stopnie = " stopni Celsjusza"
        print(end, temperature, stopnie)
    elif start == "C":
        input_temperature = input("Podaj temperaturę")
        input_temperature_float = float(input_temperature)
        temperature = (9 / 5) * input_temperature_float + 32
        end = "To będzie dokładnie "
        stopnie = " stopni Farenheita"
        print(end, temperature, stopnie)
    else:
        print("Niestety musisz podać  Celsjusza albo Farenhiety")


def circle_radiance():
    r = input("Podaj promień koła")
    r_float = float(r)
    pi = 3.14
    pole = pi * (r_float **2)
    print ("pole koła to ", pole)


def first_and_last_number():
    number = input("Podaje cyfre")
    print ("Pierwsza liczba to ", number[0], " a ostatnia to ", number[-1])


def drawing_square():
    height = input("Podaj jaka ma być wysokość prostokąta")
    depth = input("Podaj jaka ma być szerokość prostokąta")
    height_int = int(height)
    depth_int = int(depth)
    depth_up = "-"*depth_int
    middle = " "*depth_int
    height_front ="|"*height_int
    print('+',depth_up,"+")
    while height_int > 0:
        height_int = height_int-1
        print('|',middle,"|")
    else:
        print('+',depth_up,"+")


def simple_binary_conversion():
    binary = input("Proszę podaj liczbę w systemie binarnym")
    num1 = binary[-1]
    num2 = binary[-2]
    num3 = binary[-3]
    num4 = binary[-4]
    num5 = binary[-5]
    num6 = binary[-6]
    digit_number = 0
    if num1 == "1":
        digit_number = digit_number + (1 * 2**0)
    if num2 == "1":
        digit_number += (1 * 2**1)
    if num3 == "1":
        digit_number += (1 * 2**2)
    if num4 == "1":
        digit_number += (1 * 2**3)
    if num5 == "1":
        digit_number += (1 * 2**4)
    if num6 == "1":
        digit_number = digit_number + (1 * 2**5)
    print(digit_number)


def check_for_even_numbers():
    number = input("Podaj liczbę")
    number_float = float(number)
    test = number_float % 2
    print(test)
    if test > 0:
        print("Twoja liczba jest nieparzysta")
    else:
        print("Twoja liczba jest parzysta")


def check_for_dividend():
    number = input("Podaj liczbę")
    number_float = float(number)
    test_3 = number_float % 3
    test_5 = number_float % 5
    test_7 = number_float % 7
    if test_3 == 0:
        print("Twoja liczba jest podzielna przez 3")
    elif test_5 == 0:
        print("Twoja liczba jest podzielna przez 5")
    elif test_7 == 0:
        print("Twoja liczba jest podzielna przez 7")
    else:
        print(" Twoja liczba nie jest podzielna ani przez 3, ani 5 ani przez 7.")


def check_for_common_divident():
    number = input("Podaj liczbę")
    number_float = float(number)
    test_3 = number_float % 3
    test_5 = number_float % 5
    test_7 = number_float % 7
    if test_3 + test_5 + test_7 == 0:
        print ("Twoja liczba jest podzielna przez 3, 5 oraz 7")
    else:
        print("Twoja liczba niestety nie jeste podzielna przez 3, 5 oraz 7")


def check_for_leap_year():
    year = input("Podaj rok, który chcesz sprawdzić")
    year_float = float(year)
    if year_float%4 == 0 and year_float%100 != 0:
        print("Ten rok  jest rokiem przestępnym")
    elif year_float%400 == 0:
        print("Ten rok jest rokiem przestępnym")
    else:
        print("Ten rok nie jest rokiem przestępnym")


# Zadanie 2   2) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany
#    do lewej.Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy
#    trzema kropkami. A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela
#    z odpowiednią ilością wierszy i kolumn :)


# list_input = input("Proszę podać listę:")
def drawing_list():
    example_list = ["to", "przykładowa", "lista", "miłego", "dnia", ":)"]

    def drawing_first_line():
        counter_list1 = 0
        list_lenght1 = len(example_list)
        while list_lenght1 > 0:
            print("+" + "-" + "-" * len(example_list[counter_list1]), end="")

            list_lenght1 += -1
            counter_list1 += 1
        print("+")

    drawing_first_line()
    counter_list = 0
    list_lenght = len(example_list)
    internal_counter = 0
    print("|", end="")
    while list_lenght > 0:
        print(example_list[internal_counter] + " |", end="")
        internal_counter += 1
        list_lenght += -1
    print(" ")
    drawing_first_line()


# Zadanie 3 Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1
# wydając ich jak najmniej.
def counting_money():

    money = float(input("Proszę podać kwotę: "))
    five_zloty = money // 5
    print("Twoja reszta będzie wynosić: ")
    if five_zloty > 1:
        money = money - five_zloty*5
        print(str(five_zloty) + " monet pięcio złotowych ")
    two_zloty = money // 2
    if two_zloty > 1:
        money = money - two_zloty*2
        print(str(two_zloty) + " monet dwu złotowych ")
    one_zloty = money // 1
    if one_zloty > 1:
        money = money - one_zloty
        print(str(one_zloty) + " monet jedno złotowych ")
    fifty_groszy = money // 1
    if fifty_groszy > 1:
        money = money - fifty_groszy*0.5
        print(str(fifty_groszy) + " monet pięćdziesięcio groszowych ")
    twenty_groszy = money //1
    if twenty_groszy > 1:
        money = money - twenty_groszy*0.2
        print(str(twenty_groszy) + " monet dwudziesto groszowych ")
    ten_groszy = money//0.1
    if ten_groszy > 1:
        money = money - ten_groszy*0.1
        print(str(ten_groszy) + " monet dziesięcio groszowych ")
    five_groszy = money//0.05
    if five_groszy > 1:
        money = money - five_groszy*0.05
        print(str(five_groszy) + " monet pięcio groszowych ")
    two_groszy = money//0.02
    if two_groszy > 1:
        money = money - two_groszy*0.02
        print(str(two_groszy) + " monet dwu groszowych ")
    one_groszy = money//0.01
    if ten_groszy > 1:
        money = money - one_groszy*0.01
        print(str(one_groszy) + " monet jedno groszowych ")
    if money != 0:
        print("Niestety nie można wydać pełnej reszty")
# print(counting_money())


# Zadanie 4  Program rysujący piramidę o określonej wysokości, np dla 3 złożoną z giazdek
def pyramid():
    user_input = input("Proszę podaj ile pięter ma mieć piramida")
    user_input_int = int(user_input)
    revers = 1

    while user_input_int > 0:

        print((" " * user_input_int) + ("#" * revers) + (" " * user_input_int))
        revers += 2
        user_input_int += -1
# print(pyramid())


# Zadanie 5    Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
def dog_calculator():
    dog_age = float(input("Proszę podaj wiek swojego pieska"))
    if dog_age <= 2:
        human_years = 10.5 * dog_age
    else:
        human_years = (2*10.5) + (dog_age - 2) * 4
    print("Twój piesek ma " + str(human_years) + " lat. :)")
# print(dog_calculator())


if interface == 1:
    print(hw_conversion_temperature())
if interface == 2:
    print(circle_radiance())
if interface == 3:
    print(first_and_last_number())
if interface == 4:
    print(drawing_square())
if interface == 5:
    print(simple_binary_conversion())
if interface == 6:
    print(check_for_even_numbers())
if interface == 7:
    print(check_for_dividend())
if interface == 8:
    print(check_for_common_divident())
if interface == 9:
    print(check_for_leap_year())
if interface == 10:
    print(drawing_list())
if interface == 11:
    print(counting_money())
if interface == 12:
    print(pyramid())
if interface == 13:
    print(dog_calculator())
if interface == 14:
    print("Ten program jest jeszcze nie gotowy")
else:
    print ("wybierz normalny numerek z listy")


