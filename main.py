# class Notebook():
#     def __init__(self,xotira
#     def info(self):
#         info = f'Protssesori: {self.protssesori} Tezkor xotira: {self.rami} Xotirasi: {self.a_xotirasi}'
#         return info
# note = Notebook('intel','4gb', '1tr')


# print(note.info())
class Notebook():
    def __init__(self, protsessor, ram, xotira, tizim, videokarta, yadro, displey, klaviatura):
        self.protsessori = protsessor
        self.rami = ram
        self.xotirasi = xotira
        self.tizimi = tizim
        self.kartasi = videokarta
        self.yadrosi = yadro
        self.displeyi = displey
        self.klaviaturasi = klaviatura
    def get_protsessor(self):
        return self.protsessori
    def get_rami(self):
        return self.rami
    def get_xotirasi(self):
        return self.xotirasi
    def get_tizimi(self):
        return self.tizimi
    def get_yadrosi(self):
        return self.yadrosi
    def get_displeyi(self):
        return self.displeyi
    def get_klaviaturasi(self):
        return self.klaviaturasi
     


    def set_protsessor(self, new_protssesor):
        self.protsessori = new_protssesor
        return self.protsessori
    def set_rami(self, new_ram):
        self.rami = new_ram
        return self.protsessori
    def set_xotirasi(self, new_xotira):
        self.xotirasi = new_xotira
        return self.xotirasi
    def set_tizimi(self, new_tizim):
        self.tizimi = new_tizim
        return self.tizimi
    def set_yadrosi(self, new_yadro):
        self.yadrosi = new_yadro
        return self.yadrosi
    def set_displeyi(self,new_displey):
        self.displeyi = new_displey
        return self.displeyi
    def set_klaviaturasi(self, new_klaviatura):
        self.klaviaturasi = new_klaviatura
        return self.klaviaturasi


note = Notebook('Intel core i7 9300','8 GB', '256 GB', 'Windows 11 Pro','12 yadro','RGB color',)
print(note.set_protsessor("Intel core i3 10300"))