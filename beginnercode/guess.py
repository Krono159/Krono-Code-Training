#Adivina el número oculto
#
#Debemos de preguntar al usuario un número entre 1 y 50.
#
#Si añaden un número fuera de ese rango, vamos a indicar con un error que anime a elegir un número dentro del rango adecuado..
#
#Si no acertamos el número oculto, preguntaremos al usuario si queremos seguir jugando, introduciendo un nuevo número o queremos dejar de jugar.
#
#Finalmente, cuando el usuario acierta correctamente el número oculto, mostramos un mensaje de enhorabuena y mostramos el número de intentos que hemos utilizado para llegar a esta situación.
from random import randint as r
attempts = 0

loop = True
min = int(input("numero minimo...  "))
max = int(input("numero maximo...  "))
while loop:
    maxattempts = int(input("Maxima cantidad de intentos..."))
    if maxattempts>= max:
        print("la cantidad de intentos es mayor o igual al numero maximo. ingrese otro valor")
    else: 
        loop = False
num = r(min,max)
loop = True
while loop:
    try:
        usrguess = int(input("adivina el numero...\t"))

        if usrguess < min or usrguess > max:
            print(f"numero invalido, debe estar entre {min} y {max}")
            loop = True
        elif usrguess > min or usrguess < max: 
            loop = False
            attempts += 1
        else:
            loop = True
            print("error")
    except:
        print("error")
    if attempts <= maxattempts:
        loop = True

        if usrguess > num:
            print("muy alto")
        elif usrguess < num:
            print("muy bajo")
            print("intentos restantes... ")
        elif usrguess == num:
            print("numero correcto!")
            attempts = maxattempts+99
    elif attempts > maxattempts:
        print("el numero era... ", num)
        print("deseas jugar de nuevo?")
        ans = input("S)i // N)o\t\t")
        if ans.islower():
            ans = ans.upper()
        if ans == "Y":
            num = r(min,max)
            attempts = 0
            loop = True
        else:
            print("Hasta luego! ")
            attempts = 99
            loop = False
        


