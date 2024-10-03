import array
# caderno francisco baracinha

# ---------------- AULA 1 ---------------- 01 / 10 / 2024
print("Ola Mundo")

#var

nome = "Valor" #String
idade = 10 # max int em c -> 2,147,483,647, max int cm Py -> não existe
nota = 10.9 # Flaot( 6 a 7) e Double (14)
aprovado = True #

print(nome)
nome = 10
print(nome)

soma = idade + 3
print(soma)

soma2 = nota + 2
print(soma2)

nome = "Valor"
soma3 = nome + " Foo"
print(soma3)

nome = "Valor"
#soma4 = nome + 2024
#print(soma4)

op5 = nome * 2
print(op5)

#print v2


print("--" * 10)

nome = "Ricardo"
ano = 2024

#"Ola Mundo, Ricardo em 2024"

print("Ola Mundo, " + nome + " em " + str (ano))

print("Ola Mundo,", nome , "em", str(ano))

print(f"Ola Mundo, {nome.upper()} em {ano}")

print("--" * 10)

""""
-> % <-
"""
op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)

op2 = 10 / 3
print(op2)

op2 = 10 // 3
print(op2)

print("--" * 10)

#ler dados do teclado

nome2 = input("Ditie seu nome: ")
print(f"ola, {nome2}")

print("--" * 10)

#Ifs
idade = 10
print(f"Idade: {idade}")

if (idade > 18):
    print("\tDentro do if")
    print("\tAdulto")

print("Fora do if")

print("--" * 10)

# ---------------- AULA 2 ---------------- 03 / 10 / 2024

#Condições / Controlo de fluxo

#boolean (True | False)
'''
E (os dois têm de ser verdadeiros)
T e T -> T
T e F -> F
F e T -> T
F e F -> F

OU (qualquer um pode ser verdadeiro)
T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F

XOU (apenas um pode ser verdadeiro)
T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F
'''

ano = 2024

#------- if's (se) -------:

if ano == 2024:
    print("\tDentro do if")
    print("\tano = 2024")
else:
    print("\tDentro do else")
    print("\tOutro ano")
print("Fora do if")


print("--" * 10)

#Faça um programa que peça dois númros e imprima o maior deles

nmr1 = float(input("\tDigite um numero: "))
nmr2 = float(input("\tdigite outro numero: "))

if nmr1 > nmr2:
    print(f"\t{nmr1}")
else:
    print(f"\t{nmr2}")


print("--" * 10)

num = 5
print(f"\tNúmero: {num}")

if num % 2 == 0 and num % 5 == 0:
    print("\tResultado: Par e div por 5")
else:
    print("\tResultado: Impar ou nao div por 5")


'''
== <- Comaprações
= <- Atribuição
'''

print("--" * 10)

# faça um programa que verifique se uma letra digitada é "F" ou "f" ou "M" ou "m"

letra = input("\tInsira uma letra:")
if letra == "F" or letra == "f" or letra == "M" or letra == "m":
    if letra == "F" or letra == "f":
        print("\tFeminino")
    if letra == "M" or letra == "m":
        print("\tMasculino")
else:
    print("\tGenero Inválido")

print("--" * 10)

# switch ( escolha )
num =5
print(f"Numero: {num}")
match num:
    case 0:
        print(f"\tCase 0")
        print("\tO num e 0")
    
    case 1:
        print(f"\tCase 1")
        print("\tO num e 1")
    
    case 5:
        print(f"\tCase 5")
        print("\tO num e 5")
        
    case _:
        print(f"\tCase _")
        print("\toutro valor")


print("--" * 10)

menu = """
############ Menu ############
# OP1 ............ 1 #
# OP2 ............ 2 #
# OP3 ............ 3 #

 ########################"""
print(menu)

op = input("\tSelecione a op:")

match op:
    case "1":
        print(f"\tCase 1")
        print("\tO num e 1")
    
    case "2":
        print(f"\tCase 2")
        print("\tO num e 2")
    
    case "3":
        print(f"\tCase 3")
        print("\tO num e 3")
        
    case _:
        print(f"\tCase _")
        print("\tOutro valor")


print("--" * 10)

#loops

#for (par)

#while ( enquanto - faça)
count = 0
while op != "q":
    print(f"\tloop: {count}")
    
    op = input("\tInsira o valor 'q': ")
    count += 1

print("--" * 10)
num = 0

while num < 10:
    print(num)
    num += 1

'''
num++
v
num = num + 1

num += 4
v
num = num + 4

num *= 4
v
num = num * 4


num -= 4
v
num = num - 4
'''

range(0, 10, 2)
'''
range(a, b, c)

a- LB
b- UP
c- step, se oculto: c = 1

range(1, 5)
R: 1, 2, 3, 4

range(5)
R: 0, 1, 2, 3, 4

range(0, 10, 2)
0, 2, 4, 6, 8
'''

print("--" * 10)

for elm in range(0, 100):
    print(elm)
    if elm % 2 == 50:
        continue

    print(elm)

print("---" * 10)
print("---" * 10)

nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
             "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",
                     "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

for nome in nomes:
    print(nome)

print(nome.count("Daniela"))

print(nomes.__len__())
print(len(nomes))

print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("pedro" in nomes)

#nomes.sort(reverse=True)

print("---------------" * 5)
nomes.sort()
print(nomes)

"""
var 
tipos de dados
tuplos 
op com var 
if 
elif 
else 
and/or
match
while
for 
list
"""


while True:
    nota = input("Escreva um numero entre 0 e 10: ")
    try:
        nota = int(nota)
        if nota < 0 or nota > 10:
            print("Valor inválido. Por favor, reforme o valor para ser entre 0 e 10.")
        else:
            print("Nota válida!")
            break
    except ValueError:
        print("Valor inválido. Por favor, informe um número entre 0 e 10.")