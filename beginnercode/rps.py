#import libraries and initialize variables
import random
loop = True
cpuc= "N"
cpc = 0
urc = 0
cpuscore = 0
usrscore = 0
errorlock = 0
u = False
lcpuc = "N"
def clscreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#function for verifying user input
def verusrin(usr):
    if usr == "R" or usrin == "P" or usrin == "S":
            return 1
    else:
        print("input invalido, generando valor aleatorio")
        return 2
#main loop of the game
while loop:

    #ask the user for an input, R,P or S
    usrin = input("R)ock, P)aper or S)cissors?:\t\t")
    #verify if input is uppercase or lowercase
    if usrin.isupper():
        #if input is uppercase, verifies the input with the verusrin() funct. if it's not valid, generates a random value
        if verusrin(usrin) == 1:
            u = False
        elif verusrin(usrin)==2:
            u = False
            urc = random.randint(0,2)
            if urc == 0:
                usrin = "R"
            elif urc == 1:
                usrin = "P"
            elif urc == 2: 
                usrin = "S"   
            print(f"valor generado: {usrin}")
    #if input is lowercase, it converts it to uppercase and verify if input is valid with verusrin(). if not, generates a random value
    elif usrin.islower():
        print(usrin)
        usrin = usrin.upper()
        print(usrin)
        if verusrin(usrin) == 1:
            u = False
        elif verusrin(usrin) == 2:
            u = False
            print("")
            urc = random.randint(0,2)
            if urc == 0:
                usrin = "R"
            elif urc == 1:
                usrin = "P"
            elif urc == 2: 
                usrin = "S"   
            print("error")       
    #generate a value for the cpu choice. cpu choice *CAN NOT* be the same as the last game
    try:
        cpc = random.randint(0,2)
        if cpc != lcpuc:
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
        print("cpu win")
        cpuscore += 1
    elif usrin == "R" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("usr win")
        usrscore += 1
    if usrin == "P" and cpuc == "R":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("usr win")
        usrscore += 1
    elif usrin == "P" and cpuc == "P":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("Draw")
    elif usrin == "P" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("cpu win")
        cpuscore += 1
    if usrin == "S" and cpuc == "R":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("cpu win")
        cpuscore += 1
    elif usrin == "S" and cpuc == "P":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("usr win")
        usrscore += 1
    elif usrin == "S" and cpuc == "S":
        print(f"Rock Paper Scissors...!  user: {usrin}\tcpu: {cpuc}")
        print("draw")
    #else:
    #    print("error 3")
    #    loop = False
    #    errorlock = 1
    print(f"score: usr:{usrscore} - {cpuscore}: cpu")
    print("deseas seguir jugando? Y)es//N)o")
    a = input("\n\t")
    u = True
    if errorlock == 0:
        while u == True: 
            if a.isupper():
                u = False
            elif a.islower():
                a = a.upper()
            else:
                print("input invalido...")
                print("deseas seguir jugando? Y)es//N)o")
                a = input("\n\t")
            if a == "Y" or a == "y":
                u = False
                clscreen()
            elif a == "N" or a == "n": 
                print("Bye bye ;3")
                u = False
                loop = False
            else:
                print("input invalido")