package Java.objetos;

// Classe Aluno com atributos privados
public class Aluno {
    private String nome;
    private int idade;
    private double codigo;

    // Construtor que recebe nome e idade
    public Aluno(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        // Gera um código aleatório para o aluno
        this.codigo = Math.random() * 10000;
    }

    // Métodos getters (obter informações)
    public String obterNome() {
        return nome;
    }

    public int obterIdade() {
        return idade;
    }

    public double obterCodigo() {
        return codigo;
    }
}
