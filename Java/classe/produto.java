// Pacote onde a classe está localizada
package Java.classe;

public class produto {
    // 1. Atributos privados da classe (encapsulamento)
    private String nome;              // nome do produto
    private double preco;             // preço unitário do produto
    private int quantidadeEstoque;    // quantidade disponível em estoque

    // 2. Construtor da classe: inicializa os atributos quando criamos um novo produto
    public produto(String nome, double preco, int quantidadeEstoque) {
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEstoque = quantidadeEstoque;
    }

    // 3. Método para adicionar unidades ao estoque
    public void adicionarEstoque(int quantidade) {
        this.quantidadeEstoque += quantidade;
    }

    // 4. Método para vender unidades (reduz o estoque)
    public void vender(int quantidade){
        this.quantidadeEstoque -= quantidade;
    }

    // 5. Método para calcular o valor total do estoque
    // Multiplica o preço unitário pela quantidade disponível
    public double calcularValorTotalEstoque() {
        return this.preco * this.quantidadeEstoque;
    }
}
