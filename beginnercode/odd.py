#requires info for 
testo = input("ingrese numero...: \t\t\t")
def odd(i):
    if i%2==0:
        return True
try:
    test = testo
    try:
        if test>=0 or test <= 10000:
            validnum = test
    except:
        print("num is greater than 10000")
    try:
        if odd(validnum) == True:
            print("Numero entero")
        else:
            print("numero impar")
    except:
        print("error... intente de nuevo")
except:
    print("value is not a number")
