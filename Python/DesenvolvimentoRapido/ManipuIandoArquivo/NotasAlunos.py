def criar_registro_notas(arquivo):
    with open(arquivo, 'w') as file:
        file.write("Registro de Notas dos Alunos\n")
        file.write("----------------------------\n")
        
def adicionar_nota(arquivo, nome_aluno, nota):
    with open(arquivo, 'a') as file:
        file.write(f"Aluno: {nome_aluno}\n") 
        file.write(f"Nota: {nota}\n")
        file.write("----------------------------\n")
        
if __name__ == "__main__":
    registro_notas = "registro_notas.txt"
    criar_registro_notas(registro_notas)
    adicionar_nota(registro_notas, "Alice", 8.5)
    adicionar_nota(registro_notas, "Bob", 9.2)
    