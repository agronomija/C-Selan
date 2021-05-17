import datetime
import collections
import requests

def easter_date(year):
    A = year % 19
    #print(f'A: {A}')
    B = year // 100
    #print(f'B: {B}')
    C = year % 100
    #print(f'C: {C}')
    D = B // 4
    #print(f'D: {D}')
    E = B % 4
    #print(f'E: {E}')
    G = (8 * B + 13) // 25
    #print(G)
    H = (19 * A + B - D - G + 15) % 30
    #print(f'H ostanek: {H}')
    M = (A + 11 * H) // 319
    #print(f'M: {M}')
    J = C // 4
    #print(f'J: {J}')
    K = C % 4
    #print(f'K: {K}')
    L = (2 * E + 2 * J - K - H + M + 32) % 7
    #print(f'L: {L}')
    N = (H - M + L + 90) // 25
    #print(f'N: {N}')
    P = (H - M + L + N + 19) % 32
    #print(f'P: {P}')
    DL = (2 * E + 2 * J - K) % 7
    #print(f'DL: {DL}')
    #print(datetime.date(year, A, P))
    return datetime.date(year, N, P)


def all_hollidays(year):
    prvi_januar = datetime.date(year, 1, 1)
    drugi_januar = datetime.date(year, 1, 2)
    presernov_dan = datetime.date(year, 2, 8)
    okupator = datetime.date(year, 4, 27)
    velikonocni_ponedeljek = easter_date(year)
    praznik_dela = datetime.date(year, 5, 1)
    drugi_maj = datetime.date(year, 5, 2)
    dan_drzavnosti = datetime.date(year, 6, 25)
    marijino_vnebovzetje = datetime.date(year, 8, 15)
    dan_mrtvih = datetime.date(year, 11, 1)
    dan_reformacije = datetime.date(year, 10, 31)
    bozic = datetime.date(year, 12, 25)
    dan_samostojnosti = datetime.date(year, 12, 26)


def prazniki_slovar(year):
    slovar = {
        'prvi_januar': datetime.date(year, 1, 1),
        'drugi_januar': datetime.date(year, 1, 2),
        'presernov_dan': datetime.date(year, 2, 8),
        'okupator': datetime.date(year, 4, 27),
        'velikonocni_ponedeljek': easter_date(year),
        'praznik_dela': datetime.date(year, 5, 1),
        'drugi_maj': datetime.date(year, 5, 2),
        'dan_drzavnosti': datetime.date(year, 6, 25),
        'marijino_vnebovzetje': datetime.date(year, 8, 15),
        'dan_mrtvih': datetime.date(year, 11, 1),
        'dan_reformacije': datetime.date(year, 10, 31),
        'bozic': datetime.date(year, 12, 25),
        'dan_samostojnosti': datetime.date(year, 12, 26)
    }
    return slovar




print(easter_date(2001))
print(prazniki_slovar(2001))


prazniki = prazniki_slovar(2001)
r = requests.post('nek url', data=prazniki)




