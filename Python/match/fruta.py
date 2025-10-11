fruta = input("Digite o nome de uma fruta: ").strip().lower()

match fruta:
    case "maçã":
        print("Fruta vermelha e doce.")
    case "banana":
        print("Fruta amarela e rica em potássio.")
    case "laranja":
        print("Fruta cítrica, ótima para suco!.")
    case _:
        print("Fruta desconhecida.")