# Moch Yogi Firmansyah
# 20051397044
# MI 2020 B

import math
from abc import ABC, abstractmethod
class persegi(ABC):
    #Abstrak Method Persegi
    @abstractmethod
    def luas_persegi(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling_persegi(self):
        return 4 * self.__sisi

class segitiga(ABC):
    #Abstrak Method Segitiga Siku-Siku
    @abstractmethod
    def luas_segitiga(self):
        return self.__alas * self.__tinggi / 2

    def keliling_segitiga(self):
        return self.__alas + self.__tinggi + self.__miring

class jajar_genjang(ABC):
    #Abstrak Jajar Genjang
    @abstractmethod
    def luas_jajar_genjang(self):
        return self.__alas * self.__tinggi

    abstractmethod
    def keliling_jajar_genjang(self):
        return (self.__alas * 2) + (self.__samping * 2)

class persegi (persegi):
    def __init__(self, sisi):
        self.__sisi = sisi

    def luas_persegi(self):
        return self.__sisi * self.__sisi

    def keliling_persegi(self):
        return 4 * self.__sisi

class segitiga (segitiga):
    def __init__(self, alas, tinggi):
        self.__alas = alas
        self.__tinggi = tinggi

    def luas_segitiga(self):
        return self.__alas * self.__tinggi / 2

    def keliling_segitiga(self):
        self.a = self.__alas * self.__alas
        self.b = self.__tinggi * self.__tinggi 
        self.__miring = math.sqrt(self.a + self.b)
        return self.__alas + self.__tinggi + self.__miring

class jajar_genjang(jajar_genjang):
    def __init__(self, alas, tinggi, samping):
        self.__alas = alas
        self.__tinggi = tinggi
        self.__samping = samping

    def luas_jajar_genjang(self):
        return self.__alas * self.__tinggi
    
    def keliling_jajar_genjang(self):
        return (self.__alas * 2) + (self.__samping * 2)     

#kotak = persegi(sisi)
kotak = persegi(7)
print ("Luas Persegi = ",kotak.luas_persegi())
print ("Keliling Persegi = ",kotak.keliling_persegi())
#Hasilnya :
#Luas Persegi = 49
#Keliling Persegi = 28


#segitiga = segitiga(alas, tinggi)
segitiga = segitiga(3,4)
print (" ")
print ("Luas Segitiga Siku-Siku = ",segitiga.luas_segitiga())
print ("Keliling Segitiga Siku-Siku = ",segitiga.keliling_segitiga())
#Hasilnya :
#Luas Segitiga Siku-Siku = 6
#Keliling Segitiga Siku-Siku = 12

#jajar_genjang = jajar_genjang(alas, tinggi, sisi miring)
jajar_genjang = jajar_genjang(3,4,5)
print (" ")
print ("Luas Jajar Genjang = ", jajar_genjang.luas_jajar_genjang())
print ("Keliling Jajar Genjang = ", jajar_genjang.keliling_jajar_genjang())
#Hasilnya :
#Luas Jajar Genjang = 12
#Keliling Jajar Genkang = 16
