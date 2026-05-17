from collections import defaultdict

estudantes_por_sala = defaultdict(list)

estudantes_por_sala['B'].append('Raphael')
estudantes_por_sala['A'].append('Cleber')
estudantes_por_sala['A'].append('Joares')

print(dict(estudantes_por_sala))