valor: float
valorConvertido: float
opcao: int


print(f"BEM VINDO AO CONVERSOR, DIGITE AS OPÇÕES ABAIXO:")


print(f"Converter Real to Dolar (Digite 1)")
print(f"Converter Dolar to Real (Digite 2)")
print(f"Converter Real to Libra (Digite 3)")
print(f"Converter Libra to Real (Digite 4)")

opcao=int(input(f"Qual opção você deseja?:"))
valor=float(input(f"Digite o valor:"))

if opcao ==1:
    valorConvertido= valor/5.39
elif opcao==2:
    valorConvertido= valor* 5.39
if opcao==3:
    valorConvertido= valor/7.36
elif opcao==4:
    valorConvertido= valor*7.36


print(f"Valor Convertido:{valorConvertido:.2f}")











