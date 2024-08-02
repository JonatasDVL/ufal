package pacote2;
import pacote1.Carta;
import pacote1.Documento;

public class Inicial {
  public static void main(String[] args) throws Exception {
    System.out.println("Hello, World!");
    Carta carta = new Carta("jonatas", "17/11/2004", "2");
    carta.mostrar();
    Documento documento = new Documento("jonatasdvl", "17/11");
    documento.mostrar();
  };
}
