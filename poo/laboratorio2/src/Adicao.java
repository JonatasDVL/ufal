public class Adicao extends Operacao {

  @Override
  public void calcular(float num1, float num2){
    float num3 = num1 + num2; 
    System.out.printf("%f + %f = %f", num1, num2, num3);
  };

}
