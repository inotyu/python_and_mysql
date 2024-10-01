from datetime import datetime

def inserir(conexao, cursor):
    nome = input("Nome do aluno: ")
    nascimento_pessoa = input("Data de nascimento do aluno (dd/mm/aaaa): ")
    nascimento_pessoa = datetime.strptime(nascimento_pessoa, '%d/%m/%Y').strftime('%Y-%m-%d')
    peso_pessoa = float(input("Peso do aluno: "))
    altura_pessoa = float(input("Altura do aluno: "))
    nacionalidade = input("Nacionalidade do aluno: ")
    command = """
    INSERT INTO pessoa (nome_pessoa, nascimento_pessoa, peso_pessoa, altura_pessoa, nacionalidade) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(command, (nome, nascimento_pessoa, peso_pessoa, altura_pessoa, nacionalidade))
    conexao.commit()
    print(f"Aluno {nome} foi adicionado com sucesso no banco.")
    cursor.close()
    conexao.close()