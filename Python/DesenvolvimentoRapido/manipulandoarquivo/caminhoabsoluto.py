import os

def obter_caminho_absoluto(nome_arquivo: str) -> str:
    """Retorna o caminho absoluto do arquivo com base na localização deste script"""
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(diretorio_base, nome_arquivo)

def escrever_arquivo(caminho: str, conteudo: str) -> None:
    """Cria ou sobrescreve um arquivo com o conteúdo fornecido (Modo 'w')."""
    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"[Sucesso] Arquivo escrito em: {caminho} ")
    except Exception as e:
        print(f"[Erro] Falha ao escrever no arquivo: {e}")

def adicionar_texto(caminho: str, conteudo: str) -> None:
    """Adiciona conteúdo ao final de um arquivo existente (Modo 'a')"""
    try:
        with open(caminho, 'a', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"[Sucesso] Texto adicionado ao arquivo. ")
    except Exception as e:
        print(f"[Erro] Falha ao adicionar texto: {e} ")

def ler_arquivo(caminho: str) -> None:
    """Lê e retorna todo o conteúdo de um arquivo (Modo 'r'). """
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("\n--- Conteúdo do Arquivo ---")
            print(conteudo)
            print("-----------------------------") 
            return
    except FileNotFoundError:
        print(f"[Erro] Arquivo não encontrado para leitura {caminho}")
    except Exception as e:
        print(f"[Erro] Falha ao ler o arquivo: {e}")

def apagar_arquivo(caminho: str) -> None:
    """Remove o arquivo do sistema operacional. """
    try:
        if os.path.exists(caminho):
            os.remove(caminho)
            print(f"[Sucesso] Arquivo apagado: {caminho}")
        else:
            print(f"[Erro] O arquivo '{caminho}' não existe")
    except Exception as e:
        print(f"[Erro] Falha ao apagar o arquivo {e}")

if __name__ == "__main__":
    caminho_meu_arquivo = obter_caminho_absoluto('exemplo_aula.txt')
    escrever_arquivo(caminho_meu_arquivo, "Nossa aula!\n")
    ler_arquivo(caminho_meu_arquivo)
    adicionar_texto(caminho_meu_arquivo, "De Python, explorando manipulação de arquivos. ")
    ler_arquivo(caminho_meu_arquivo)
    apagar_arquivo(caminho_meu_arquivo)
    ler_arquivo(caminho_meu_arquivo)     