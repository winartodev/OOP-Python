# Membuat Parent Class produk 
class Produk():
    def __init__(self, merek):
        self.merek = merek
    
    def hargaProduk(self, harga):
        self.harga = harga

# Membuat class jass dengan menurunkan sifat dari parent class produk
class Jas(Produk):
    __kategori = 'Jass'

    def __init__(self, merek):
        super().__init__(merek)

    def infoJass(self):
        print('\n{} dengan merek {} di jual dengan harga {}'.format(self.__kategori, self.merek, self.harga))

    def Additem(self):
        item = self.merek
        harga_item = self.harga
        return item, harga_item

class Buku(Produk):
    __kategori = 'Buku'

    def __init__(self, merek):
        super().__init__(merek)

    def infoBuku(self):
        print('\n{} dengan merek {} di jual dengan harga {}'.format(self.__kategori, self.merek, self.harga))

    def Additem(self):
        item = self.merek
        harga_item = self.harga
        return item, harga_item

class Keranjang():
    __keranjang = dict()
    __jumlahItem = 1 
    __jumlah = 0

    def __init__(self, nama):
        self.nama = nama

    def tambahKeranjang(self, item=list()):
        print('\nTambah Item')
        self.__jumlah = len(item)
        
        if self.__jumlah == 1:
            self.__keranjang['item{}'.format(self.__jumlahItem)] = {'Merek':item[0][0], 'Harga':item[0][1]}
        else:
            for i in range(0,self.__jumlah):
                self.__jumlahItem += i
                self.__keranjang['item{}'.format(self.__jumlahItem)] =  {'Merek':item[i][0], 'Harga':item[i][1]}
            
    def lihatKeranjang(self):
        print('\nKeranjang {} memiliki {}'.format(self.nama, self.__keranjang))
        pass

    def hapusItem(self, key):
        print('\nMenghapus {} : {}'.format(key, self.__keranjang[key]))
        self.__keranjang.pop(key)

    def ubahItem(self, data):
        self.__keranjang.update(data)
        pass


produk_jas = Jas('Cardinal')
produk_jas.hargaProduk(10000)

produk_buku = Buku('Python OOP Book')
produk_buku.hargaProduk(15000)

budi = Keranjang('Budi')
budi.tambahKeranjang([produk_jas.Additem(), produk_buku.Additem()])
budi.lihatKeranjang()

budi.hapusItem('item1')
budi.lihatKeranjang()

budi.ubahItem({'item2':produk_jas.Additem()})
budi.lihatKeranjang()


