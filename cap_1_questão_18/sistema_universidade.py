class Disciplina:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas_lecionadas = []

    def lecionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas_lecionadas:
            self.disciplinas_lecionadas.append(disciplina)
            print(f"O professor {self.nome} agora leciona {disciplina.nome}.")
        else:
            print(f"O professor {self.nome} já leciona {disciplina.nome}.")

    def listar_disciplinas(self):
        print(f"\nProfessor: {self.nome}")
        if not self.disciplinas_lecionadas:
            print("Nenhuma disciplina atribuída.")
        else:
            for d in self.disciplinas_lecionadas:
                print(f"- {d.nome}")

d1 = Disciplina("Matemática")
d2 = Disciplina("Física")
d3 = Disciplina("Programação")

prof = Professor("Carlos")
prof.lecionar_disciplina(d1)
prof.lecionar_disciplina(d2)
prof.lecionar_disciplina(d1)

prof.listar_disciplinas()