import mysql.connector

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        password = '',
        database = 'escola',
        user = 'root',
        port = '3306'
    )
    print('conectado com sucesso')
    sql = 'select * from aluno order by nome desc'
    cursor = conexao.cursor(dictionary = True)
    cursor.execute(sql)
    for aluno in cursor:
        media = (aluno["nota1"] + aluno["nota2"]) /2
        if media  >=7:
            situação = "aprovado"
        else:
            situação = "reprovado"

        print(f'{aluno["nome"]}')
        print(f'{aluno["nota1"]} - {aluno["nota2"]} ')
        print(f'{media} - {situação}') 
except:
    print('conexão não encontrada')
finally:
    if conexao != None:
        conexao.close()
