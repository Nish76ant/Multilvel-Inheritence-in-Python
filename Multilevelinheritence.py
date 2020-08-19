class Dad:
    basketball = 1

class son(Dad):
    dance = 6
    basketball = 9

    def isDance(self):
        return f'yes i dance {self.dance} no of times'

class Grandson(son):
    dance = 9
    guitar = 5

    def isDance(self):
        return f' Jackson yeah i dance very osmly {self.dance} no of time'




darry = Dad()
larry = son()
harry = Grandson()

print(harry.isDance())
print(harry.basketball)
print(harry.guitar)

#Excercise
"""
class 1 = Electronic device
class 2 = pocket_gadget
class 3 = phone
"""

