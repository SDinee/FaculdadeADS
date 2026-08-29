package Java.mtdestatico;

public class Prova {
    // Método estático que soma duas notas de simulado
    static float Simulado(float s1, float s2){
        return s1 + s2;
    }

    // Método estático que calcula a nota total (simulado + avaliação)
    static float NotaTotal(float s, float a){
        return s + a;
    }

    // Método estático que calcula a nota final (nota fixa de avs + simulado)
    static float NotaFinal(float s){
        float avs = 6.3f; // valor fixo da avaliação substitutiva
        return avs + s;
    }

    public static void main(String[] args){
        // Calcula a nota do simulado
        float simulado = Simulado(0.2f, 0.6f);

        // Nota da avaliação principal
        float av = 4.5f;

        String condicao; // variável para guardar se foi aprovado ou reprovado

        // Calcula a nota total (simulado + avaliação)
        int notaTotal = (int) NotaTotal(simulado, av);

        // Verifica se a nota total é suficiente para aprovação
        if (notaTotal > 6) {
            condicao = "Aprovado";
        } else {
            // Caso contrário, calcula a nota final com a avaliação substitutiva
            float notaFinal = NotaFinal(simulado);
            if (notaFinal > 6) {
                condicao = "Aprovado";
            } else {
                condicao = "Reprovado";
            }
        }

        // Exibe o resultado final
        System.out.println("Condição: " + condicao);
    }
}
