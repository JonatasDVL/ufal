package pacote1;

public class Carta extends Documento {
  String anexo;

  public Carta(String nome, String data, String anexo) {
    super(nome, data);
    this.anexo = anexo;
  };

  public void mostrar() {
    super.mostrar();
    System.out.printf("Anexo: %s \n", this.anexo);
  };
}
