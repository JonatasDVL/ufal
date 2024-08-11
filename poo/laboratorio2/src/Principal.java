import java.util.Scanner;

public class Principal {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String entrada = "";
    Operacao operacao = null;

    while (!entrada.equals("0")) {
      System.out.println(
          "\n\nDigite A para realizar a adição;\r\n" +
          "Digite S para realizar a subtração;\r\n" +
          "Digite M para realizar a multiplicação;\r\n" +
          "Digite D para realizar a divisão;\r\n" +
          "Digite 0 (zero) para SAIR;");

      entrada = scanner.nextLine().toLowerCase();

      if (entrada.equals("a")) {
        operacao = new Adicao();
      } else if (entrada.equals("s")) {
        operacao = new Subtracao();
      } else if (entrada.equals("m")) {
        operacao = new Multiplicacao();
      } else if (entrada.equals("d")) {
        operacao = new Divisao();
      }
      
      if (operacao != null) {
        System.out.println("Digite o primeiro número:");
        float numero1 = scanner.nextFloat();
        System.out.println("Digite o segundo número:");
        float numero2 = scanner.nextFloat();
        operacao.calcular(numero1, numero2);
        scanner.nextLine();
        operacao = null;
      }
    }

    scanner.close();
  }
}
