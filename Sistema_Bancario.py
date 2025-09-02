menu = """
  ====== Menu Bancário ======

Bem vindo ao sistema bancário
 Selecione a opção desejada

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
"""

LIMITE_SAQUE = 500
valor_deposito = 0
valor_saque = 0
saldo_conta = 0
depositos = []
saques = []
opcao = 0


while opcao != 4:
  print(menu)
  try:
    opcao = int(input("Qual a opção desejada? : "))

    if opcao == 1:
      try:
        valor_deposito = float(input("Digite o valor do deposito: "))
        if valor_deposito < 0:
            print("Valor de depósito inválido! O valor do depósito precisa ser positivo")
        else:
            depositos.append(valor_deposito)
            saldo_conta += valor_deposito
      except ValueError: print("Vocâ não digitou apenas números, sendo assim, não foi possível realizar o depósito.")

    elif opcao == 2:
      try:
        valor_saque = float(input("Digite o valor o qual deseja sacar: "))
        if valor_saque > LIMITE_SAQUE:
          print("O valor solicitado ultrapassa o limite permitido por transação")
        elif valor_saque > saldo_conta:
          print("Você não possui saldo suficiente para realizar o saque")
        elif valor_saque < 0:
          print("O valor de saque não pode ser negativo")
        else:
          saques.append(valor_saque)
          saldo_conta -= valor_saque
      except ValueError:print("Você não digitou apenas números, sendo assim, não foi possível realizar o saque.")

    elif opcao== 3:
      print("""
              ======= Extrato Bancário =======
                *** Seus depósitos foram ***
            """)

      for deposito in depositos:
        print(f"R$ {deposito:.2f}", end="\n")
        

      print("""
                *** Seus saques foram ***
            """)
      for saque in saques:
        print(f"R$ {saque:.2f}", end="\n")
    
      print(f"Saldo da Conta = {saldo_conta:.2f}", end="\n")
      
    elif opcao == 4:
      print("Obrigado por utilizar nosso sistema, até a próxima!")

    else:
      print("Opção inválida, por favor escolha uma opção da lista.")

  except ValueError:print(f"Você digitou um tipo de caractere não aceito, por favor digite um valor do tipo INTEIRO")