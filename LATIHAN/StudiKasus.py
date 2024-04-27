Customer=input("Nama Customer : ")
NoHp=input("Nomor Handphone : ")
Jurusan=input("Jurusan Yang Dipilih : ")
JumlahBeli=int(input("Jumlah Beli : "))
if Jurusan=="SBY" :
    NamaJurusan="SURABAYA"
    Harga=300000
elif Jurusan=="BL" :
    NamaJurusan="BALI"
    Harga=350000
else :
    NamaJurusan="LAMPUNG"
    Harga=500000

if JumlahBeli>=3 :
    Potongan=(JumlahBeli*Harga)*0.1
else :
    Potongan=0

Total=(JumlahBeli*Harga)-Potongan

print("***********************************************")
print("             PENJUALAN TIKET BUS")
print("                     XYZ")
print("***********************************************")
print("Nama Pembeli     : "+str(Customer))
print("Nomor Handphone  : "+str(NoHp))
print("Kode Jurusan     : "+str(Jurusan))
print("Nama Kota Tujuan : "+str(NamaJurusan))
print("Harga            :",+(Harga))
print("Jumlah Beli      :",+(JumlahBeli))
print("***********************************************")
print("Potongan         :",+(Potongan))
print("Total Bayar      :",+(Total))
Bayar=int(input("Bayar            : "))
Kembali=Bayar-Total
print("Kembali          :",+(Kembali))