package Java.objetos;

public class Main {
    public static void main(String[] args) {
        // Cria um objeto Aluno com nome e idade
        Aluno aluno1 = new Aluno("João", 20);

        // Usa métodos da classe Aluno para obter informações
        String nomeAluno = aluno1.obterNome();   // retorna o nome
        int idadeAluno = aluno1.obterIdade();   // retorna a idade
        double codigoAluno = aluno1.obterCodigo(); // retorna o código (provavelmente gerado internamente)

        // Exibe os dados do aluno no console
        System.out.println("Nome do aluno: " + nomeAluno);
        System.out.println("Idade do aluno: " + idadeAluno);
        System.out.println("Código do aluno: " + codigoAluno);
    }
}
