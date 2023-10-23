import mysql.connector

def conectar():
    global con 
    global cursor 
    try:
        con = mysql.connector.connect(user= "root", password = "adm123", database = "conexaopython", host = "localhost")
        cursor = con.cursor()
    except Exception as e:
        print("Acesso negado!")
        

def consulta_cadastro(nometabela,coluna = "",filtro=""):
    try:
        conectar()
        if filtro and coluna:
            comando_consulta = f"""SELECT * FROM {nometabela} WHERE {coluna} = '{filtro}'
        """
        else:
            comando_consulta = f"SELECT * FROM {nometabela}"
        
        cursor.execute(comando_consulta)
        linhas = cursor.fetchall()
        print("Registros encontrados: ",cursor.rowcount)
        print(*linhas, sep="\n")
    except Exception as e :
        print("Falha na conexão\n",e)
    
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def atualiza_cadastro(nometabela,coluna,novo_valor,coluna_filtro,valor_filtro):
    try:
        conectar()
        comando_atualiza = f"""UPDATE {nometabela} 
                            SET {coluna} = '{novo_valor}'
                            WHERE {coluna_filtro} = '{valor_filtro}'
        """
        cursor.execute(comando_atualiza)
        con.commit()
    except Exception as e:
        print("Falha na conexão\n", e)
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def inserir_dado(nometabela,*values):
    try:
        conectar()
        comando_inserir = f"""INSERT INTO {nometabela} values('{values[0]}','{values[1]}','{values[2]}','{values[3]}','{values[4]}')
    """
        cursor.execute(comando_inserir)
        con.commit()
    except Exception as e:
        print("Erro na conexão:\n",e)
    
    finally:
        if con.is_connected():
            con.close()
            cursor.close()

# inserir_dado("perfil",4,"Humberto","Hanashiro","50","M")
consulta_cadastro("perfil")