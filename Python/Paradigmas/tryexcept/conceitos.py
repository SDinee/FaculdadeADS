try:
    nota = float(input("Digite a nota do aluno(0-10): "))
    
    if nota <= 0 or nota <= 10:
        if nota >= 9:
            conceito = 'A'
        elif nota >= 7:
            conceito = 'B'
        elif nota >= 5:
            conceito = 'C'
        else:
            conceito = 'D'
        print(f"A nota do aluno é {nota} e o conceito é: {conceito}")
    else:
        print("Erro: A nota deve estar entre 0 e 10.")
        
except ValueError:
    print("Erro: insira apenas valores numéricos válidos.")