'''
Enkelt Python spill:
riktig nummer.
'''
import random

ANTALL_SIFFER = 3
MAKS_FORSØK = 10

def main():
    print('''Gjett riktig nummer,
    du har tre forsøk.
    Lykke til!

    Jeg tenker på et tall med {} antall siffer, uten repeterende siffer
    Prøv å gjett nummeret. Her er noen tips til hjelp:
    Når jeg sier:      Betyr det:
    Alpha            Ett siffer er riktig men i feil posisjon.
    Gamma            Ett siffer er riktig og i riktig posisjon.
    Sigma            Ingen siffer er riktig.

    For eksempel, hvois det hemmelige nummeret er 248 og du gjettet
    843, hintene ville vært Fermi Pico.'''.format(ANTALL_SIFFER))

    #Main loop
    while True:
        #det hemmelige nummeret som må gjettes
        hemmeligNummer = hentHemmeligNummer()
        print('Jeg har tenker på et nummer.')
        print('Du  har {} antall forsøk på å gjette det'.format(MAKS_FORSØK))

        gjetningNr = 1
        while gjetningNr <= MAKS_FORSØK:
            gjett = ''
            #loopen fortsetter til gyldig forsøk
            while len(gjett) != ANTALL_SIFFER or not gjett.isdecimal():
                print('Gjetning nr #{}: '.format(gjetningNr))
                gjett = input('> ')

            hint = fåHint(gjett, hemmeligNummer)
            print(hint)
            gjetningNr += 1

            if gjett == hemmeligNummer:
                break
            if gjetningNr > MAKS_FORSØK:
                print('Du har ikke flere forsøk igjen.')
                print('Det riktige svaret var {}.'.format(hemmeligNummer))

        #Spør om spilleren vil spille på nytt
        print('Vil du spille igjen? (ja eller nei)')
        if not input('> ').upper().startswith('Y'):
            break

    print('Takk for at du spillte!')

def hentHemmeligNummer():
    '''returnerer en string laget på ANTALL_SIFFER unike tilfeldige nummer'''
    nummere = list('0123456789') #lager en liste med siffer fra 0-9
    random.shuffle(nummere)
    #henter sifferene fra den tilfeldig sorterte listen
    hemmeligNummer = ''
    for i in range(ANTALL_SIFFER):
        hemmeligNummer += str(nummere[i])
    return hemmeligNummer

def fåHint(gjett, hemmeligNummer):
    ''' returnerer en string med hint '''
    if gjett == hemmeligNummer:
        return 'DU GJETTET RIKTIG!'

    hint = []

    for i in range(len(gjett)):
        if gjett[i] == hemmeligNummer[i]:
            # Et korrekt siffer er på korrekt plass
            hint.append('Gamma')
        elif gjett[i] in hemmeligNummer:
            # Et korrekt siffer er på feil plass
            hint.append('Alpha')
        if len(hint) == 0:
            return 'Sigma' #Ingen korrekte siffer
        else:
            #Sorterer hintene alfabetisk slik at
            #de ikke gir informasjon om posisjonen vekk
            hint.sort()
            #Omgjør listen til en returnerbar string
            return ' '.join(hint)



#For å kjøre spillet
if __name__ == '__main__':
    main()




















