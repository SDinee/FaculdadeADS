// Pacote onde a classe está localizada
package Java.arraylista;
import java.util.*; // Importa todas as classes utilitárias (List, ArrayList, Set, HashSet, Queue, LinkedList, Deque, ArrayDeque)

public class colecoes {
    public static void main(String[] args) {
        // 1. Criando uma lista (ArrayList) que mantém a ordem de inserção e permite elementos repetidos
        List<String> lista = new ArrayList<>();
        lista.add("Banana");
        lista.add("Maçã");
        lista.add("Laranja");
        System.out.println("Lista de frutas: " + lista);

        // Percorrendo a lista com for-each
        for (String fruta : lista) {
            System.out.println("Fruta: " + fruta);
        }

        // 2. Criando um conjunto (HashSet) que não mantém ordem e não permite elementos repetidos
        Set<String> conjunto = new HashSet<>();
        conjunto.add("Banana");
        conjunto.add("Maçã");
        conjunto.add("Laranja");
        System.out.println("Conjunto de frutas: " + conjunto);

        // 3. Uso de Queue (LinkedList) → fila (FIFO: First In, First Out)
        Queue<String> fila = new LinkedList<>();
        fila.offer("Primeiro");
        fila.offer("Segundo");
        fila.offer("Terceiro");
        System.out.println("Fila inicial: " + fila);

        // Remove o elemento que está no início da fila
        String removidoFila = fila.poll();
        System.out.println("Elemento removido da fila: " + removidoFila);
        System.out.println("Fila após remoção: " + fila);

        // 4. Uso de Deque (ArrayDeque) → permite inserções e remoções nos dois extremos
        Deque<String> deque = new ArrayDeque<>();
        
        // Adiciona no final
        deque.offer("Fim");

        // Adiciona no início
        deque.push("Inicio");
        System.out.println("Deque inicial: " + deque);

        // Remove do início
        String removidoDequeInicio = deque.pop();
        System.out.println("Elemento removido do início do deque: " + removidoDequeInicio);
        System.out.println("Deque após remoção do início: " + deque);
    }
}
