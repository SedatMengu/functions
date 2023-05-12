# fonkisyonlara neden ihtiyaç duyarız: 

# birden fazla kere kullanacağımız bir kod parçasını fonksiyon olarak tanımlarsak eğer daha efektif olabilir.
# örneğin çıktı metnini değiştirmemiz gerektiğinde teker teker ifadelerin tamamını değiştirmek yerine fonksiyonu güncellemek yeterli olur.
# örnek : bir web sitesi akışı içerisinde birden fazla kere işlem başarılı sonucu döndürülebilir. 
            # bunu fonksiyon olmadan yaparsak aşağıdaki gibi bir manzara oluşurdu.
            # işlem başarılı yerine işlem başarılı bir şekilde gerçekleşti olarak değiştirmek istersek tek tek yapmamız gerekir.


print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")

# eğer yukardaki işlemi fonksiyon yardımı ile yapacak olursak:

def bildirim():
    print("İşlem Başarılı")

bildirim()
bildirim()
bildirim()
bildirim()
bildirim()
bildirim()
bildirim()

# çıktı ekranı aynı olacak ancak metini değiştirmek istersek sadece fonksiyonu değiştirmemiz yeterlidir.
# bu seepten dolayı fonksiyonlara ihtiyaç duyarız.


# 2 farklı fonksiyon vardır. 
#   1 - parametre almayan fonksiyonlar
#   2 - parametre alan fonksiyonlar

# 1 - parametre almayan fonksiyon iskelet yapısı:

# def fonksiyon ():
# // kodlar

# fonksiyonu çağırmak için 

# fonksiyon()

# örnek:

def selamla():
    print("merhaba")

selamla()                        #/ merhaba


# parametre alan foknksiyon iskelet yapısı:

# def parametreli_fonksiyon (parametre1 , parametre2)
    #// kodlar

# örnek : 

def selamla(isim):
    print("merhaba {}".format(isim))

selamla("Kemal")                # / merhaba kemal
selamla("İhsan")                # / merhaba İhsan
selamla("tayfun")               # / merhaba tayfun

# 2 parametreli fonksiyon örnek

def topla(x,y):
    print("{} ve {} toplamı {} dır".format(x,y,x+y))

topla(4,5)                      # / 4 ve 5 toplamı 9 dır


def birlestir(str1,str2):
    print(str1 + str2)

birlestir("a","b")                      # / ab
birlestir("Merhaba","- dünya")          # / Merhaba- dünya
birlestir("Pythom","- Ögreniyorum")     # / Python- Ögreniyorum


def ortalama_hesapla(liste):
    toplam=sum(liste)
    adet=len(liste)
    ortalama= toplam/adet
    print("listenin ortalaması : {}".format(ortalama))

ortalama_hesapla([2,3,4,5,6,7,8,9,10])  # liste girmek gerektiği için [] kullandık  # / listenin ortalaması : 6.0


def buyuk_harfe_cevir(metin):
    metin=metin.upper()
    print(metin)

buyuk_harfe_cevir("Ahmet ABASIyanık")           # / AHMET ABASIYANIK

def kucuk_harfe_cevir(metin):
    metin=metin.lower()
    print(metin)

kucuk_harfe_cevir("EN BÜYÜK CİMBOM")            # / en büyük cimbom

# tanımlanan fonksiyonda ne kadar parametre isteniyorsa o kadar girmek gerekir. aksi hale hata alırız.
# bazı parametrelere default değerler atayarak boş geçilmesi durumunda oluşacak hatayı önleyebilriz.

def selamla(mesaj,isim="anonim"):
    print("{} {} ".format(mesaj,isim))

selamla("merhaba")                              # / merhaba anonim


def indirim_yap(fiyat , yuzde=20):              # eğer indirim girmediysek bu indirimi 20 kabul et dedik
    indirim_miktari = fiyat * (yuzde/100)
    indirimli_fiyat = fiyat-indirim_miktari
    print("indirimli fiyat {}".format(indirimli_fiyat))

indirim_yap(100,40)                         # / indirimli fiyat 60.0
indirim_yap(50,10)                          # / indirimli fiyat 45.0


# return kavramı

# kullanacağımız fonksiyonun sonucunu her zaman fonksiyon bitince ekrana bastırmasını istemeyebilriz.
# bu gibi durumlarda return anahtar kelimesi devreye girer. 
# iç içe fonksiyonların kullanılmasında da işe yarar.

# örnek : 

def ortalama_hesapla(x,y):
    return (x + y) /2

ortalama_hesapla(3,7)           # / ortalama_hesapla fonksiyonu print içermediği için hesaplamayı yaptı ancak ekrana bir şey bastırmadı


sonuc = ortalama_hesapla(3,7)
print(sonuc)                    # hesaplanan ortalamayı sonuc değişkeninin içine attık ve print ile sonuc ifadesini ekrana yazarak geçici hafızada tutulan return u kullandık.

# positional arguments: 

# tanımlanan fonksiyonların içerisine alıdığı parametrelere denir.


def kuvvet_al(x,y):             
    return x**y 

print(kuvvet_al(3,4))           # / 81
# print(kuvvet_al(5))           # / TypeError: kuvvet_al() missing 1 required positional argument: 'y'
# print(kuvvet_al(3,4,5))         # / TypeError: kuvvet_al() takes 2 positional arguments but 3 were given

#keyword arguments :

# tanımlanan fonksiyonlarda varsayılan olarak gelen argumanlar olabilir. bunlar keyword arguemts olarak isimlendirilir.

def bilgi_ver(isim,soyisim,yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas) 

print(bilgi_ver("Ahmet","Kuzu"))            # / Ad:Ahmet , soyad: Kuzu , yas: Girilmedi
# print(bilgi_ver("orhan"))                   # TypeError: bilgi_ver() missing 1 required positional argument: 'soyisim'

def bilgi_ver2(isim,soyisim = "Girilmedi",yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas)

print(bilgi_ver2("Halim"))              # / Ad:Halim , soyad: Girilmedi , yas: Girilmedi

# kendime not: fonksiyon tanımlarken boş bırakılmasını uygun gördüğümüz yerlerde default olarak bi ifade tanıtabiliriz. aksi hale hata alırız ve program biter. 


def bilgi_ver3(isim,soyisim="girilmedi",yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas)

print(bilgi_ver3("uğur",34))             # / Ad:uğur , soyad: 34 , yas: Girilmedi / pythonda veri sıralaması önemlidir. fonksyionda belirtildiği şekliyle veri girmek gerekir. eğer bilinmiyorsa şu şekilde yapılabilir.
print(bilgi_ver3("oğuz",yas=34))         # / Ad:oğuz , soyad: girilmedi , yas: 34



# *args argument

# parametrede kaç tane parametre olduğunu bilmediğimiz zamanlarda kullanılır.

def topla2 (x,y):                       # / 2 den az veya çok değer verirsek hata alırız
    return x + y

def topla3 (x,y,z):                     # / 3 den az veya çok değer verirsek hata alırız
    return x+y+z
 
def topla4 (*args):                     # isteğimiz kadar değer girebiliriz.
    return args 

print(topla2(5,6))                                    # / 11
print(topla3(2,3,4))                                  # / 9
print(topla4(1,2,3,4,5,6,7,8,9,True,"Python"))        # / (1, 2, 3, 4, 5, 6, 7, 8, 9, True, 'Python')


def carpim(*args):          # / *args dediğimiz için istediğimiz kadar değer girebiliriz.
    carpim = 1      
    for i in args:
        carpim*=i
    return(carpim)


print(carpim(3,4,5))                # / 60
print(carpim(3,4,5,6,7,8,9))        # / 181440 


def selamla(mesaj,*args):
    print(mesaj)
    print("****************")
    for i in args:
        print(i)
    return "fonksyionun çalışması tamamlandı"

print(selamla("selamlar","nasılsınız","iyi günler","hoşçakalın"))

# / selamlar
# / ****************
# / nasılsınız
# / iyi günler
# / hoşçakalın
# / fonksyionun çalışması tamamlandı


# / ilk arguman mesaj değişkeni içerisine girdi ve ekrana basıldı. diğer bütün argumanlar args ı oluşturdu ve for döngüsü ile teker teker ekrana basıldı.



# / **kwargs arguments : verileri sözlük olarak saklar.

def fonk(**kwargs):
    print(kwargs)


fonk(ad="Ali",soyad="Veli",yas=3)               # / {'ad': 'Ali', 'soyad': 'Veli', 'yas': 3}


def fonk2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("********************")
    for i in args:
        print(i)
    print("********************")
    for j in kwargs:
        print(j)

fonk2(1,2,3,4,5,6,ad="ahmet",soyad="varlı",yas=7)

# 1
# ********************
# 2
# 3
# 4
# 5
# 6
# ********************
# ad
# soyad
# yas


# iç içe fonksiyon kullanımı : 

def dis_fonk():
    print("Dış fonksiyon Çalışıyor")
    def ic_fonk():
        print("iç fonksiyon çalışıyor")
    print("Dış fonksiyon tamamlanıyor...")

dis_fonk()

# / Dış fonksiyon Çalışıyor
# / tam burada ic_fonk oluşturuldu ancak print fonksiyonu ic_fonk un içinde olduğundan çalışmadı.
# / Dış fonksiyon tamamlanıyor... 


# / Eğer iç fonksiyonun da çalışmasını istiyorsak dış fonksiyon çalışırken fonksiyon içinde çalıştırmamız gerekir.

def dis_fonk():
    print("Dış fonksiyon Çalışıyor")
    def ic_fonk():
        print("iç fonksiyon çalışıyor")
    ic_fonk()
    print("Dış fonksiyon tamamlanıyor...")

dis_fonk()

# / Dış fonksiyon Çalışıyor      
# / iç fonksiyon çalışıyor       
# / Dış fonksiyon tamamlanıyor...


# parametreli olarak iç içe fonksiyon örneği 

def hesapla(x):                                 
    def karesini_al(a):                         
        return a**2                             
    def karekok_al(a):                          
        return a**0.5                           
    def faktoriyel(a):                          
        carpim=1                                
        for i in range(1,a+1):                  
            carpim*=i                          
        return carpim                           
    kare = karesini_al(x)                       
    karekok = karekok_al(x)                     
    fak = faktoriyel(x)                        
    return "karesi : {} , karekoku : {} , faktöriyeli: {}".format(kare,karekok,fak) 

print(hesapla(9))           # / karesi : 81 , karekoku : 3.0 , faktöriyeli: 362880  # print yazmamızın sebebi fonksyionun son hareketinde print ifadesi olmadığındandır.


# önemli not: iç içe tanımlanan fonksiyonlarda içeride tanımlı olan fonksiyona erişim mümkün değildir.


def toplam_carpim(*args):
    def toplama(demet):
        return sum(demet)
    def carpim(demet):
        carpim = 1
        for i in demet:
            carpim *=i
        return carpim
    return "girilen sayıların toplamı: {} , girilen sayıların çarğımı : {}".format(toplama(args),carpim(args))

print(toplam_carpim(2,3,4,5,6,7,8))                     # girilen sayıların toplamı: 35 , girilen sayıların çarğımı : 40320

# önemli not: içerideki fonksiyonlara erişim olmadığından dolayı sonuçlarına da erişim mümkün değildir. o sebepten dolatı toplama(args) , carpim(args) ifadelerini kullandık.


#fonksiyonlardan fonksyion döndürme

def fonk(x):
    return x*x

a = fonk(4)                 # bunu dersek a değişkenine fonk(4) sonucunu atamış oluruz. yani sonuc 16

b = fonk                    # bunu dersek b değişkenine fonk fonksiyonunun kendisini atamış oluruz. bu sebepten dolayı herhangi bir sonucu yok.

print(b(5))                 # b ifadesini fonksiyona kısa isim vermiş gibi düşünebilriz.

def islem_sec(islem):                     
    def toplama(*args):                   
        return sum(args)                  
    def carpim(*args):                   
        carpim=1
        for i in args:
            carpim *=i
        return carpim                     
    def ortalama(*args):                  
        return sum(args) / len(args)     
    
    if islem == "toplama":                
        return toplama                   
    elif islem == "carpim":               
        return carpim                     
    elif islem=="ortalama":               
        return ortalama                   
    
top_fonk = islem_sec("toplama")           
print(top_fonk(3,4,5,6,7,10))             # 3,4,5,6,7,10 sayılarının toplamı : 35

carp_fonk = islem_sec("carpim")           
print(carp_fonk(2,3,4,5,6,7,8))           # 2,3,4,5,6,7,8 sayılarının çarpımı : 40320

ort_fonk = islem_sec("ortalama")          
print(ort_fonk(100,34,35,765))            # 100,34,35,765 sayılarının ortalaması : 233.5


def kisi_sec(kisi):                         
    def takim_sec(takim):                   
        return "{} {} takımını tutuyor.".format(kisi,takim) 
    return takim_sec                        # dışarıdaki fonksiyon çalışırsa ne yapacağını belirttik. takim_sec fonksiyonunun kendisini geri dönecek

a = kisi_sec("Ali")                         
b = kisi_sec("Hamza")                       

print(a("Fenerbahçe"))                      # Ali Fenerbahçe takımını tutuyor.
print(b("istanbulspor"))                    # Hamza istanbulspor takımını tutuyor.


