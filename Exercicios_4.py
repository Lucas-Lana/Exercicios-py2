# Exercício 1: Multa de Velocidade
def Exercício_1():
    velocidade = float(input("Qual é a velocidade do carro: "))
    if velocidade > 80:
        multa = velocidade - 80
        multa = multa * 7
        print(f'O carro está acima da velocidade permitida, a multa será de R${multa}')
    else:
        print("O carro está dentro do limite de velocidade, não há penalidades")
    print("----------//----------")
    
# Exercício 2: Par ou ímpar ?
def Exercício_2():
    n = int(input("Digite um número: "))
    if n//2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é impar")
    print("----------//----------")
    
# Exercício 3: Preço de passagens
def Exercício_3():
    viagem = float(input("Quantos Km têm a viagem: "))
    if viagem > 200:
        print(f'O preço da passagem é de R${viagem * 0.45}')
    else:
        print(f'O preço da passagem será de R${viagem *0.50}')
    print("----------//----------")
    
# Exercício 4: Aumento de salário
def Exercício_4():
    salario = float(input("Qual o seu salário: "))
    if salario > 1250:
        print(f'O seu salário atualizado é de R${salario *1.10:.2f}')
    else:
        print(f'O seu salário atualizado é de R${salario *1.15:.2f}')
    print("----------//----------")
    
# Exercício 5: Calcúlo de raiz quadrada
def Exercício_5():
    número = int(input("Digite o número: "))
    if número > 0:
        print(f'A raiz quadrada de {número} é {número ** 0.5:.2f}')
    else:
        print(f'O número digitado não pussuí raiz, já que é um número negativo')
    print("----------//----------")

# Exercício 6: Formação de triangulo
def Exercício_6():
    a,b,c = map(float,input("Digite o comprimento das 3 retas, sepradas por ';': ").split(";"))
    if a<b+c and b<a+c and c<a+c:
        print("É possível construir um triangulo com essas 3 retas")
    else:
        print("Não é possível construir um triangulo com essas retas")
    print("----------//----------")

# Exercício 7: Calculadora básica   
def Exercício_7():
    print("Escolha qual operação deseja realizar")
    print("1) Adição\n2) Subtração\n3) Multiplicação\n4) Divisão\n5) Sair")
    escolha = int(input("Escolha (1 à 5): "))
    if escolha == 1:
        print("----------//----------\nAdição selecionada")
        n1 = float(input('Digite o primeiro número da operação: '))
        n2 = float(input('escolha o segundo número da operação: '))
        print(f'{n1} + {n2} = {n1+n2}')
    
    elif escolha == 2:
        print("----------//----------\nSubtração selecionada")
        n1 = float(input('Digite o primeiro número da operação: '))
        n2 = float(input('escolha o segundo número da operação: '))
        print(f'{n1} - {n2} = {n1-n2}')
    
    elif escolha ==3:
        print("----------//----------\nMultiplicação selecionada")
        n1 = float(input('Digite o primeiro número da operação: '))
        n2 = float(input('escolha o segundo número da operação: '))
        print(f'{n1} x {n2} = {n1*n2}')
    
    elif escolha == 4:
        print("----------//----------\nDivisão selecionada")
        n1 = float(input('Digite o primeiro número da operação: '))
        n2 = float(input('escolha o segundo número da operação: '))
        print(f'{n1} / {n2} = {n1/n2}')
    
    elif escolha == 5:
        print("----------//----------")
        print("Saindo...")
    
    else:
        print("----------//----------")
        print("ERRO: Opção inválida")
    
    print("----------//----------")
    
# Exercício 8: Comparação de números
def Exercício_8():
    print("Este programa irá dizer qual número é maior")
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    if a > b:
        print(f'O número  {a} é maior que {b} ({a} > {b}), sendo a diferença: {a} - {b} = {a-b}')
    elif a < b:
        print(f'O número  {b} é maior que {a} ({b} > {a}), sendo a diferença: {b} - {a} = {b-a}')
    else:
        print(f'Os dois números são iguais ({a} = {b}), {a} - {b} = {a-b}')
    print("----------//----------")
    
# Exercício 9: Empréstimo bancário
def Exercício_9():
    casa = float(input("Digite o valor da casa R$"))
    salario = float(input("Digite o seu sálario R$"))
    tempo = float(input("Em quantos anos planeja pagar o empréstimo: "))
    calculo = casa / (tempo * 12)
    if calculo > (salario * 0.30):
        print("O empréstimo foi NEGADO\nA prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.")
    else:
        print("O empréstimo foi APROVADO")
    print("----------//----------")
    
# Exercício 10: Taxação de produto
def Exercício_10():
    produto = float(input('Digite o valor do produto: R$'))
    estado = str(input('Digite as sigla do estado de destino (MG,SP,RJ,MS): '))
    estado = estado.upper()
    if estado ==  "MG":
        print(f'O novo valor do produto com a taxa de {estado} é de R${produto * 1.07:.2f}')
    
    elif estado == "SP":
        print(f'O novo valor do produto com a taxa de {estado} é de R${produto * 1.12:.2f}')
        
    elif estado == "RJ":
        print(f'O novo valor do produto com a taxa de {estado} é de R${produto * 1.15:.2f}')
        
    elif estado == "MS":
        print(f'O novo valor do produto com a taxa de {estado} é de R${produto * 1.08:.2f}')
        
    else:
        print("Estado inválido...")
    print("----------//----------")

# Exercício 11: Pagamento de produto
def Exercício_11():
    
    produto = float(input("Digite o valor do produto: R$"))
    print("Escolha qual forma de pagamento deseja realizar")
    print("1) À vista dinheiro/pix: 10% de desconto\n2) À vista no cartão: 5% de desconto")
    print("3) Em até 2X no cartão: preço formal\n4) EM 3X ou mais no cartão: 20% de juros")
    escolha = int(input("Escolha (1 à 4): "))
    if escolha == 1:
        print(f'O preço à vista no dinheiro/pix fica em R${produto * 0.90}')
    
    elif escolha == 2:
        print(f'O preço à vista no cartão fica em R${produto * 0.95}')
    
    elif escolha ==3:
        print(f'O preço parcelado em até 2X no cartão fica em R${produto * 0.90}')
    
    elif escolha == 4:
        print(f'O preço parcelado em 3X ou mais no cartão fica em R${produto * 1.20}')
        
    else:
        print("----------//----------")
        print("ERRO: Opção inválida")
    
    print("----------//----------")
    
# Exercício 12: Peso Ideal
def Exercício_12():
    sexo = str(input("Digite qual o seu sexo (M) para masculino ou (F) para feminino: "))
    altura = float(input("Digite a sua altura em metros, Ex: 1.80, para 1 metro e 80 cm : "))
    sexo = sexo.upper()
    if sexo == 'M':
        print(f'O seu peso ideal a partir de seu sexo ({sexo}) e altura ({altura}) é {(72.7 * altura) - 58:.2f}')
    
    elif sexo == 'F':
        print(f'O seu peso ideal a partir de seu sexo ({sexo}) e altura ({altura}) é {(62.1 * altura) - 44.7:.2f}')
    
    else:
        print("Sexo inválido...")
        
# Executa todos os programas
def ALL():
    Exercício_1()
    Exercício_2()
    Exercício_3()
    Exercício_4()
    Exercício_5()
    Exercício_6()
    Exercício_7()
    Exercício_8()
    Exercício_9()
    Exercício_10()
    Exercício_11()
    Exercício_12()


# Execução dos programas
# para executar um programa é necessário somente digitar o nome da função    
# Exemplo:
Exercício_1()