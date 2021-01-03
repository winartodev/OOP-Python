'''
Object atau instance adalah dasar dari modularitas dan structur pada OOP. dan merupakan representasi dari class, object akan memiliki sifat dan perilaku dari class yang digunakan.
'''
# Membuat kelas kendaraan yang memiliki costructor merek dan harga
class Kendaraan:
    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga
    
# Membuat objek mobil1 yang memanggil kelas kendaraan
mobil1 = Kendaraan('Avanza', 200000000)

# Menampilkan attribut yang dimiliki oleh objek mobil1 menggunakan dot atau .
print("Merek Mobil : {}".format(mobil1.merek))
print("Harga Mobil : {}".format(mobil1.harga))

