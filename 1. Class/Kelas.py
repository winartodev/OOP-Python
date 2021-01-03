'''
Class adalah salah satu cara bagaimana kita membuat sebuah kode yang mempunyai behaviour tertentu dan lebih mudah dalam mengorganisasi berbagai fungsi dan state-nya.
'''
# Membuat Sebuah Class Kosong 
class ClassKosong:
    pass

# Membuat Sebuah Class Kendaraan yang memiliki attribut jurusan dan harga
class Kendaraan:
    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga