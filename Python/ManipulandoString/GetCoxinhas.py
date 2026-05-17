import time  # importa a biblioteca time para usar pausas (simular tempo de preparo)

# Função que usa RETURN (retorna tudo de uma vez)
def get_coxinhas(*pedidos):
    # mensagem inicial
    print("--- [Return] Preparando TODA a fornada de coxinhas de uma vez...")

    # simula tempo de preparo
    time.sleep(1)

    # return: devolve uma LISTA completa de uma vez só
    return [f"{pedido} coxinhas" for pedido in pedidos]


# Função que usa YIELD (gera um item por vez)
def get_joelho(*pedidos):
    # percorre cada pedido separadamente
    for pedido in pedidos:
        # mostra que está saindo um item por vez
        print(f"--- [Yield] Saindo um pedido de {pedido} joelho(s) agora!")

        # simula tempo de preparo individual
        time.sleep(1)

        # yield: devolve um item por vez (gerador)
        yield f"{pedido} joelho(s)"


# só executa isso se o arquivo for rodado diretamente
if __name__ == "__main__":

    # TESTE DA FUNÇÃO COM RETURN
    print("SOLICITANDO COXINHAS {return}: ")

    # chama a função e recebe a lista completa de uma vez
    salgados_return = get_coxinhas(4, 6, 8)

    # imprime tudo de uma vez
    print("Recebi a lista completa: ", salgados_return)


    # separador visual
    print("\n" + "="*30 + "\n")


    # TESTE DA FUNÇÃO COM YIELD
    print("SOLICITANDO JOELHOS {Yield}: ")

    # chama a função geradora (não executa tudo ainda)
    pedidos_joelho = get_joelho(4, 6, 8)

    # percorre os itens um por um
    for salgado in pedidos_joelho:
        # recebe cada item individualmente conforme é gerado
        print(f"Cliente recebeu: {salgado}")