class Hobi:
    __hobi = []

    def tambahHobi(self,hobi):
        Hobi.__hobi.append(hobi)

    def lihatHobi(self):
        return Hobi.__hobi

    def hapusHobi(self, hapus):
        Hobi.__hobi.pop(hapus)

Budi = Hobi()
Budi.tambahHobi('Main Bola')
Budi.tambahHobi('Main Layangan')
Budi.tambahHobi('Main Sepeda')
print('Hobi 1 budi adalah {}'.format(Budi.lihatHobi()))
Budi.hapusHobi(1)
print('Hobi 2 budi adalah {}'.format(Budi.lihatHobi()))