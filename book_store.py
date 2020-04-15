
"""
Zadanie z obiektowości.
Spróbujemy zrobić mini sklep internetowy.
W tym przypadku sprzedawać będziemy książki ale starajmy się
tak przygotować program by był gotowy na produkty innego typu
Za bazę posłuży nam plik Excel (lub CSV).
Załączm przykład pliku jak i przykład struktury obiektów
"""


class Book(object):

    vat = 0.23

    def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.cena = cena
        self.vat = 7


class Ebook(Book):
    def __init__(self, autor, tytul):
        super().__init__(autor, tytul)
        self.format = 'pdf'
        self.vat = 23


class Cart():
    def __init__(self):
        self.element = []
        self.element_number = 0
        self.netto = 0
        self.brutto = 0  
        self.__marza = 0.1

    def dodaj(self, element):
        self.element.append(element)
        self.element_number += 1
        self.netto = self.netto + element.cena
        self.brutto = self.brutto + element.cena_brutto()

    def __len__(self):
        return len(self.element)

    def wartosc_netto(self):
        return self.netto

    def wartosc_brutto(self):
        return self.brutto


def __str__(self):
    return f"Kupiłeś książki :   za {self.brutto} zł brutto"


@property
def brutto(self):
        return (self.netto *(1 + self.__marza)*(1 + self.vat)).__round__(2)


cart = Cart()


ksiazka_1 = Book('Potop', 'Sienkiewicz', 300)
ksiazka_2 = Book('Trylogia', 'Sienkiewicz', 1300)
ebook_1 = Ebook('Potop', 'Sienkiewicz')


Cart.dodaj(ksiazka_1)
Cart.dodaj(ksiazka_2)
Cart.dodaj(ebook_1)

print(f"Ilosc w koszyku: {len(Cart)}")
print(f"Wartość netto: {Cart.wartosc_netto()}")
print(f"Wartość netto: {Cart.wartosc_brutto()}")

# do zrobienia:
# ogarnięcie czemu tutaj len(Cart) wywala jako błąd a wcześniej nie
# dodanie by pobierało informację o książkach z csv albo xlxs
# dodanie remove_items_from_cart
# zrobić ładne podsumowanko



def menu():
    # 1. pokaz produkty
    # 2. dodaj produkt do koszyka
    # 3. pokaz koszyk
    # 4. kupno
    pass

