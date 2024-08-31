public class Principal {
  public static void main(String[] args) {
    Agenda agenda = new Agenda();

    Pessoa p1 = new Pessoa("Jônatas Leite", "82 994261785", "jonatas.leite@arapiraca.ufal.br", "12345");
    Pessoa p2 = new Pessoa("Thallys de Alcantara", "82 99.......", "thallys.alcantara@arapiraca.ufal.br", "1235");
    Pessoa p3 = new Pessoa("Anderson Passos", "82 99.......", "anderson.passos@arapiraca.ufal.br", "12345");
    Pessoa p4 = new Pessoa("Francisco Colatino", "82 99.......", "francisco.colatino@arapiraca.ufal.br", "12345");

    //quando tem duas Pessoas tem o mesmo email, o ultimo colocado é o que permanence
    Pessoa p5 = new Pessoa("Rayanuarte", "", "rayane.duarte@arapiraca.ufal.br", "12345"); 
    Pessoa p6 = new Pessoa("Rayane Duarte", "82 99.......", "rayane.duarte@arapiraca.ufal.br", "12345");
  
    agenda.inserirPessoa(p1);
    agenda.inserirPessoa(p2);
    agenda.inserirPessoa(p3);
    agenda.inserirPessoa(p4);
    agenda.inserirPessoa(p5);
    agenda.inserirPessoa(p6);
    
    agenda.imprimirPessoas();

    agenda.removerPessoa(p2);

    agenda.imprimirPessoas();
  }

}
