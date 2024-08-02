public class Pessoa {
  // Atributos
  String nome;
  int idade;
  
  // Construtor:
  Pessoa(String nome, int idade){
    this.nome = nome;
    this.idade = idade;
  }

  // Construtor:
  // Pessoa(String nome){
  //   this.nome = nome;
  //   this.idade = ;
  // }

  // Construtor:
  Pessoa( int idade){
    this.nome = "Não informado";
    this.idade = idade;
  }

  void falar(String frase){
    System.out.println(frase + " Eu sou " + this.nome);
  }

  public static void main(String[] args) {
    System.out.println("Iniciando o programa...");
    Pessoa p1 = new Pessoa("Jônatas",19);
    p1.falar("Olá!");
    Pessoa p2 = new Pessoa("Thallys",19);
    p2.falar("Oie!");
  
  }
  
}