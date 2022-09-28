class Karyawan:
    _nama = "" 
    _umur = 0
    _JenisKelamin= None
    _upahPerHari = None

    def __init__(self,nama,umur):
        self._nama = nama
        self._umur = umur

    def setNama(self,nama):
        self._nama = nama
    def setUmur(self,umur):
        self._umur = umur
    def setJenisKelamin(self,JenisKelamin):
        self._JenisKelamin = JenisKelamin 
    def setupahPerHari(self,upahPerHari):
        self._upahPerHari = upahPerHari
    
    def getNama(self):
        return self._nama
    def getUmur(self):
        return self._umur 
    def getJenisKelamin(self):
        return self._JenisKelamin
    def getupahPerHari(self):
        return self._upahPerHari


    def printInfo(self):
        print("="*12, "INFO","="*12)
        print("Nama :", self._nama)
        print("Umur :",self._umur)
        print("Jenis Kelamin    :",self._JenisKelamin)
        print("Upah per Hari    :",self._upahPerHari)


    def hitungGajiBulanan(self,hariPerBulan):
        if self._upahPerHari == None:
            print("ERROR! Upah per Hari belum di inputkan")
        else:
            print("Gaji Bulan ini :",self._upahPerHari * hariPerBulan)



#input
orang1 = Karyawan("Haniif", 90)
orang1.printInfo()

orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setupahPerHari(30000)
orang2.printInfo()
orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)
    

