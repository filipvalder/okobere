#!/usr/bin/python3

# import funkce randrange
from random import randrange

# vychozi hodnoty
body = 0
platna_odpoved = True

# vlastni cyklus
while body < 21:
    if platna_odpoved:
        print('Máš', body, 'bodů...')

    # verime, ze dostaneme platnou odpoved (a, A, n, N, y, Y :-))
    platna_odpoved = True

    # ...co nam rekne uzivatel(ka)?
    rozhodnuti = input('Pokračujeme? ')
    if rozhodnuti and rozhodnuti in 'nN':
        break
    elif rozhodnuti and rozhodnuti in 'aAyY':
        body += randrange(2, 11)
    # dostali jsme neplatnou odpoved :-(
    else:
        platna_odpoved = False

# zhodnoceni vysledku
if body == 0:
    print('Tos to vzdal(a) trochu brzy, nemyslíš???')
elif body == 21:
    print('Celkem', body, 'bodů, vyhrál(a)s! :-)')
elif body > 21:
    print('Celkem', body, 'bodů, prohrál(a)s! :-(')
elif body < 21:
    # TODO
    print('To nebylo špatné! Zbývalo ti', 21-body, 'bodů.')
else:
    print('Uh???')
