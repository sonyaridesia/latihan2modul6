#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:52:50 2022

@author: sonyaridesia
"""
print ("Program ini akan menentukan jumlah hari dalam bulan tertentu")

F = False

year = ''

#Fungsi Tidak Berparameter
def Kabisat(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        print("29 hari dalam sebulan")
    else:
        print("28 hari dalam sebulan")
        
#Fungsi Berparameter
def NonKabisat(bulan):
   if bulan in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
       if bulan in [4, 6, 9, 11]:
           print("30 hari dalam sebulan")
       elif bulan in [1, 3, 5, 7, 8, 10, 12]:
           print("31 hari dalam sebulan")
       elif bulan == 2:
           year = int(input("masukkan tahun (e.g., 2021): "))
           Kabisat(year) #Melempar Nilai Kedalam Fungsi Berparameter
   else:
       print("Error")
        
while (not F):
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("Masukan bulan 1-12 : "))
    if bulan == 0:
        F = True
    else:
        NonKabisat(bulan) #Melempar Nilai kedalam Fungsi Berparameter
        print ("Terima Kasih sudah menggunakan program saya, smapai berjumpa lagi")