dia = input("Digite o dia da semana (ex: segunda): ").strip().lower()

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Hoje é um dia útil.")
    case "sábado" | "domingo":
        print("Hoje é um final de semana.")
    case _:
        print("Dia inválido. Por favor, insira um dia válido da semana.")