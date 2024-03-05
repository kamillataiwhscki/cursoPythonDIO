MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH")
elif idade == 17:
    print("Pode fazer aulas teóricas, mas não pode fazer as práticas")
else:
    print("Não pode tirar a CHN")

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 500
chque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saldo <= (saque + chque_especial):
        print("Saque realizado utilizando o cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

# if ternário
        
status = "Sucesso" if saldo >= saque else "False"
print(f"{status} ao realizar o saque")

texto = "DKADKJANDKJANIYFUI9PIUHEUIUFUIAFKJASBF"
VOGAIS = "AEIOU"

for letra in VOGAIS:
    if letra.upper() in texto:
        print(letra, end=" ")
    else: 
        print("que")


for numero in range(0, 11):
    print(numero, end=" ")
for numero in range(0, 51, 5):
    print(numero, end=" ")

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2]Extrato\n[0]Sair"))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo extrato")
    elif opcao == 0:
        break
    else:
        print("Escolha uma opção válida!")

for numero in range(100): 
    if numero % 2 == 0: #imprimindo apenas numeros impares
        continue
    print(numero, end=" ")