###########Exercicio 2#################3

#1

numero1 = int(input("insere um numero: "))

numero2 = int(input("insere outro numero: "))


if numero1 > numero2:
    print(numero1)
elif numero2 > numero1:
    print(numero2)
else:
    print(numero1 or numero2)

#2

num6 = int(input("insere um numero para se saber se é positivo ou negativo: "))

if num6 < 0:
    print("o número é negativo")
else:
    print("o número é positivo")

#3

letra = input("\tInsira uma letra:")
if letra == "F" or letra == "f" or letra == "M" or letra == "m":
    if letra == "F" or letra == "f":
        print("\tFeminino")
    if letra == "M" or letra == "m":
        print("\tMasculino")
else:
    print("\tGenero Inválido")

#4

letra = input("Digite uma letra: ")
if letra in 'aeiou':
    print("Vogal")
else:
    print("Consoante")

#5

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    if media == 10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")

#6

for num in range(101):
    print(num)

#7

for num_decrescente in range(100, -1, -1):
    print(num_decrescente)

#8

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print("Compre o primeiro produto")
elif preco2 < preco1 and preco2 < preco3:
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")

#9

turno = input("Digite o turno que você estuda (M-matutino, V-vespertino, N-noturno): ")
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

#10

salario_atual = float(input("Digite o salário atual: "))

if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + aumento

print(f"Salário atual: R$ {salario_atual}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento}")
print(f"Novo salário: R$ {novo_salario}")

#11

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    menor_numero = segundo_numero
    maior_numero = primeiro_numero
else:
    menor_numero = primeiro_numero
    maior_numero = segundo_numero

for numero_intervalo in range(menor_numero + 1, maior_numero):
    print(numero_intervalo)

#12

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto}")
print(f"(-) IR ({(ir/salario_bruto)*100:.0f}%) : R$ {ir}")
print(f"(-) INSS (10%) : R$ {inss}")
print(f"FGTS (11%) : R$ {fgts}")
print(f"Total de descontos : R$ {total_descontos}")
print(f"Salário Líquido : R$ {salario_liquido}")

#13

dia = int(input("Digite um número (1-7) para o dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido")

#14

nota1_aluno = float(input("Digite a primeira nota: "))
nota2_aluno = float(input("Digite a segunda nota: "))
media_aluno = (nota1_aluno + nota2_aluno) / 2

if media_aluno >= 9:
    conceito = 'A'
elif media_aluno >= 8:
    conceito = 'B'
elif media_aluno >= 7:
    conceito = 'C'
elif media_aluno >= 6:
    conceito = 'D'
else:
    conceito = 'E'

print(f"Média: {media_aluno}")
print(f"Conceito: {conceito}")

if conceito in ['A', 'B', 'C']:
    print("Aprovado")
else:
    print("Reprovado")

#15

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")

# 16
a_eq = float(input("Digite o valor de a: "))
if a_eq == 0:
    print("A equação não é do segundo grau.")
else:
    b_eq = float(input("Digite o valor de b: "))
    c_eq = float(input("Digite o valor de c: "))
    delta_eq = b_eq**2 - 4*a_eq*c_eq
    
    if delta_eq < 0:
        print("A equação não possui raízes reais.")
    elif delta_eq == 0:
        raiz_unica = -b_eq / (2 * a_eq)
        print(f"A equação possui uma raiz real: {raiz_unica}")
    else:
        raiz1_eq = (-b_eq + delta_eq**0.5) / (2 * a_eq)
        raiz2_eq = (-b_eq - delta_eq**0.5) / (2 * a_eq)
        print(f"A equação possui duas raízes reais: {raiz1_eq} e {raiz2_eq}")

# 17
ano_informado = int(input("Digite um ano: "))
if (ano_informado % 4 == 0 and ano_informado % 100 != 0) or (ano_informado % 400 == 0):
    print(f"{ano_informado} é um ano bissexto.")
else:
    print(f"{ano_informado} não é um ano bissexto.")

# 18
dia_informado, mes_informado, ano_informado_data = map(int, input("Digite uma data (dd/mm/aaaa): ").split("/"))

valida_data = True
if mes_informado < 1 or mes_informado > 12:
    valida_data = False
elif dia_informado < 1 or dia_informado > 31:
    valida_data = False
elif mes_informado == 2:
    if (ano_informado_data % 4 == 0 and ano_informado_data % 100 != 0) or (ano_informado_data % 400 == 0):
        if dia_informado > 29:
            valida_data = False
    else:
        if dia_informado > 28:
            valida_data = False
elif mes_informado in [4, 6, 9, 11] and dia_informado > 30:
    valida_data = False

if valida_data:
    print("Data válida")
else:
    print("Data inválida")

# 19
numero_informado = int(input("Digite um número menor que 1000: "))

centenas = numero_informado // 100
dezenas = (numero_informado % 100) // 10
unidades = numero_informado % 10

if centenas > 0:
    print(f"{centenas} {'centena' if centenas == 1 else 'centenas'}, ", end="")
if dezenas > 0:
    print(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}, ", end="")
if unidades > 0:
    print(f"e {unidades} {'unidade' if unidades == 1 else 'unidades'}")

# 20
nota1_aluno = float(input("Digite a primeira nota: "))
nota2_aluno = float(input("Digite a segunda nota: "))
nota3_aluno = float(input("Digite a terceira nota: "))

media_notas = (nota1_aluno + nota2_aluno + nota3_aluno) / 3

if media_notas == 10:
    print(f"Aprovado com Distinção com média {media_notas}")
elif media_notas >= 7:
    print(f"Aprovado com média {media_notas}")
else:
    print(f"Reprovado com média {media_notas}")

# 21
valor_saque = int(input("Digite o valor do saque (mínimo 10 e máximo 600): "))
if 10 <= valor_saque <= 600:
    notas_100 = valor_saque // 100
    valor_saque %= 100
    notas_50 = valor_saque // 50
    valor_saque %= 50
    notas_10 = valor_saque // 10
    valor_saque %= 10
    notas_5 = valor_saque // 5
    notas_1 = valor_saque % 5
    
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 1: {notas_1}")
else:
    print("Valor inválido.")

# 22
numero_par_impar = int(input("Digite um número inteiro: "))
if numero_par_impar % 2 == 0:
    print(f"{numero_par_impar} é par.")
else:
    print(f"{numero_par_impar} é ímpar.")

# 23
numero_inteiro_decimal = float(input("Digite um número: "))
if numero_inteiro_decimal == int(numero_inteiro_decimal):
    print(f"{numero_inteiro_decimal} é um número inteiro.")
else:
    print(f"{numero_inteiro_decimal} é um número decimal.")

# 24
num1_operacao = float(input("Digite o primeiro número: "))
num2_operacao = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado_operacao = num1_operacao + num2_operacao
elif operacao == "-":
    resultado_operacao = num1_operacao - num2_operacao
elif operacao == "*":
    resultado_operacao = num1_operacao * num2_operacao
elif operacao == "/":
    if num2_operacao != 0:
        resultado_operacao = num1_operacao / num2_operacao
    else:
        print("Divisão por zero.")
        exit()

print(f"Resultado: {resultado_operacao}")

# Verificação
if resultado_operacao % 2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é ímpar.")

if resultado_operacao >= 0:
    print("O resultado é positivo.")
else:
    print("O resultado é negativo.")

if resultado_operacao == int(resultado_operacao):
    print("O resultado é inteiro.")
else:
    print("O resultado é decimal.")

# 25
respostas_crime = 0

if input("Telefonou para a vítima? (s/n): ").lower() == "s":
    respostas_crime += 1
if input("Esteve no local do crime? (s/n): ").lower() == "s":
    respostas_crime += 1
if input("Mora perto da vítima? (s/n): ").lower() == "s":
    respostas_crime += 1
if input("Devia para a vítima? (s/n): ").lower() == "s":
    respostas_crime += 1
if input("Já trabalhou com a vítima? (s/n): ").lower() == "s":
    respostas_crime += 1

if respostas_crime == 2:
    print("Suspeito.")
elif 3 <= respostas_crime <= 4:
    print("Cúmplice.")
elif respostas_crime == 5:
    print("Assassino.")
else:
    print("Inocente.")

# 26
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()
litros_vendidos = float(input("Digite a quantidade de litros: "))

preco_alcool = 1.90
preco_gasolina = 2.50

if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_final = litros_vendidos * preco_alcool * (1 - desconto)
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_final = litros_vendidos * preco_gasolina * (1 - desconto)

print(f"Valor a pagar: R$ {preco_final:.2f}")
