cuvant_ales = "alfabet"

cuvant = list(cuvant_ales)



numar_incercari = 7

greseli = []

cuvant_curent = list("")
for i in cuvant:
    if cuvant[0] != i and cuvant[-1] != i:
        cuvant_curent += "_"
    else:
        cuvant_curent += i
print(cuvant_curent)
# print(i)

while cuvant_curent != cuvant:
    litera_aleasa = input("spune o litera:")

    if litera_aleasa in greseli or litera_aleasa in cuvant_curent:
        print("Litera a fost de aleasa, te rugam sa alegi alta")

    elif not litera_aleasa.isalpha():
        print("Introdu o litere")

    elif litera_aleasa in cuvant:
        for pozitie, valoare in enumerate(cuvant):
            if valoare == litera_aleasa:
                cuvant_curent[pozitie] = litera_aleasa
                print(pozitie, valoare)

        print(f"cuvantul este {cuvant_curent}")
    else:
        greseli.append(litera_aleasa)
        numar_incercari -=1
        print(f"Gresit, mai ai {numar_incercari} incercari")

if numar_incercari > 0:
     print(f"Ai castigat,cuvantul este {cuvant}")
else:
    print(f"Ai piersut, cuvantul corect era:{cuvant}")