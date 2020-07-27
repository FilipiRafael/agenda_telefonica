from sistema import sistemas
from time import sleep

agenda = list()

while True:
    opcao = sistemas.menu()
    if opcao == 0:
        print('Programa finalizado com sucesso!')
        sleep(0.5)
        break
    elif opcao == 1:
        sistemas.novo()
        sleep(1)
    elif opcao == 2:
        sistemas.altera()
        sleep(1)
    elif opcao == 3:
        sistemas.apaga()
        sleep(1)
    elif opcao == 4:
        sistemas.lista()
        sleep(1)
    elif opcao == 5:
        sistemas.grava()
        sleep(1)
    elif opcao == 6:
        sistemas.read()
        sleep(1)
    elif opcao == 7:
        sistemas.mostrar_tamanho()
        sleep(1)
    elif opcao == 8:
        sistemas.ordenar_agenda()
        sleep(1)
    
