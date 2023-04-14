print("Exercício 59 da lista 03 - Escreva um retângulo oco com O (REPETIÇÃO)\n\n")

inicia = True
while inicia == True:

    num = int(input("Digite o número: "))

    n1 = num-2

    cont = 1
    n2 = 1
    n3 = 1
    espaco = " "


    if num <= 1:
        print("O número deve ser MAIOR que 2!")

    else:
        
        while num >= n2:
            print("O", end="")
            n2 = n2+1
        n2 = 1
        print("")

        #----------------------------------------
        
        while n1 >= cont:
            print("O", espaco * (n1 - 2), "O")
            cont = cont+1


    #--------------------------------------------------
        while num >= n2:
                print("O", end="")
                n2 = n2+1

    soun = input("\n\nDeseja fazer outro Retângulo oco? s/n ")
    if soun.lower() == "s":
         inicia = True
    else:
         inicia = False