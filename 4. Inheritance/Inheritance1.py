'''
Inheritance adalah konsep pewarisan class. Class juga dapat menuruni dan memiliki apa yang dimiliki oleh class lainnya.
'''
class Kendaraan():
    def __init__(self, nama):
        self.nama = nama

class Mobil(Kendaraan):
    __roda = 4

    def __init__(self, nama):
        super().__init__(nama)

    def merekMobil(self, merek):
        self.merek = merek
    
    def infoMobil(self):
        print('Mobil {} merek {} roda {}'.format(self.nama, self.merek, self.__roda))

class Motor(Kendaraan):
    __roda = 2

    def __init__(self, nama):
        super().__init__(nama)
    
    def merekMotor(self, merek):
        self.merek = merek
    
    def infoMotor(self):
        print('Motor {} merek {} roda {}'.format(self.nama, self.merek, self.__roda))
        

kendaraan1 = Mobil('Budi')
kendaraan1.merekMobil('Avanza')
kendaraan1.infoMobil()

kendaraan2 = Motor('Anton')
kendaraan2.merekMotor('Ninja')
kendaraan2.infoMotor()
