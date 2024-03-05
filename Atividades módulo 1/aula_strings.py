#Alguns métodos para manipular String
curso = "pyThon"
curso2 = "     Python    "

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso2.strip()+".") #remove espaços
print(curso2.lstrip()+".") #remove espaços da esquerda
print(curso2.rstrip()+".") #remove espaços da direta 

print(curso.center(12, "#"))
print(curso.center(12))
print(".".join(curso))

#Interpolação de variáveis

nome = "Maria"
idade = 30
profissao = "professora"
especificacao = "matemática"

pessoa = {"nome":"Maria", "idade":30, "profissao":"professora", "especificacao":"matemática"}

print("Me chamo %s tenho %d anos de idade e sou %s de %s" %(nome, idade, profissao, especificacao))
print("Me chamo {} tenho {} anos de idade e sou {} de {}" .format(nome, idade, profissao, especificacao))
print("Me chamo {1} tenho {3} anos de idade e sou {0} de {2}" .format(profissao, nome, especificacao, idade))
print("Me chamo {nome} tenho {idade} anos de idade e sou {profissao} de {especificacao}" .format(profissao=profissao, nome=nome, especificacao=especificacao, idade=idade))
print("Me chamo {nome} tenho {idade} anos de idade e sou {profissao} de {especificacao}" .format(**pessoa))


PI = 3.14159
print(f"Valor de PI: {PI}" )
print(f"Valor de PI: {PI:.2f}" )

#Fatiamento de strings

texto = "Me chamo Maria tenho 30 anos de idade e sou professora de matemática!"

print(texto[1])
print(texto[-1])
print(texto[:9])
print(texto[5:])
print(texto[10:16])
print(texto[10:16:2])
print(texto[:])
print(texto[::-1])

#Strings multilinhas
#mensagens com diferentes recuos
nome = "Paula"
mensagem = f""" Oi meu nome é {nome}, 
                estou aprendendo Python"""

print(mensagem)


mensagem2 = f'''Oi meu nome é {nome},                 estou aprendendo Python'''

print(mensagem2)

