package Java.modacessos;

public class exemplo {
    public static void main(String[] args) {
        minhaclasse obj = new minhaclasse();

        // Atributos acessíveis
        System.out.println("Atributo default: " + obj.defaultAtributo);
        System.out.println("Atributo protegido: " + obj.protectedAtributo);
        System.out.println("Atributo público: " + obj.publicAtributo);

        // ERRO se tentar acessar diretamente o private:
        // System.out.println("Atributo privado: " + obj.privateAtributo);

        // Correto: acessar via getter
        System.out.println("Atributo privado via getter: " + obj.getPrivateAtributo());

        // Métodos acessíveis
        obj.defaultMetodo();
        obj.protectedMetodo();
        obj.publicMetodo();

        // ERRO se tentar chamar diretamente o private:
        // obj.privateMetodo();

        // Correto: chamar via método público que acessa o private
        obj.chamarPrivateMetodo();
    }    
}
