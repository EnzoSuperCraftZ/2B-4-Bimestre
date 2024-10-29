#Enzo Kail Vizalli, Enoch Souza, Kenttonny, Miguel Franco
#2° B Vespertino
from classes import *

usuarios = []
reviews = []
def registrar_usuario():
    tipo = input("Tipo de usuário:\n\n1 - Aluno\n2 - Visitante\n3 - Chefe De Departamento\nEscolha o seu tipo de usuário: ").strip().upper()
    print("\nRegistrar informações\n")
    nome = input("Digite seu nome completo: ").strip()
    cpf = input("Digite seu CPF: ").strip()
    idade = input("Digite sua Idade: ").strip()
    senha = input("Digite sua senha: ").strip()


    if any(usuario.nome == nome for usuario in usuarios):
        print("\nErro: Pessoa já cadastrada.")
        return

    if tipo == '1':
        matricula = input("Digite sua matrícula: ").strip()
        curso = input("Digite seu curso: ").strip()
        usuario = Aluno(nome, cpf, idade, matricula, curso, senha)
        usuarios.append(usuario)
    elif tipo == '2':
        motivo = input("Digite seu motivo para sua visita: ").strip()
        usuario = Visitante(nome, cpf, idade, motivo, senha)
        usuarios.append(usuario)
    elif tipo == '3':
        departamento = input("Digite seu departamento: ").strip()
        usuario = ChefeDepartamento(nome, cpf, idade, senha, departamento)
        usuarios.append(usuario)
    else:
        print("Tipo de usuário inválido.")
        return

    print("\nUsuário registrado com sucesso.")

def fazer_feedback():
    nota = None
    feedback = None
    tipo = input("Tipo de review:\n\n1 - Lugar\n2 - Departamento\nEscolha o seu tipo de feedback: ").strip().upper()
    def feedback2():
        print("\nRegistrar informações\n")
        nota = input("Digite a nota: ").strip()
        feedback = input("Redija sua crítica: ").strip()




    if tipo == '1':
        local = input("Digite o local: ").strip()
        feedback2()
        review = Local(nota, feedback, local)
        reviews.append(review)
    elif tipo == '2':
        departamento = input("Digite o departamento: ").strip()
        feedback2()
        review = Departamento(nota, feedback, departamento)
        reviews.append(review)
    else:
        print("Tipo de review inválido.")
        return

    print("\nFeedback registrado com sucesso.")

def fazer_login():
  print("\nFazer login \n")
  cpf = input("\nDigite seu CPF: ").strip()
  senha = input("Digite sua senha: ").strip()


  for usuario in usuarios:
      if usuario.cpf == cpf and usuario.senha == senha:
          return usuario
      else:
          print("\nCPF ou senha incorretos.\n")

1
def menu():
  while True:
      print("Sistema de Feedback\n")
      print("1 - Cadastrar")
      print("2 - Fazer login")
      print("3 - Feedback")
      print("4 - Sair")
      opcao = input("\nEscolha uma opção: ").strip()

      if opcao == '1':
          registrar_usuario()
      elif opcao == '2':
          usuario_logado = fazer_login()
          if usuario_logado:
              print(f"\nBem-vindo, {usuario_logado.nome}!\n")
      elif opcao == '3':
        fazer_feedback()           
      elif opcao == '4':
          print("\nSaindo...")
          break
      else:
          print("Opção inválida.")

  

menu()