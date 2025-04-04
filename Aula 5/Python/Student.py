class Student:
    # definido o nosso método construtor e atributos
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    # adicionando as notas
    def add_grade(self, grade):
        self.grades.append(grade)
    
    # mostrando a média entre as notas
    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # Mostra se o aluno esta com mais de 60 na nota de 100
    @property
    def is_passing(self):
        return self.get_average_grade() >= 60
    
    # método que chama todos os outros métodos
    @classmethod
    def main(cls):
        # lista que recebe os estudantes
        students = []
        
        while True:
            # o nosso menu
            print("1 - Adicionar Aluno")
            print("2 - Adicionar Nota")
            print("3 - Verificar aprovação")
            print("4 - Apresentação do Aluno")
            print("5 - Sair")
            # Defiunição do índice do menu
            choice = int(input("Escolha uma opção: "))
            
            # Cadastro de alunos
            if choice == 1:
                name = input("Nome do Aluno: ")
                age = int(input("Idade do Aluno: "))
                student = cls(name, age)
                students.append(student)
                print("Aluno adicionado")
            
            # Cadastro de notas de alunos
            elif choice == 2:
                # verificação se existe objeto definido na lista de students
                if not students:
                    print("Nenhum aluno cadastrado!")
                    # se a lista for vazia volta para o menu
                    continue
                # forma o índice de aluno na lista de students
                for idx, student in enumerate(students):
                    print(f"{idx+1} - {student.name}")
                # opção de escolha o índice do aluno
                student_idx = int(input("Escolha o número do aluno: ")) -1
                
                if 0 <= student_idx < len(students): # verificar se o índicve esta cerrto
                    # Define a nota do aluno
                    grade = float(input("Nota do aluno: "))
                    # escolhendo o objeto na lista e inserindo a nota
                    students[student_idx].add_grade(grade)
                    print("Nota adicionada!")
                else:
                    print("Índice de aluno inválido!")
            
            elif choice == 3:
                if not students:
                    print("Nenhum aluno cadastrado!")
                    continue
                for student in students:
                    average_grade = student.get_average_grade()
                    if average_grade >= 6.0:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"
                    
                    print(f"""
                          - Nome do estudante{student.name} 
                          - Média {average_grade} 
                          - Status {status}
                          """)
            
            elif choice == 4:
                # verificação se existe objeto definido na lista de students
                if not students:
                    print("Nenhum aluno cadastrado!")
                    # se a lista for vazia volta para o menu
                    continue
                # forma o índice de aluno na lista de students
                for idx, student in enumerate(students):
                    print(f"""
                        Matricula do aluno: {idx+1}
                        Nome do aluno  - {student.name}
                        Idade do aluno - {student.age}
                        Notas do aluno - {student.grades}
                          """)
            
            
            elif choice == 5:
                print("Saíndo....")
                print("Obrigado por usar o nosso sistema!")
                print("Até a próxima!")
                break
            
            else:
                print("Opção errada, escolha novamente!")

estudante = Student.main()