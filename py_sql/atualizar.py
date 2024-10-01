from datetime import datetime

def atualizar(conexao, cursor):
    opcao = int(input('''Deseja atualizar por nome ou ID do aluno?
                      1 - Nome
                      2 - ID
                      Escolha sua opção: '''))
    if opcao in [1, 2]:
            if opcao == 1:
                nome_atu = str(input("Insira o nome do aluno a ser atualizado: "))
                nome_pessoa = input("Novo nome do aluno: ")
                nascimento_pessoa = input("Data de nascimento do aluno (dd/mm/aaaa): ")
                nascimento_pessoa = datetime.strptime(nascimento_pessoa, '%d/%m/%Y').strftime('%Y-%m-%d')
                peso_pessoa = float(input("Peso do aluno: "))
                altura_pessoa = float(input("Altura do aluno: "))
                nacionalidade = input("Nacionalidade do aluno: ")
                command = """
                UPDATE pessoa 
                SET nome_pessoa = %s, nascimento_pessoa = %s, peso_pessoa = %s, altura_pessoa = %s, nacionalidade = %s 
                WHERE nome_pessoa = %s
                """
                cursor.execute(command, (nome_pessoa, nascimento_pessoa, peso_pessoa, altura_pessoa, nacionalidade, nome_atu))
                conexao.commit()
                print("Dados do aluno atualizados com sucesso.")
            if opcao == 2:
                id_pessoas = int(input("Insira o nome do aluno a ser atualizado: "))
                nome_pessoa = input("Novo nome do aluno: ")
                nascimento_pessoa = input("Data de nascimento do aluno (dd/mm/aaaa): ")
                nascimento_pessoa = datetime.strptime(nascimento_pessoa, '%d/%m/%Y').strftime('%Y-%m-%d')
                peso_pessoa = float(input("Peso do aluno: "))
                altura_pessoa = float(input("Altura do aluno: "))
                nacionalidade = input("Nacionalidade do aluno: ")
                command = """
                UPDATE pessoa 
                SET nome_pessoa = %s, nascimento_pessoa = %s, peso_pessoa = %s, altura_pessoa = %s, nacionalidade = %s 
                WHERE id_pessoas = %s
                """
                cursor.execute(command, (nome_pessoa, nascimento_pessoa, peso_pessoa, altura_pessoa, nacionalidade, id_pessoas))
                conexao.commit()
                print("Dados do aluno atualizados com sucesso.")
                
    cursor.close()
    conexao.close()


