def main():

    #definição de valores hipotéticos de contas normal/universitária
    conta_normal = saldo = 1000
    conta_universitaria = saldo1 = 1000
    cheque_especial = 200

    #escolha no terminal qual o tipo de conta
    opção = int(input("Informe uma opção:\n [1] Conta normal \n [2] Conta universitária\n "))

    saque = int(input("Qual o valor do saque? "))
    status = "Sucesso" if saldo >= saque else "Falha"
    status1 = "Uso do cheque especial! " if saldo + cheque_especial >= saque else "Saldo insuficiente! "
    x = print(f"{status} ao realizar o saque! ")
    y = print(f"{status1}")



    if opção == 1:
        if saque <= saldo + cheque_especial:
            y
        else:
            saldo >= saque
            x

    elif opção == 2:
        if saldo1 >= saque:
            x
        else:
            x
main()