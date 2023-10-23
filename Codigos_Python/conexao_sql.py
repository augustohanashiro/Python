import mysql.connector
from mysql.connector import Error

# 1° Passo, tentar estabelecer conexão com o nosso banco 
# 2° Passo, Colocar o comando a ser executado em uma variavel
# 3° Passo, Criar um cursos que é o que vai receber o comando da nossa query
# 4° Passo, Colocar o cursos para executar o comando,(caso o comando altere a
#           tabela, é preciso fazer um commit em seguida) 
# 5° Passo, Dentro do Except verificar se a conexão foi estabelecida
# 6° Passo, Caso estabelecida, fechar a conexão do banco junto ao cursos

# Comando Insert
# try:
#     con = mysql.connector.connect(host ="localhost", database ="conexaopython", user ="root",password = "adm123")

#     comando_insert = "insert into perfil values(3,'Sheila','Hanashiro',22,'F')"
#     comando = "update perfil set sobrenome = 'Fukushima' where id_cadastro = 3"
#     comando_create_table = """Create table Endereco(
#             Id int primary key,
#             Rua varchar(30),
#             Numero int,
#             Cidade varchar(30),
#             Estado char(2),
#             CEP char(8),
#             Complemento varchar(30)
#         )"""

#     cursor = con.cursor()
#     cursor.execute(comando_insert)
#     con.commit()
try:
    con = mysql.connector.connect(host = "localhost", database = "conexaopython", user = "root", password = "adm123")
    comando = "Select * from perfil"
    cursor = con.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    print("Numero de linhas encontradas",cursor.rowcount)
    print(*linhas, sep="\n")
    # for linha in linhas:
    #     print("Id",linha[0])
    #     print("Nome",linha[1])
    #     print("Sobrenome",linha[2])
    #     print("Sexo",linha[3])

except Error as erro:
    print(f"Deu erro\n{erro}")
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Deu tudo Certo")