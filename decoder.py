#v8 u6 p9 m3 l1 r4 z2 s5 t7
#123456789abcdefghijk
csl = 1362963
def decode(csl):
    while csl != 0:
        z = (csl % 21)
        csl = (csl // 21)
        numero(z)



def numero(z):
    if z == 10:
        print("a")
    elif z == 11:
        print("b")
    elif z == 12:
        print("c")
    elif z == 13:
        print("d")
    elif z == 14:
        print("e")
    elif z == 15:
        print("f")
    elif z == 16:
        print("g")
    elif z == 17:
        print("h")
    elif z == 18:
        print("i")
    elif z == 19:
        print("j")
    elif z == 20:
        print("k")
    elif z == 9:
        print("p")
    elif z == 8:
        print("v")
    elif z == 7:
        print("t")
    elif z == 6:
        print("u")
    elif z == 5:
        print("s")
    elif z == 4:
        print("r")
    elif z == 3:
        print("m")
    elif z == 2:
        print("z")
    elif z == 1:
        print("l")
    else:
        print("o")

decode(csl)