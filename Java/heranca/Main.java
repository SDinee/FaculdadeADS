package Java.heranca;

public class Main {
    // public static void main(String[] args){
    //     Pessoa pessoa1 = new Pessoa("João", 30);
    //     System.out.println(pessoa1.toString());

    //     Pessoa pessoa2 = new Pessoa();

    //     pessoa2.setNome("Maria");
    //     pessoa2.setIdade(25);

    //     System.out.println("Nome: " + pessoa2.getNome());
    //     System.out.println("Idade: " + pessoa2.getIdade());
    // }

   public static void main(String[] args) {
        // Criando um aluno com nome, idade e matrícula
        Aluno aluno1 = new Aluno("Carlos", 20, 12345);
        System.out.println(aluno1.toString());

        // Criando um professor com nome, idade e disciplina
        Professor professor1 = new Professor("Dr. Silva", 45, "Matemática");
        System.out.println(professor1.toString());
    }
}
