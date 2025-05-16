import tkinter as tk
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        raise NotImplementedError("Subclasse deve implementar o método apresentar().")

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        return f"Sou o aluno {self.nome} e curso {self.curso}."

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Sou o professor {self.nome} e leciono {self.disciplina}."

def apresentar_pessoas():
    aluno = Aluno("Zé da Manga", "Engenharia de Software")
    professor = Professor("Zé da Couve", "POO")

    pessoas = [aluno, professor]
    mensagens = [p.apresentar() for p in pessoas]

    messagebox.showinfo("Apresentações", "\n".join(mensagens))


janela = tk.Tk()
janela.title("Sistema de Apresentações")
janela.geometry("300x150")

botao = tk.Button(janela, text="Mostrar Apresentações", command=apresentar_pessoas)
botao.pack(pady=40)

janela.mainloop()