# try, tente mudar a senha para um número inteiro, se não consegue print a mensagem

def recebe_pin():
    senha = input("Digite seu PIN: ")
    try:
        senha = int(senha)
    except:
        print("Senha Inválida")
        senha = input("Digite seu PIN: ")

    print(senha)

recebe_pin()