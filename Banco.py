from models import Usuario, Conta


class Banco:
    def __init__(self):
        self.usuarios = []
        self.numero_conta_atual = 1
    

    def cadastrar_usuario(self, username, senha, is_admin=False):
        for u in self.usuarios:
            if u.username == username:
                print("Usuário já existe.")
                return 

        usuario = Usuario(username, senha, is_admin)
        usuario.conta = Conta(self.numero_conta_atual)

        self.numero_conta_atual += 1
        self.usuarios.append(usuario)

        print(f"Usuário {username} cadastrado com sucesso. Conta número {usuario.conta.numero} criada.")

    def autenticar(self, username, senha):
        for u in self.usuarios:
            if u.username == username and u.senha == senha:
                print(f"Usuário {username} autenticado com sucesso.")
                return u
        return None

