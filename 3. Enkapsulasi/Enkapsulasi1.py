'''
Enkapsulasi (encapsulation) adalah sebuah metoda untuk mengatur component class dengan cara menyembunyikan alur kerja dari class tersebut. Component class yang dimaksud adalah property dan method. Dengan enkapsulasi, kita bisa membuat pembatasan akses kepada property dan method, sehingga hanya property dan method tertentu saja yang bisa diakses dari luar class. Enkapsulasi juga dikenal dengan istilah 'information hiding'.
'''
#Pada konsep enkapsulasi semua property dalam bentuk private. Untuk mengakses dan merubah property diperlukan method getter dan setter.

class Umur:
    def __init__(self, nama):
        self.nama = nama
    
    def setUmur(self, num):
        self.__umur = num

    def getUmur(self):
        return self.__umur
    
budi = Umur('Budi')
budi.setUmur(12)

print(budi.getUmur()) # Output : 12