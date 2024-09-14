public interface IMotor {

	public void ligar();

	public void desligar();

	public boolean isLigado();
	
	public float getAceleracao();
	
	public abstract void acelerar(Carro c, float quantCombustivel);
	
}
