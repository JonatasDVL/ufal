import java.util.ArrayList;

public class Agenda {
  ArrayList<Pessoa> lista = new ArrayList<>();

  public void inserirPessoa(Pessoa pessoa) {
    if (this.lista.size() == 0) {
      this.lista.add(pessoa);
    } else {
      for (Pessoa p : lista) {
        if (p.getEmail().equals(pessoa.getEmail())) {
          removerPessoa(p);
          break;
        }
      }
      this.lista.add(pessoa);
      ;
    }
  };

  public void removerPessoa(Pessoa pessoa) {
    this.lista.remove(pessoa);
  }

  public void imprimirPessoas() {
    System.out.println("");
    for (Pessoa elemento : this.lista) {
      System.out.println(elemento);
    }
  }
}
