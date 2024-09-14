public class Tanque {

	private float capacidade;
	private float quantidadePresente;

	public Tanque(float capacidade) {
		this.capacidade = capacidade;
		this.quantidadePresente = 0;
	}

	public void abastecer(float quantidade) {
		if (quantidade <= (this.capacidade - this.quantidadePresente)) {
			this.quantidadePresente = this.quantidadePresente + quantidade;
			System.out.println("Tanque foi abastecido.");
		} else {
			this.quantidadePresente = this.capacidade;
			System.out.println("Tanque foi abastecido, porém parte do combustível transbordou.");			
		}
	}

	public float getQuantidadePresente() {
		return this.quantidadePresente;
	}

	public float usarCombustivel(float quantidade) {
		if (this.quantidadePresente > quantidade) {
			this.quantidadePresente -= quantidade;
			System.out.println("Foi gasto " + quantidade + " de combustível.");
		} else {
			quantidade = this.quantidadePresente;
			this.quantidadePresente = 0;
			System.out.println("Foi gasto todo o combustível do tanque.");
		}
		return quantidade;
	}

}
