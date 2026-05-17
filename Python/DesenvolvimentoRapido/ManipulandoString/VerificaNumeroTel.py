import re

def verificar_regex(texto: str) -> None:
    padrao = r'\(\d{3}\) \d{3}-\d{4}'
    # Padrão para encontrar números de telefone no formato (XX) XXXXX-XXXX
    resultado = re.search(padrao, texto)
    if resultado:
        numero_telefone = resultado.group()
        print("Número de telefone encontrado: ", numero_telefone)
    else:
        print("Número de telefone não encontrado. ")

if __name__ == "__main__":
    verificar_regex("O número de telefone do Sidne é (123) 456-7080.")