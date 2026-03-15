nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    conceito = 'A'
elif nota >= 7:
    conceito = 'B'
elif nota >= 5:
    conceito = 'C'
else:
    conceito = 'D'
    
print(f"A nota do aluno é {nota} e o conceito é: {conceito}")