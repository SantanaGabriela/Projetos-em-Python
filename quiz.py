Descricao = '''

Quiz Sobre Conhecimentos Gerais!!

Responda o quiz e veja sua pontuação no final. 

Cada resposta correta vale 10 pontos!


'''
print(Descricao)

def Quiz():
    iniciar = input("Deseja Começar? (S/N)")
    if iniciar =="S" or "s":
        print("Vamos começar!")
        iniciar_quiz()
    else:
        quit()

def iniciar_quiz():
    score = 0 
    print("Qual a capital de Pernambuco? \n")
    resposta= input(" (A)Caruaru \n (B)Recife \n (C)Olinda \n (D)Paulista \n Resposta:")

    if resposta == "B" or "b":
        print("Resposta Correta")
        score += 10
    else:
        print("Resposta Incorreta! :(")
    

    print("Onde fica localizada a ilha de Fernando de Noronha ? \n")
    resposta2 = input(" (A) Rio De Janeiro \n (B)Fortaleza \n (C)Pernambuco \n (D)Paraíba \n Resposta:")

    if resposta2 == "C" or "c":
        print("Resposta Correta")
        score += 10
    else:
        print("Resposta Incorreta! :(")
    
    print("Qual a cidade conhecida por: onde o sol nasce primeiro ? \n")
    resposta2 = input(" (A) Rio De Janeiro \n (B)Recife \n (C)Natal \n (D)João Pessoa \n Resposta:")

    if resposta2 == "D" or "d":
        print("Resposta Correta")
        score += 10
    else:
        print("Resposta Incorreta! :(")


    print(f' Parabéns Você concluiu o quiz com score de {score} pontos!')


Quiz()