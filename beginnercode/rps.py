import random
loop = True
cpuc= "N"
cpc = 0
cpuscore = 0
usrscore = 0
u = False
def verusrin(usr):
    if usr == "R" or usrin == "P" or usrin == "S":
            return False
    else:
        print("input invalido")
def cpuwin():
    print("cpu win")
    return False
def usrwin():
    print("usr win")
    return True
while loop:
    u = True
    while u == True:
        usrin = input("R)ock, P)aper or S)cissors?:\t\t")
        if usrin.isupper():
            try:
                u = verusrin(usrin)
            except:
                print("error")
        elif usrin.islower():
            usrin = usrin.upper()
            try:
                u = verusrin(usrin)
            except:
                print("error")
            pass
        else:
            print("input invalido")
        

    try:
        cpc = random.randint(0,2)
        if cpc == 0:
            cpuc = "R"
        elif cpc == 1:
            cpuc = "P"
        elif cpc == 2: 
            cpuc = "S"            
    except:
        loop = False
        print("Error generando eleccion del programa...")
    if usrin == "R" and cpuc == "R":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("draw")
    elif usrin == "R" and cpuc == "P":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        if cpuwin():
            cpuscore += 1
    elif usrin == "R" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        if usrwin() == False:
            print(usrscore)
            usrscore += 1
            print(usrscore)
    if usrin == "P" and cpuc == "R":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        if usrwin() == False:
            usrscore += 1
    elif usrin == "P" and cpuc == "P":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("Draw")
    elif usrin == "P" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        cpuwin()
        cpuscore += 1
    if usrin == "S" and cpuc == "R":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        cpuwin()
        cpuscore += 1
    elif usrin == "S" and cpuc == "P":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        if usrwin() == False:
            usrscore += 1
    elif usrin == "S" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("draw")
    print(f"score: usr:{usrscore} - {cpuscore}: cpu")
    print("deseas seguir jugando? Y)es//N)o")
    a = input("\n\t")
    u = True
    while u == True: 
        if a.isupper():
            u = False
            pass
        elif a.islower():
            a = a.upper()
        else:
            print("input invalido...")
            print("deseas seguir jugando? Y)es//N)o")
            a = input("\n\t")
    if a == "Y":
        pass
    else: 
        loop = False