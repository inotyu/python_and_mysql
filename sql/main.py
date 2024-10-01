from inserir import inserir
from atualizar import atualizar
from deletar import deletar
from ler import ler
from conectar import conectar

def menu():
    conexao, cursor = conectar()
    
    while True:
        escolha = int(input('''Escolha uma opção abaixo:
    1 - Adicionar Aluno
    2 - Atualizar Aluno
    3 - Deletar Cadastro
    4 - Ver Cadastros
    Informe sua opção: '''))
    
        if escolha in [1, 2, 3, 4]:
            if escolha == 1:
                inserir(conexao, cursor)
            elif escolha == 2:
                atualizar(conexao, cursor)
            elif escolha == 3:
                deletar(cursor, conexao)
            elif escolha == 4:
                ler(cursor)  
        else:
            print('Opção inválida!')
            continue
        

        continuar = input('Deseja realizar outra ação? (s/n): ').strip().lower()
        if continuar != 's':
            break


    cursor.close()
    conexao.close()

menu()
