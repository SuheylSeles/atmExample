print("""

ATM MAKİNESİ HOŞGELDİNİZ

1)BAKİYE SORGULAMA

2)PARA YATIRMA 

3)PARA ÇEKME

Programdan Çıkmak İçin q ya basınız..

""")


bakiye = 2000
while True:
    islem = input("İşlemi Seçiniz : ")
    if(islem == "q"):
        print("Yine bekleriz.. :)")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tl dir.. ".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktarı Giriniz : "))
        bakiye = bakiye + miktar
    elif(islem == "3"):
        miktar = int(input("Miktarı Giriniz : "))
        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsin!!!")
            continue
        bakiye = bakiye - miktar

