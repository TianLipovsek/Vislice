import random
from re import A

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'




class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke is None else crke

    def napacne_crke(self):
        sez = []
        for element in self.crke:
            if element not in self.geslo:
                sez.append(element)
        return sez
    
    def pravilne_crke(self):
        sez = []
        for element in self.crke:
            if element in self.geslo:
                sez.append(element)
        return sez
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK
           
    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            if crka in self.crke:
                s += crka + ' '
            else:
                s += '_ '
        return s.strip()

    def nepravilni_ugibi(self):
        return ''.join(self.napacne_crke())
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else: 
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else: 
                    return NAPACNA_CRKA


with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))