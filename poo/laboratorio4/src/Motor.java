public abstract class Motor {

	private boolean ligado;
	private float aceleracao;

	public Motor() {
		this.ligado = false;
		this.aceleracao = 0;		
	}

	public void ligar() {
		this.ligado = true;
	}

	public void desligar() {
		this.ligado = false;
	}

	public boolean isLigado() {
		return ligado;
	}
	
	protected void setAceleracao(float aceleracao) {
		this.aceleracao = aceleracao;
	}

	public float getAceleracao() {
		return this.aceleracao;
	}
	
	public abstract void acelerar(Carro c, float quantCombustivel);
	
}
