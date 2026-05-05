class Aluno:
    def __init__(self: object, nome: str, idade: int, notas: int) -> None:
        self.nome = nome
        self.idade = idade
        self.notas = notas
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
# sum(lista) → soma todos os números da lista
# len(lista) → conta quantos números tem na lista

if __name__ == "__main__":
    aluno1 = Aluno("João", 20, [7.5, 8.0, 6.5])
    aluno2 = Aluno("Maria", 22, [9.0, 8.5, 7.0])
    lista_alunos = [aluno1, aluno2]
    for aluno in lista_alunos:
        print(f"Aluno: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")