public class MotorFlex implements IMotor {

	private boolean ligado;
	private float aceleracao;

	public MotorFlex() {
		this.ligado = false;
		this.aceleracao = 0;		
	}

	@Override
	public void ligar() {
		this.ligado = true;
	}

	@Override
	public void desligar() {
		this.ligado = false;
	}

	@Override
	public boolean isLigado() {
		return ligado;
	}
	
	protected void setAceleracao(float aceleracao) {
		this.aceleracao = aceleracao;
	}

	@Override
	public float getAceleracao() {
		return this.aceleracao;
	}

	@Override
	public void acelerar(Carro c, float quantCombustivel) {
		this.setAceleracao(quantCombustivel * 500);
		c.setVelocidade(this.getAceleracao() / 50);
		System.out.println("Motor acelerou em " + this.getAceleracao() + ", e a velocidade atual é " + c.getVelocidade());
	}

}
