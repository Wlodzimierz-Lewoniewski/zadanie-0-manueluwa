import re

ile_zdan = int(input("Ile zdań? "))

zdania = []
for z in range(ile_zdan):
    zdania.append(input("Wprowadź zdanie " + str(z + 1) + ": "))
#print("Wprowadzone zdania:", zdania)

slowa_zdania = [[slowo.strip() for slowo in re.split(r'[,\.\?!: ]+', z.lower()) if slowo] for z in zdania]
#print("Lista słów w zdaniach:", slowa_zdania)

ile_slow = int(input("Ile słów do wyszukania? "))
slowa_do_wyszukania = []
for z in range(ile_slow):
    slowa_do_wyszukania.append(input("Wprowadź słowo " + str(z + 1) + ": ").lower())

output = {slowo: [0] * ile_zdan for slowo in slowa_do_wyszukania}

for i, slowa in enumerate(slowa_zdania):
    for slowo in slowa:
        if slowo in output:
            output[slowo][i] += 1

sort_output = {}

for slowo, wystapienia in output.items():
    indeksy_zdan = [i for i in range(len(wystapienia)) if wystapienia[i] > 0]

    indeksy_zdan.sort(key=lambda i: (-wystapienia[i], i))

    sort_output[slowo] = indeksy_zdan

for indeksy in sort_output.values():
        print(indeksy)

#Przykład otrzymania wartości wprowadzonej przy użyciu funkcji input().

#W celu poprawnego działania kodu w ramach GitHub Classroom warto dodatkowo użyć funkcję strip()
#To pozwoli na usunięcie spacji oraz innych "spacjopodobnych" znaków (tabulacja \t', przejście do nowej linii '\n' lub '\r' etc.) z "głowy" i "ogona" (lewej i prawej części wyrazu).
#wyraz=wyraz.strip()

#Wydruk na ekranie (w konsoli)
#print ('Ten wyraz został wprowadzony:', wyraz)
