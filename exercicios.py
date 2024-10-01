print("ola mundo")

asd= int(input("inser que execicio queres fazer: "))


nome2 = int(input ("escreve um número:"))
print(f"o numero inserido foi, {nome2}")
#3
numero1 = int(input("insere o um numero:")) 
numero2 = int(input("insere o um numero:"))

soma = numero1 + numero2

print(f"a soma dos numeros é :{soma}")

#4

numero1 = float(input("insere a primeira nota"))
numero2 = float(input("insere a segunda nota"))
numero3 = float(input("insere a terceira nota"))
numero4 = float(input("insere a quarta nota"))

media = numero1 + numero2 + numero3 + numero4 / 4


print(f"a media é {media}")

#5

metros = float(input("insere a tua medida em metros: "))

centimetros = metros*100

#6

print(f"a tua medida em centimetros é: {centimetros}")

raio = float(input("insere o raio do teu circulo: "))

raioquadrado = raio*raio

area = 3.14 * raioquadrado

print(f"a area do teu circulo é: {area}")

#7



lados = float(input("insere a medida dos lados do quadrado: "))

resultado = (lados * lados)/2

print(f"a area do teu quadrado é: {resultado}")

#8

valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario = valor_hora * horas_trabalhadas
print(f"Seu salário no mês é: R$ {salario:.2f}")

#9

F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5 * ((F - 32) / 9)
print(f"A temperatura em Celsius é: {C:.2f}")

#10

C = float(input("Digite a temperatura em Celsius: "))
F = (C * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {F:.2f}")

#11

num_inteiro1 = int(input("Digite o primeiro número inteiro: "))
num_inteiro2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))
produto = (2 * num_inteiro1) * (num_inteiro2 / 2)
soma = (3 * num_inteiro1) + num_real
cubo = num_real ** 3
print(f"Produto do dobro do primeiro com metade do segundo: {produto}")
print(f"Soma do triplo do primeiro com o terceiro: {soma}")
print(f"Terceiro número elevado ao cubo: {cubo}")

#12

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").upper()
if sexo == 'M': 
    peso_ideal_homem = (72.7 * altura) - 58 
    print(f"Seu peso ideal é: {peso_ideal_homem:.2f} kg") 
elif sexo == 'F': 
    peso_ideal_mulher = (62.1 * altura) - 44.7 
    print(f"Seu peso ideal é: {peso_ideal_mulher:.2f} kg") 
else: 
    print("Sexo inválido. Tente novamente.")

#13

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").upper()
if sexo == 'M': 
    peso_ideal_homem = (72.7 * altura) - 58 
    print(f"Seu peso ideal é: {peso_ideal_homem:.2f} kg") 
elif sexo == 'F': 
    peso_ideal_mulher = (62.1 * altura) - 44.7 
    print(f"Seu peso ideal é: {peso_ideal_mulher:.2f} kg") 
else: 
    print("Sexo inválido. Tente novamente.")

#14

peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
limite = 50
excesso = 0
multa = 0
if peso_peixes > limite: 
    excesso = peso_peixes - limite 
    multa = excesso * 4
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a ser paga: R$ {multa:.2f}")

#15

peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
limite = 50
excesso = 0
multa = 0
if peso_peixes > limite: 
    excesso = peso_peixes - limite 
    multa = excesso * 4
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a ser paga: R$ {multa:.2f}")
