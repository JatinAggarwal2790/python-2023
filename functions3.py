# variable length args
def total(*args):
    print(sum(args))

total(3,4)
total(3)
total()
total(3,4,4)
total(3,4,6,7,8,9,6,0,4,3,2,1)

# variable length keyword args

def polygon(**sides):
    print(sides)

polygon(side1=30,side2=45,side3=55,side4=98)
polygon(side1=30,side2=45,side3=55)
polygon(side1=30,side2=45)
polygon(side1=30)


