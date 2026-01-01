menu ={
    "freid chiken"  :10000,
    "kentang goreng":12000,
    "ayam geprek"   :10000,
    "nasi goreng"   :20000,
    "lemon tea"     :5000,
}
print("================Daftar Menu===========================")
for i in menu:
    print("Daftar menu: ",i,  "\t  harga: ",menu[i])

print("pembelian di atas 50.000 mendapatkan Diskon 5%")
print("======================================================")  
beli= input("piih menu: ")
jumlah= int(input("jumlah pesanan:"))
bayar= jumlah*menu[beli]

if bayar> 50.000:
        diskon = bayar*5/50.000
        total=bayar-diskon
else:
        total=bayar
    
print ("===============Detail Pembayaran=====================")
print("menu yang di pesan       :",beli)
print("jumlah yang di pesan     : ",jumlah)  
print("total biaya              : ",bayar)
print("total yang harus di bayar:",total)