print("PROGRAM HITUNG GAJIH KARYAWAN")
Nama = input("masukan Nama :")
Jabatan = int(input("masukan Jabatan :"))
Pendidikan = input("masukan Pendidikan :")
JamKerja = int(input("masukan jam Kerja :"))
GajiPokok = 300000
TjnJabatan = 0
TjnPendidikan = 0
HonorLembur = 0
if Jabatan == 1:
    TjnJabatan = 0.05 * GajiPokok
elif Jabatan == 2:
    TjnJabatan = 0.10 * GajiPokok
elif Jabatan == 3:
    TjnJabatan = 0.15 * GajiPokok
else:
    print("Golongan Jabatan tidak ada")

if Pendidikan == "SMA":
    TjnPendidikan = 0.025 * GajiPokok
elif HonorLembur== "D1":
    TjnPendidikan = 0.5 * GajiPokok
elif HonorLembur== "D3":
    TjnPendidikan = 0.20 * GajiPokok
elif HonorLembur== "S1":
    TjnPendidikan = 0.30 * GajiPokok
    print("Pendidikan tidak ada")

if JamKerja > 8:
    HonorLembur = (JamKerja -8) * 3500
else:
    HonorLembur = 0

total = GajiPokok + TjnPendidikan + TjnJabatan +HonorLembur

print("==============================")
print("Karyawan yang bernama    :", Nama)
print("Honor yang di terima")
print(" Tunjangan Jabatan       :", TjnJabatan)
print(" Tunjangan Pendidikan    :", TjnPendidikan)
print(" Honor Lembur            :", HonorLembur)
print("                         -----------------+")
print("                         ", total )
print("==============================")
print("Total Gajih")
print(total)