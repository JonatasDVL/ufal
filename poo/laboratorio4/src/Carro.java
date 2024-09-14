public class Carro {
	private String modelo;
	private String cor;
	private float velocidade;
	private Tanque tanque;
	private Motor motor;

	public Carro(String modelo, String cor, Motor motor) {
		this.modelo = modelo;
		this.cor = cor;
		this.motor = motor;
		this.tanque = new Tanque(45);
	}

	public Carro(String modelo, String cor, Motor motor, Tanque tanque) {
		this.modelo = modelo;
		this.cor = cor;
		this.motor = motor;
		this.tanque = tanque;
	}

	public void ligar() {
		if (!motor.isLigado()) {
			motor.ligar();
			System.out.println("Carro ligou.");
	} else {
			System.out.println("O carro está ligado.");
	}
	}

	public void desligar() {
		if (motor.isLigado()) {
			if (this.velocidade > 0) {
				this.freiar();
			}
			this.motor.desligar();
			System.out.println("Carro desligou.");			
		} else {
			System.out.println("O carro está desligado.");			
		}

	}

	public void acelerar(float quantCombustivel) {
		if (this.motor.isLigado()) {
			if (this.tanque.getQuantidadePresente() > 0) {	
				if (quantCombustivel > 0) {
					this.motor.acelerar(this, this.tanque.usarCombustivel(quantCombustivel));
					if (this.tanque.getQuantidadePresente() == 0) {
						System.out.println("Porém acabou o combustível.");
						this.desligar();
					} 
				} else {
					System.out.println("Você não acelerou o carro!");
				}
			} else {
				System.out.println("O tanque está com combustível insuficiente para acelerar!");
				this.desligar();
			}
		} else {
			System.out.println("O carro está desligado, não é possível acelerar!");
		}
	}

	public void freiar() {
		if(this.velocidade > 0){
			this.velocidade = 0;
			System.out.println("O carro freou.");
		} else { 
			System.out.println("O carro já está parado.");
		};
	}

	protected void setVelocidade(float velocidade) {
		this.velocidade = velocidade;
	}

	public float getVelocidade() {
		return this.velocidade;
	}

	public String getModelo(){
		return this.modelo;
	}

	public String getCor(){
		return this.cor;
	}

	public void abastecer(float quantidade) {
		this.tanque.abastecer(quantidade);
	}

}
