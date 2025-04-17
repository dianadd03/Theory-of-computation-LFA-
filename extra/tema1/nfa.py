# TURCU ANDREI CRISTIAN
# Grupa 152
# Python3

stare_initiala = ""
relatie = {}
stari_finale = set()
stari_ignorate = set()
stari = set()
litere = set()
litere_ignorate = set()


def States_Reader():
    global nod_ignorat, stare_initiala, stari, f
    linie = f.readline()
    while linie != "End\n" and linie != "":
        linie = linie.strip()
        cuvinte = linie.split()
        cuvinte = [cuv.strip(',') for cuv in cuvinte]
        if cuvinte != []:
            if cuvinte[0] == "#":
                stari_ignorate.add(cuvinte[1])
            else:
                stari.add(cuvinte[0])
                relatie.update({cuvinte[0]: {}})

                for i in range(1, len(cuvinte)):
                    if cuvinte[i] == "S":
                        if stare_initiala != "":
                            print("Atentie! automatul are mai multe stari initiale...")
                        stare_initiala = cuvinte[0]
                    if cuvinte[i] == "F":
                        stari_finale.add(cuvinte[0])
        linie = f.readline()
    return


def Sigma_Reader():
    global litere_ignorate, litere, f
    linie = f.readline()
    while linie != "End\n" and linie != "":
        linie = linie.strip()
        if linie != []:
            if linie[0] == "#":
                litere_ignorate.add(linie[1])
            else:
                litere.add(linie[0])
        linie = f.readline()
    return


def Transition_Reader():
    global f, relatie
    linie = f.readline()
    linie=linie.strip('\n')
    while linie != "End" and linie != "":
        linie = linie.strip()
        cuvinte = linie.split()
        cuvinte = [cuv.strip(',') for cuv in cuvinte]
        if cuvinte != []:
            if cuvinte[0][0] != "#":
                x = cuvinte[0]
                y = cuvinte[2]
                litera = cuvinte[1]

                if x in stari_ignorate or y in stari_ignorate:
                    print("stare_ignorata!!!")
                else:
                    if litera not in relatie[x]:
                        set_gol = set()
                        relatie[x].update({litera: set_gol})
                    relatie[x][litera].add(y)
        linie = f.readline()
    return


def Cuvant_Valid(cuvant, stare_curenta):
    if cuvant == "":
        if stare_curenta in stari_finale:
            # print("here")
            return 1
        else:
            return 0

    litera = cuvant[0:1]

    if litera not in relatie[stare_curenta]:
        return 0

    for stare_viitoare in relatie[stare_curenta][litera]:
        if Cuvant_Valid(cuvant[1:], stare_viitoare):
            return 1

    return 0


# ---------------------------------MAIN---------------------------------------------------------------------
f = open("nfa_config_file.txt", "r")
linie = f.readline()
while linie!="" :
    if linie == "States:\n" :
        States_Reader()
    linie = f.readline()
f.close()
f = open("nfa_config_file.txt", "r")
linie = f.readline()
while linie != "":
    if linie == "Sigma:\n":
        Sigma_Reader()
    linie = f.readline()
f.close()

f = open("nfa_config_file.txt", "r")
linie = f.readline()
while linie != "":
    if linie == "Transitions:\n":
        Transition_Reader()
    linie = f.readline()
f.close()
f = open("input.txt", "r")

cuvant = f.readline()
while cuvant != "":
    cuvant = cuvant.strip()
    if Cuvant_Valid(cuvant, stare_initiala):
        print(cuvant + "  acceptat!")
    else:
        print(cuvant + "  refuzat!")
    print("------------------------")
    cuvant = f.readline()

f.close()


# comentata o relatie ---> nu fac nimic?...
# comentat o stare ---> semnalez daca e necesara -> daca nu mai apare ulterior/precedent?... -> daca sunt mai multe asfel de stari si nu am un
#                       raspuns valid atunci le trec pe toate?...
# comentat o litera ---> ce fac...

# daca automatul are mai multe stai intiale
# un cuvant ce trebuie verificat poate fi format din mai multe litere gen cuvantul "aabbacab" sa fie interpretat ca "aa|b|bac|ab"?
# trb mentionat ce fel de automat este?
# daca pot primi cuvinte vide -> cum citesc cuvantul vid..


# faptul ca redeschid un fiser de 3 ori este o abominatie?


