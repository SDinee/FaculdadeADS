package Java.heranca;

//Classe base Pessoa 
public class Pessoa {
    // Atributos privados (encapsulamento)
    private String nome;
    private int idade;

    // Construtor vazio (permite criar objeto sem inicializar atributos)
    public Pessoa(){}

    // Construtor com parâmetros (permite criar objeto já com nome e idade)
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Métodos getters e setters (acesso controlado aos atributos privados)
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    // Sobrescrevendo toString para mostrar informações da pessoa
    @Override
    public String toString() {
        return "nome=" + nome + "\nidade=" + idade;
    }
}

// Classe Aluno herda de Pessoa
class Aluno extends Pessoa {
    private int matricula;

    //Construtor chama o super (Pessoa) e adiciona matrícula
    public Aluno(String nome, int idade, int matricula) {
        super(nome, idade);
        this.matricula = matricula;
    }

    public int getMatricula() {
        return matricula;
    }

    // Sobrescreve toString para incluir matrícula
    @Override
    public String toString() {
        return super.toString() + "\nmatricula=" + matricula;
    }
}

// Classe Professor herda de Pessoa
class Professor extends Pessoa {
    private String disciplina;

    // Construtor chama o super (Pessoa) e adiciona disciplina
    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    public String getDisciplina() {
        return disciplina;
    }

    // Sobrescreve toString para incluir disciplina
    @Override
    public String toString() {
        return super.toString() + "\ndisciplina=" + disciplina;
    }
}
