import os

opcao =input('''Selecione o que deseja fazer: 
    1- Escaneamento completo de um host ou uma rede 
    2- Escaneamento de range (intervalo) de portas 
    3- Well-Know Ports e seus serviços 
''')

if int(opcao) == 1:
    ip = input("Qual o ip do host/rede que deseja escanear? ")
    os.system("nmap {}".format(ip))

elif int(opcao) == 2:
    ip = input("Qual o ip do host/rede que deseja escanear? ")
    range1 = input("Qual o primeiro número do range de portas que deseja escanear? ")
    range2 = input("Qual o segundo número do range de portas que deseja escanear? ")
    os.system("nmap -p{}-{} {}".format(range1, range2, ip))

elif int(opcao) == 3:
    ip = input("Qual o ip do host/rede que deseja escanear? ")
    os.system("nmap sV --top-ports 1023 {}".format(ip))



