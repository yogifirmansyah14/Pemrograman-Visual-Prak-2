# Moch Yogi Firmansyah
# 20051397044
# MI 2020 B

class tabung:
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume(self):
        pi = 22/7
        self.l_alas = pi * self.jari * self.jari
        self.volume = self.l_alas * self.tinggi
        print ("Volume Tabung = ", self.volume)
        print(" ")

class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume (self):
        self.l_alas = self. panjang * self.lebar
        self.volume = self.l_alas * self.tinggi
        print ("Volume Balok = ", self.volume)
        print (" ")

class prisma_segitiga:
    def __init__(self, alas, tinggi, tinggi_prisma):
        self.alas = alas
        self.tinggi = tinggi
        self.tinggi_prisma = tinggi_prisma

    def volume (self):
        self.l_alas = self.alas * self.tinggi / 2
        self.volume = self.l_alas * self.tinggi_prisma
        print ("Volume Prisma Segitiga = ", self.volume)

tabung = tabung(7,10)
balok = balok(5,6,9)
prisma_segitiga = prisma_segitiga(4,2,12)

for hasil in (tabung, balok, prisma_segitiga):
    hasil.volume()

'''
       OutPutnya

Volume Tabung =  1540.0
 
Volume Balok =  270
 
Volume Prisma Segitiga =  48.0

'''
