num = 45198465
r = 16
def prevod(num):
    while num != 0:
        z = (num % r)
        num = (num // r)
        if (r == 16):
            binary(z)
        else:
            print(z)

def binary(z):
    if z == 15:
        print("f")
    elif z == 14:
        print("e")
    elif z == 13:
        print("d")
    elif z == 12:
        print("c")
    elif z == 11:
        print("b")
    elif z == 10:
        print("a")
    else:
        print(z)

        
    
prevod(num)