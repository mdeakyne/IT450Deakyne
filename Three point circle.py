__author__ = 'Administrator'
#http://www.regentsprep.org/regents/math/geometry/gcg6/RCir.htm
def checkio(data):
    data = data.replace("(","")
    data = data.replace(")","")
    coords = data.split(",")

    x1,y1 = float(coords[0]),float(coords[1])
    x2,y2 = int(coords[2]),int(coords[3])
    x3,y3 = int(coords[4]),int(coords[5])

    print(x1,y1,x2,y2,x3,y3)
    if(x2-x1 == 0):
        x2,x3,y2,y3 = x3,x2,y3,y2
        print("switched points 1")
    if(x3-x2 == 0):
        x2,x3,y2,y3 = x3,x2,y3,y2
        print("switched points 1")
    if(y2-y1 == 0):
        y1,y3,x1,x3 = y3,y1,x3,x1
        print("switched points 1")

    mr = float(y2-y1)/(x2-x1)
    mt = float(y3-y2)/(x3-x2)

    print (mr,mt)

    x0 = (mr*mt*(y3-y1) + mr*(x2+x3) - mt*(x1+x2))/(2*(mr-mt))
    y0 = -(1/mr) * (x0 - (x1+x2)/2)+(y1+y2)/2
    r = ((x2-x0)**2+(y2-y0)**2) ** .5

    print(x0, y0, r)

    x0 = str(round(x0,2))
    y0 = str(round(y0,2))
    r = str(round(r,2))

    if(x0[-1]=='0'):
        x0=x0[:-2]
    if(y0[-1]=='0'):
        y0=y0[:-2]
    if(r[-1]=='0'):
        r=r[:-2]

    #replace this for solution

    return "(x-%s)^2+(y-%s)^2=%s^2" % (x0,y0,r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    print checkio("(3,7),(6,9),(9,7)")
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"