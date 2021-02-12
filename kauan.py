

import os 
import time


while True:
    

    print('Codigo feito Por Kauan Costa Silva ')


    print(('======================================'))
    print('  Sistemas    |  Outros               *')
    print('=======================================')
    print('* 1. Windows  |  3.Jogos              *')
    print('* 2. linux    |  4.Sair do Programa   *')
    print('=======================================')

    op1 = int(input('O que vc deseja fazer?? '))
    os.system('clear')

    if 1 == op1:
        print('==============================')
        print('* 1. Limpar lixeira          *')
        print('* 2. Limpar as Patas (cache) *')
        print('* 3. Sair do programa        *')
        print('==============================')

        opçao = int(input('o que voce deseja vazer? '))
        os.system('cls')

        if opçao == 1:
            os.system('rd /S /Q c:\$Recycle.bin')
            print('Lixeira limpa')
        
        elif opçao == 2:
            os.system("rd /S /Q c:\\$Recycle.bin")
            os.system("del /q C:\\Windows\\Temp\\*")
            os.system("del /q C:\\Users\\%username%\\AppData\\Local\\Temp\\*")
            os.system("del /q C:\\Windows\\Prefetch\\*")
            print('Pastas apagadas')
            

        elif opçao == 3:
            print('muito obrigado !')
            print('volte sempre')
            exit()
        

        else:
            print('Opção invalida. Tente novamente')
            print('=-=' * 10)

    elif 2 == op1:
        print('===============================')
        print('* 1. instalar um programa     *')
        print('* 2. Remover um programa      *')
        print('* 3. Atualizar o sistema      *')
        print('* 4. Sair do Programa         *')
        print('===============================')

        op2 = int(input('O que voce deseja fazer?? '))
        os.system('clear')
        
        if op2 == 1:
            no1 = input('Informe o nome do pacote para ser instalado ?? ')
            os.system('sudo dpkg -i {}'.format(no1))
            os.system('sudo apt install -f')
            time.sleep(5)

        elif op2 == 2:
            no2 = input('Informe o nome do pacote para ser removido? ')
            os.system('sudo apt purge {} -y'.format(no2))
            os.system('sudo apt autoremove -y')
            time.sleep(5)
            print('>>>>>>> Pacote Removido !!')


        elif op2 == 3:
            print('Atualizando Sistema...')
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade -y')
            time.sleep(5)
            print('>>>>>>> Sistema Atualizado !!')

        elif op2 == 4:
            print('muito obrigado !')
            print('volte sempre')
            exit()
        
        else:
            print('Opção invalida. Tente novamente')
            print('=-=' * 10)


    elif 3 == op1:
        print('===========================')
        print('*           JOGOS         *')
        print('===========================')
        print('*  1.Lutris    | 3.Psspp  *')
        print('*  2.CS 1.6    | 4.Stem   *')
        print('*          5.wine         *')
        print('============================')
        print('*    6.SAIR DO PROGRAMA    *')
        print('============================')

        op3 = int(input('Qual jogo voce deseja intalar?'))
        os.system('clear')

        if op3 == 1:
            print('Instalando o Lutris')
            os.system('sudo add-apt-repository ppa: lutris-team / lutris ')
            os.system('sudo apt update')
            os.system('sudo apt install lutris -y')

        elif op3 == 2:
            print('o cs.16 sera baixado basta clicar e intarlar para isso instale o wine')
            os.system('sudo wget http://files.gs2us.com/cs_16.exe')
            os.system('sudo chmod 777 cs_16.exe')
            print('o Download acabou!!!')

        elif op3 == 3:
            print('instalando o Ppsspp')
            os.system('sudo add-apt-repository ppa:ppsspp/stable')
            os.system('sudo apt-get update')
            os.system('sudo apt-get install ppsspp -y')
            os.system('sudo apt-get install ppsspp-sdl')
            print('ppsspp instalado !!!')

        elif op3 == 4:
            print('instalando o Steam')
            os.system('sudo apt-get install steam -y')
            os.system('sudo apt-get update')
            print('steam instalado !!!')

        elif op3 == 5:
            print('instalando o wine')
            os.system('sudo dpkg --add-architecture i386')
            os.system('sudo apt-get update -y')
            os.system('sudo apt install wine -y')
            os.system('sudo apt install wine64 -y')
            os.system('sudo apt install wine32 -y')
            os.system('sudo apt install winbind -y')
            os.system('sudo apt install winetricks -y')

        elif op3 == 6:
            print('muito obrigado !')
            print('volte sempre')
            exit()

        else:
            print('Opçao invalida. Tente novamente')
            print('=-=' * 10)

    elif 4 == op1:
        print('Saindo...')
        print('Muito obrigado !')
        print('Volte sempre')
        exit()

    else:
        print('Opção invalida. Tente novamente')
        print('=-=' * 10)


    
