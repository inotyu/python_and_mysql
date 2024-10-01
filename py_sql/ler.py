def ler(cursor):
    comando = "SELECT * FROM PESSOA"
    cursor.execute(comando)
    resultado = cursor.fetchall()
    
    print(f'- {"ID".ljust(3)} -- {"Nome".ljust(15)} -- {"Preço".ljust(5)}')
    for i,j in enumerate(resultado,start=1):
        a = j
        print(f'{i} │ {str(j[0]).ljust(3)} │ {j[1].ljust(15)} │ {str(j[2]).ljust(5)}')