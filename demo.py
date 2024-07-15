"""
ogrenciler  = {
'120' : {
'ad' : 'ali',
'soyad' : 'yılmaz',
'telefon' : '532 000 00 01'
},
'125' : {
'ad' : 'can',
'soyad' : 'korkmaz',
'telefon' : '552 000 00 02'
},
{
'128' : {
'ad' : 'volkan',
'soyad' : 'yükselen',
'telefon' : '532 000 00 03'
},
}
1- bilgerli verilen öğrencileri kullancıdan aldığınız bilgilerle dictionary içinde saklayın
2- öğrenci numarasını kullınıcıdan alıp ilgili öğrenci bilgisini gösterin.
"""

ogrenciler = {}
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }

ogrenciler.update({ #update kullanıldığında birden fazla veriyi aynı anda ekleme şansımız vardır.
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")
ogrenciler.update({
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")
ogrenciler.update({
        number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

print('*'*50)


ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
print(f"Aradğınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonuysa {ogrenci['telefon']}")
