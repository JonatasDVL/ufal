package pacote1;

public class Documento {
  String nome;
  protected String data;

  public Documento(String nome, String data) {
    this.nome = nome;
    this.data = data;
  };

  public Documento(String data) {
    this.nome = "Documento Qualquer";
    this.data = data;
  };

  public void mostrar() {
    System.out.printf("Nome: %s \nData: %s \n", this.nome, this.data);
  };

}
