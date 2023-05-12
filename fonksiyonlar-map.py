# map fonksiyonu:

# yazdığımız kodun daha kısa ve kullanışlı olmasını sağlar.
# parametre olarak bir fonksiyon ve bir liste alır. liste elemanlarını teker teker fonksiyonda yerine koyar ve sonucu yeni bir liste olarak döndürür.

# map fonksiyonu kullanmadan liste içerisindeki rakamlarının karelerini alalım:

liste= [1,2,3,4,5]              
def f1 (x):                     
    return x*x                  

liste2=[]                       
for i in liste:                 
    liste2.append(f1(i))        
print(liste2)                   # / [1, 4, 9, 16, 25]


# map fonksyionu kullanarak yaparsak:

liste= [1,2,3,4,5] 
liste3= map(f1,liste)           
print(liste3)                   # / <map object at 0x000001F51CF1C250>

liste3= list(map(f1,liste))     
print(liste3)                   # / [1, 4, 9, 16, 25]

# lambda ile iç içe kullanım : 

liste4 = [9,8,7,6,5]
liste5=list(map(lambda x : x*x ,liste4))        
print(liste5)                   # / [81, 64, 49, 36, 25]

liste6=[6,6,6,6,6]
liste7=list(map(lambda x : x*x , liste6))
print(liste7)                   # / [36, 36, 36, 36, 36]


#listedeki bütün elemanlara aynı işlemi uygulamak istersek (listedeki bütün elemanların karesini al , kokunu al , vb) map fonksiyonu çok kullanışlı olabilir.

# örnek : birbirinden bağımsız iki listedeki elemanları index numaralarına göre birleştirip tek liste yapalım.

liste8 = [1,3,4,5,6]                        
liste9 = [9,6,5,4,5]                        

def toplam(x,y):                            
    return x+y                              

liste10= list(map(toplam , liste8,liste9))

print(liste10)                              # / [10, 9, 9, 9, 11]

# örnek - 2

liste11 = [1,3,4,5,6]                       
liste12 = [9,6,5,4,5]                       
liste13 = [7,6,5]                           

def toplam(x,y,z):                            
    return x+y+z                              

liste14= list(map(toplam , liste11,liste12,liste13))  

print(liste14)                              # / [17, 15, 14] en düşük eleman sayısı olan liste elemanı kadar eleman döndürür.

liste15 = list(map(lambda x,y,z : x+y+z,liste11,liste12,liste13))
print(liste15)                              # / [17, 15, 14] lambda yardımı ile bu şekilde de yazabiliriz.

# map fonksiyonu birden fazla liste alabilir.


