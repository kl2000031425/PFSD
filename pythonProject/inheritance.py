from circle import one
from square import two

class main(one,two):
    def a(self):
        print('area of given values')
#super.area(7)

obj=main()
obj.a()
obj.area(5)
obj.peri(5)
obj.sq(3)