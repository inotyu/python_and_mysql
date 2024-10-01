from conectar import conectar
from ler import ler
def deletar(conexao, cursor):
    conexao, cursor = conectar()
    opcao = int(input('''Deseja deletar por ID ou nome do aluno?
                      1 - ID
                      2 - Nome
                      Escolha sua opção: '''))
    if opcao in [1, 2]:
            if opcao == 1:
                option = int(input('''Gostaria de ver a lista de alunos antes de deletar?
                                   1 - Sim
                                   2 - Não
                                   Escolha sua opção: '''))
                if option == 1:
                    ler(cursor)
                    id_pessoas = int(input("Insira o ID do aluno a ser deletado: "))
                    command = "DELETE FROM pessoa WHERE id_pessoas = %s"
                    cursor.execute(command, (id_pessoas,))
                    conexao.commit()
                    print("Aluno deletado com sucesso.")
                    cursor.close()
                    conexao.close()
                if option == 2:
                    id_pessoas = int(input("Insira o ID do aluno a ser deletado: "))
                    command = "DELETE FROM pessoa WHERE id_pessoas = %s"
                    cursor.execute(command, (id_pessoas,))
                    conexao.commit()
                    print("Aluno deletado com sucesso.")
                    cursor.close()
                    conexao.close()
                    
            elif opcao == 2:
                option = int(input('''Gostaria de ver a lista de alunos antes de deletar?
                                   1 - Sim
                                   2 - Não
                                   Escolha sua opção: '''))
                
                if option == 1:
                    ler()
                    nome_pessoa = input("Insira o nome do aluno a ser deletado: ")
                    command = "DELETE FROM pessoa WHERE nome_pessoa = %s"
                    cursor.execute(command, (nome_pessoa,))
                    conexao.commit()
                    print("Aluno deletado com sucesso.")
                    cursor.close()
                    conexao.close()
                if option == 2:
                    nome_pessoa = input("Insira o nome do aluno a ser deletado: ")
                    command = "DELETE FROM pessoa WHERE nome_pessoa = %s"
                    cursor.execute(command, (nome_pessoa,))
                    conexao.commit()
                    print("Aluno deletado com sucesso.")
                    cursor.close()
                    conexao.close()
    else:
        print("Opção inválida.")
        cursor.close()
        conexao.close()
