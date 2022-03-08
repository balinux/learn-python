from mimetypes import init

class Manusia:
    jumlah_tangan = 2

    def __init__(self, nama):
        self.nama = nama

    @classmethod
    def pengertian(cls):
        print(f'manusia bernama memiliki {cls.jumlah_tangan} tangan')

# class Manusia:
#   jumlah_tangan = 2 # class variable

#   def __init__(self, nama):
#     self.nama = nama # instance variable

#   @classmethod
#   def pengertian(cls):
#     print(f'Manusia memilki {cls.jumlah_tangan} tangan')


Manusia.pengertian()
seseorang  = Manusia("itadori")
seseorang.pengertian