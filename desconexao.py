warn = input("Você está aí? (s/n):   ")
question = ""

if warn == "s":
    question = input("Você vai continuar jogando? (s/n):     ")
    tempo = int(input("Quanto tempo você jogou hoje? {digite em minutos.}    "))

else:
    print("Você será desconectado em breve.")

if question == "n": 
    print("Você será deslogado em 10 segundos.")

elif question == "s" and tempo < 120:
    print("Obrigado e bom jogo!")

elif question == "s" and tempo >= 120:
    print("Você está jogando por bastante tempo, melhor dar uma pausa.")