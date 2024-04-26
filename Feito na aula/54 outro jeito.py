def verificarDisponibilidade(listaFuncionario, nome, salario, cargo):

    if len(listaFuncionario)<=5:
        if cargo != 'Professor':
            funcionario = Funcionario(nome, salario, cargo)
            listaFuncionario.append(funcionario)
        else:
            controleProfessores = 0
            for funcionario in listaFuncionario:
                if funcionario.cargo == 'Professor':
                    controleProfessores+= 1

            if controleProfessores <2:
                funcionario = Funcionario(nome, salario, cargo)
                listaFuncionario.append(funcionario)
            else:
                print('Não há disponibilidade para cadastrar mais professores')
    else:
        print('Não há mais vagas')

class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salraio = salario
        self.cargo = cargo
        self.diciplinas = []
#mudar coisos
    def mudarNome(self, nome):
        self.nome = nome

    def cadatrarDisciplinas(self, disciplinas):
        if self.cargo == 'Professor':
            self.diciplinas.append(disciplinas)
        else:
            print('Só professores podem lecionar')



lista = []
Funcionario1 = Funcionario('Dio', 1000, 'Professor')
Funcionario2 = Funcionario('Jodio', 5000, 'Professor')

lista.append(Funcionario1)
lista.append(Funcionario2)
verificarDisponibilidade(lista, 'Leila', 1000, 'Pedagoga')


Funcionario1.cadatrarDisciplinas('Portugues')
lista[2].cadatrarDisciplinas('Portugues')


for funcionario in lista:
    print(Funcionario1.diciplinas)