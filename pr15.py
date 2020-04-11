import math
def hello(name) : 
    print (name,'안녕하세요')


class myClass():
    name = str()
    def __init__(self):
        self.name='아직 이름이 없습니다'
    def setname(self,nam):
        self.name=nam
    def showmyname(self) :
        print(self.name)

cl = myClass()
cl.showmyname()
cl.setname('kmj')
cl.showmyname()

print(math.pi)
