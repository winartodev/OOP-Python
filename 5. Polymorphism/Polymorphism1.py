'''
Polymorphism berasal dari bahasa yunani yang berarti memiliki banyak bentuk, adalah kemampuan dalam menyampaikan pesan tertentu keluar dari hirarki objectnya, dimana object yang berbeda memberikan tanggapan atau respon terhadap pesan yang sama sesuai dengan sifat masing-masing object.
'''
class Kucing():
    def __init__(self, jenis, suara):
        self.jenis = jenis
        self.suara = suara

    def get_suara(self):
        print('Kucing {} suara {}'.format(self.jenis, self.suara))
    
class Anjing():
    def __init__(self, jenis, suara):
        self.jenis = jenis
        self.suara = suara
    
    def get_suara(self):
        print('Anjing {} suara {}'.format(self.jenis, self.suara))

hewan1 = Kucing('Persia','Meong')
hewan2 = Anjing('Siberia','Guk Guk')

# hewan1.get_suara()
# hewan2.get_suara()

for binatang in [hewan1, hewan2]:
    binatang.get_suara()