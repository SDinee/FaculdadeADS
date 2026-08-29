package Java.sla;

public class minhaclasse {
    int defaultAtributo = 1; 
    protected int protectedAtributo = 2; 
    public int publicAtributo = 3; 
    private int privateAtributo = 4; // só acessível dentro da classe

    void defaultMetodo() {
        System.out.println("Método com acesso padrão (default)");
    }

    protected void protectedMetodo() {
        System.out.println("Método protegido");
    }

    public void publicMetodo() {
        System.out.println("Método público");
    }

    private void privateMetodo() {
        System.out.println("Método privado");
    }

    // Getter para acessar o atributo privado de fora
    public int getPrivateAtributo() {
        return privateAtributo;
    }

    // Método público que chama o método privado
    public void chamarPrivateMetodo() {
        privateMetodo();
    }
}
