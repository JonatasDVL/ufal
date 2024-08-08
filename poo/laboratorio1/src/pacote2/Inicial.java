package pacote2;
import pacote1.Carta;
import pacote1.Documento;

public class Inicial {
  public static void main(String[] args) {
    Carta carta = new Carta("jonatas", "17/11/2004", "2");
    carta.mostrar();
    Documento documento = new Documento("jonatasdvl", "17/11");
    documento.mostrar();
    Telegrama telegrama = new Telegrama("telecenaasas", "13/02", "feijan");
    telegrama.mostrar2();
  };
}

// 10. Na classe Telegrama, crie o método “mostrar2()”, que instancia dois objetos: um do
// tipo Carta e outro do tipo Telegrama; em seguida, imprima o valor do atributo data de
// ambos os objetos. O que aconteceu? Como você poderia corrigir o problema? Justifique
// através de um comentário no código.

// Resposta: O código funcionará corretamente apenas na instância do telegrama, porém na instância da carta dará erro ao tentar acessar o atributo data, pois os atributos imprimidos são atributos protegidos, logo não há problemas ao acessar se for filho o da classe documento e se for filho do "arquivo". Porém para uma melhor proteção dos dados é preferivel utilizar o metodo get para receber os atributos.

// 12. Na classe Inicial, crie o método “main()”, que instancie um objeto do tipo Carta e
// imprima na tela os valores dos atributos do objeto. O que aconteceu? Como você poderia
// corrigir o problema? Justifique através de um comentário no código.

// Resposta: Como a classe Inicial está no pacote pacote2 e a classe Carta está no pacote pacote1, há uma questão relacionada à visibilidade dos atributos. Desta forma, o atributo anexo na classe Carta possui visibilidade de pacote, o que significa que ele não será acessível diretamente no pacote pacote2. No entanto, como estamos utilizando o método mostrar(), que é público, o código ainda funciona corretamente, e todos os atributos da carta são impressos. Portanto, o código não precisa de correção.