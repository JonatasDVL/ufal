package pacote2;
import pacote1.Carta;
import pacote1.Documento;

public class Telegrama extends Documento {
  private String assinatura;  
  
  public Telegrama(String nome, String data, String assinatura) {
    super(data);
    this.assinatura = assinatura;
  };

  public void mostrar() {
    super.mostrar();
    System.out.printf("Assinatura: %s \n", this.assinatura);
  };

  public void mostrar2() {
    Carta carta = new Carta("energia", "05/08", "375asde541");
    System.out.println(carta.getData());
    Telegrama telegrama = new Telegrama("telecena", "15/02", "joazin");
    System.out.println(telegrama.getData());
  };
};
