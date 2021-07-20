import os
import time
import platform

sy = platform.system()
tm = 5

try:
    while True:
        print('Codigo feito Por Kauan Costa Silva e Pedro Rosendo')

        if sy == 'Linux':
            print('======================================')
            print('|          Opções          | Pacotes |')
            print('======================================')
            print('|1-Instalar um programa    |(APT)    |')
            print('|2-Instalar um programa    |(SNAP)   |')
            print('|3-Instalar um programa    |(FLATPAK)|')
            print('|4-Remover um programa     |(APT)    |')
            print('|5-Remover um programa     |(SNAP)   |')
            print('|6-Remover um programa     |(FLATPAK)|')
            print('|7-Atualizar o sistema     |    X    |')
            print('|8-Instalar um jogo e utils|    X    |')
            print('|====================================|')
            print('|9-         Sair do programa         |')
            print('======================================')
            op1 = int(input('O que você deseja fazer? : '))
            os.system("clear")

            if op1 == 1:
                o1 = input('Qual pacote você deseja instalar? : ')
                os.system("sudo apt update")
                os.system("sudo apt upgrade -y")
                os.system("sudo apt install {} -y".format(o1))
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 2:
                o2 = input('Qual pacote você deseja instalar? : ')
                os.system("sudo apt update")
                os.system("sudo apt upgrade -y")
                os.system("sudo apt install snap -y")
                os.system("sudo apt install snapd -y")
                os.system("sudo snap install {} --stable -y".format(o2))
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 3:
                o3 = input('Qual pacote você deseja instalar? : ')
                os.system("sudo apt update")
                os.system("sudo apt upgrade -y")
                os.system("sudo apt install flatpak -y")
                os.system(
                    "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
                os.system("clear")
                print("FLATPAK INSTALADO COM SUCESSO SERÁ PRECISO REINICIAR A MAQUINA (CASO SEJA SUA PRIMEIRA VEZ INSTALANDO ALGO EM FLATPAK)")
                print("É RECOMENDAVEL REINICIAR O PC CASO SEJA A PRIMEIRA VEZ")
                time.sleep(tm)
                o4 = str(
                    input('Essa é a sua primeira vez utilizando flatpak? (S/N): '))

                if 'n' or 'N' == o4:
                    os.system("sudo flatpak install {}".format(o4))
                    os.system("clear")
                    print('FECHANDO O APP')
                    time.sleep(tm)
                    exit()

                else:
                    os.system("clear")
                    print('FECHANDO O APP')
                    time.sleep(tm)
                    exit()
                    os.system("sudo reboot")

            elif op1 == 4:
                o5 = str(input('Qual pacote você deseja remover? : '))
                os.system("sudo apt purge {} -y".format(o5))
                os.system("sudo apt autoremove -y")
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 5:
                o6 = str(input('Qual pacote você deseja remover? : '))
                os.system("sudo snap remove {}".format(o6))
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 6:
                o7 = str(input('Qual pacote você deseja remover? : '))
                os.system("sudo flatpak uninstall {}".format(o7))
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 7:
                os.system("sudo apt update")
                os.system("sudo apt upgrade")
                os.system("clear")
                print('FECHANDO O APP')
                time.sleep(tm)
                exit()

            elif op1 == 8:
                print('')
            print('============================')
            print('|  1.Lutris    | 4.Psspp   |')
            print('|  2.CS 1.6    | 5.Stem    |')
            print('|  3.wine                  |')
            print('============================')
            print('|    6.SAIR DO PROGRAMA    |')
            print('============================')
            op3 = int(input('Qual jogo você deseja intalar? '))
            os.system("clear")

            if op3 == 1:
                print('Instalando o Lutris')
                os.system("sudo chmod 777 lutris.sh")
                os.system("sudo ./lutris.sh")
                os.system('clear')
                print('Lutris instalado !!!')
                time.sleep(tm)
                exit()

            elif op3 == 2:
                print('Instalando o CS 1.6')
                os.system("sudo chmod 777 cs_1.6.sh")
                os.system("sudo ./cs_1.6.sh")
                print('CS 1.6 instalado !!!')
                time.sleep(tm)
                exit()

            elif op3 == 3:
                print('instalando o PPSSPP')
                os.system("sudo chmod 777 ppsspp.sh")
                os.system("sudo ./ppsspp.sh")
                print('PPSSPP instalado !!!')
                time.sleep(tm)
                exit()

            elif op3 == 4:
                print('instalando o Steam')
                os.system("sudo chmod 777 steam")
                os.system("sudo ./steam.sh")
                print('Steam instalado !!!')
                time.sleep(tm)
                exit()

            elif op3 == 5:
                print('instalando o wine')
                os.system("sudo chmod 777 wine")
                os.system("sudo ./wine.sh")
                print('wine instalado !!')
                time.sleep(tm)
                exit()

            elif op3 == 6:
                print('muito obrigado !')
                print('volte sempre')
                exit()

            else:
                print('Opção invalida. Tente novamente')
                print('=-=' * 10)

        elif op1 == 9:
            os.system("clear")
            print('FECHANDO O APP')
            time.sleep(tm)
            exit()

        else:
            os.system("clear")
            print('FECHANDO O APP')
            time.sleep(tm)
            exit()

        if sy  == 'Windows':
            print('===============================')
            print('| 1. Limpar lixeira           |')
            print('| 2. Limpar as Pastas (cache) |')
            print('| 3. Sair do programa         |')
            print('===============================')
            opçao = int(input('o que voce deseja vazer? '))
            os.system("cls")

        if opçao == 1:
            os.system("rd /S /Q c:\$Recycle.bin")
            os.system("cls")
            print('Lixeira limpa')
            time.sleep(tm)
            exit()

        elif opçao == 2:
            os.system("rd /S /Q c:\\$Recycle.bin")
            os.system("del /q C:\\Windows\\Temp\\*")
            os.system("del /q C:\\Users\\%username%\\AppData\\Local\\Temp\\*")
            os.system("del /q C:\\Windows\\Prefetch\\*")
            os.system("cls")
            print('Pastas apagadas')
            time.sleep(tm)
            exit()

        elif opçao == 3:
            print('muito obrigado !')
            print('volte sempre')
            time.sleep(tm)
            exit()

        else:
            os.system("cls")
            print('Opção invalida. Tente novamente')
            print('=-=' * 10)

except Exeception as s:
    print('ERRO: ', s)
