from abc import ABC, abstractmethod
class Pessoa(ABC):
  def __init__ (self, nome, cpf, idade, senha):
    self.nome = nome
    self.cpf = cpf
    self.idade = idade 
    self.senha = senha   
    def get_nome(self):
            return self.nome
    def set_nome(self, nome):
            self.nome =  nome
    def get_cpf(self):
            return self.cpf
    def set_cpf(self, cpf):
            self.cpf =  cpf
    def get_idade(self):
            return self.idade
    def set_idade(self, idade):
            self.idade =  idade
    def get_senha(self):
            return self.senha
    def set_senha(self, senha):
            self.senha =  senha

  def  __str__(self):
    return self.nome + "" + self.cpf + "," + str(self.idade)

  def exibirPessoa(self):
    print ("nome:" + self.nome + "\nCPF: " +self.cpf + '\nIdade:' + str(self.idade) )


class Aluno(Pessoa): #herança
  def __init__(self, nome, cpf, idade, matricula, curso, senha):
        #person.__init__(self, primeiro, sobrenome, idade)
    super().__init__(nome, cpf, idade, senha)
    self.matricula = matricula
    self.curso = curso
    def get_matricula(self):
            return self.matricula
    def set_matricula(self, matricula):
            self.matricula =  matricula
    def get_curso(self):
            return self.curso
    def set_curso(self, curso):
            self.curso =  curso

  def __str__(self):
    return super().__str__() + "," + str(self.matricula) + "," + self.curso

  def exibirAluno(self):
    print("\nNome:" + self.nome + "\nCPF: " + str(self.cpf) + '\nIdade:' + str(self.idade) + '\nMatricula: ' + str(self.matricula) + "\nCurso: "+ str(self.curso))


class Visitante(Pessoa): #herança
  def __init__(self, nome, cpf, idade, motivo, senha):
    super().__init__(nome, cpf, idade, senha)
    self.motivo = motivo
    def get_motivo(self):
            return self.motivo
    def set_motivo(self, motivo):
            self.motivo =  motivo

  def __str__(self):
    return super().__str__() + "," + self.motivo

  def exibirVisitante(self):
    print("\nNome:" + self.nome + "\nCPF: " + str(self.cpf) + '\nIdade:' + str(self.idade) + '\nMotivo da vinda: ' + str(self.motivo))

class ChefeDepartamento(Pessoa): #herança
  def __init__(self, nome, cpf, idade, departamento, senha):
    super().__init__(nome, cpf, idade, senha)
    self.departamento = departamento
    def get_departamento(self):
            return self.departamento
    def set_departamento(self, departamento):
            self.departamento =  departamento

  def __str__(self):
    return super().__str__() + "," + self.departamento

  def exibirChefeDepartamento(self):
    print("\nNome:" + self.nome + "\nCPF: " + str(self.cpf) + '\nIdade:' + str(self.idade) + '\nDepartamento: ' + self.departamento)

class Feedback(ABC):
  def __init__ (self, nota, feedback, usuario_logado):
    self.nota = nota
    self.feedback = feedback
    self.usuario_logado = usuario_logado #associação
    def get_nota(self):
            return self.nota
    def set_nota(self, nota):
            self.nota =  nota
    def get_feedback(self):
            return self.feedback
    def set_feedback(self, feedback):
            self.feedback = feedback
    def get_usuario_logado(self):
            return self.usuario_logado
    def set_usuario_logado(self, usuario_logado):
            self.usuario_logado = usuario_logado
    '''def get_pessoa(self):
            return self.pessoa
    def set_pessoa(self, pessoa):
            self.pessoa = pessoa'''

  def  __str__(self):
       '''return str(self.feedback) + "," + str(self.usuario_logado.nome)'''
       return "\nNome: " + str(self.usuario_logado.nome) + "\nFeedback: " + str(self.feedback)

  def exibirFeedback(self):
    print ("\nNome:" + self.nomePessoa + "\nTipo de review:" + self.tipo + "\nNota (de 1 a 10): " + str(self.nota) + '\nFeedback: ' + self.feedback)

class FeedbackLocal(Feedback): #herança
  def __init__ (self, nota, feedback, local, usuario_logado):
    super().__init__(nota, feedback, usuario_logado)
    self.local = local
    def get_local(self):
            return self.local
    def set_local(self, local):
            self.local =  local

  def __str__(self):
    '''return super().__str__() + "," + self.local'''
    return "\nNome: " + str(self.usuario_logado.nome) + "\nLocal: " + self.local + "\nNota: " + self.nota + "\nFeedback: " + str(self.feedback)

  def exibirLocal(self):
      print ("\nNome:" + self.usuario_logado + "\nTipo de review: " + self.tipo + "\n\nAlvo da review: " + self.local + "\nNota (de 1 a 10): " + str(self.nota) + '\nFeedback: ' + self.feedback)

class FeedbackDepartamento(Feedback): #herança
  def __init__ (self, nota, feedback, departamento, usuario_logado):
    super().__init__(nota, feedback, usuario_logado)
    self.departamento = departamento
    def get_departamento(self):
            return self.departamento
    def set_departamento(self, departamento):
            self.departamento =  departamento

  def __str__(self):
    '''return super().__str__() + "," + self.departamento'''
    return  "\nNome: " + str(self.usuario_logado.nome) + "\nDepartamento: " + self.departamento + "\nNota: " + self.nota + "\nFeedback: " + str(self.feedback)

  def exibirDepartamento(self):
    print ("\nNome:" + self.usuario_logado + "\nTipo de review: " + self.tipo + "\n\nAlvo da review: " + self.departamento + "\nNota (de 1 a 10): " + str(self.nota) + '\nFeedback: ' + self.feedback)
