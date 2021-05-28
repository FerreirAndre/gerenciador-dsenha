import sqlite3, time, click

con = sqlite3.connect("dsenhas.db")
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS service(
        servico TEXT NOT NULL,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    );
''')

class GerenciadorDeSenha:
    def menu():
        print("============================")
        print("\nI - inserir")
        print("\nD - deletar")
        print("\nE - editar")
        print("\nM - mostrar todos")
        print("\nU - mostrar um")
        print("\nS - Sair")
        print("\n============================")
        
    def inserir(servico,usuario,senha):
        cursor.execute(f'''
        INSERT INTO service(servico,usuario,senha)
        VALUES('{servico}','{usuario}','{senha}');
        ''')
        con.commit()
    
    def editar(servico,usuario,senha):
        cursor.execute(f'''
        UPDATE service SET
        usuario = '{usuario}',
        senha = '{senha}'
        WHERE servico = '{servico}';
        ''')
        con.commit()

    def remover(servico):
        cursor.execute(f'''
        DELETE *
        FROM service
        WHERE service ='{servico}'
        ''')

    def mostrarTodos():
        cursor.execute('''
        SELECT servico
        FROM service;
        ''')
        for service in cursor.fetchall():
            print(service)
    
    def mostrarUm(servico):
        cursor.execute(f'''
        SELECT usuario, senha 
        FROM service
        WHERE servico = '{servico}'
        ''')
        if cursor.rowcount == 0:
            print("Nao tem esse servico no banco de dados.")
        else:
            for usuario in cursor.fetchall():
                print(usuario)



if __name__ == "__main__":
    gds = GerenciadorDeSenha
    while True:
        gds.menu()
        escolha = input().upper()
        if escolha == "I":
            print("entre com os dados\n")
            servico = input("servico: ")
            usuario = input("usuario: ")
            senha = input("senha: ")
            gds.inserir(servico,usuario,senha)
        
        elif escolha == "D":
            servico = input("digite o servico que deseja deletar: ")
            gds.remover(servico)
        
        elif escolha == "E":
            servico = input("digite o servico que deseja editar: ")
            usuario = input("novo usuario: ")
            senha = input("nova senha: ")
            gds.editar(servico,usuario,senha)
        
        elif escolha == "M":
            gds.mostrarTodos()
        
        elif escolha == "U":
            servico = input("servico que deseja ver a senha: ")
            gds.mostrarUm(servico)

        elif escolha == "S":
            print("Saindo...")
            exit()
        
        else:
            print("escolha indisponivel, selecione uma escolha possivel.")
        
        time.sleep(2)
        click.clear()
