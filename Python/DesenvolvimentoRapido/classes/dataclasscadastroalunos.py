from dataclasses import dataclass
@dataclass

class Aluno:
    nome: str
    idade: int
    notas: list[float]
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
if __name__ == "__main__":
    aluno1 = Aluno("Luiz", 22, [7.0, 5.5, 8.5])
    aluno2 = Aluno("Marcio", 33, [1.0, 7.5, 2.0])
    lista_alunos = [aluno1, aluno2]
    for aluno in lista_alunos:
        print(f"Aluno: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")