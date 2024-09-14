public class MotorFlex extends Motor {

	public void acelerar(Carro c, float quantCombustivel) {
		super.setAceleracao(quantCombustivel * 500);
		c.setVelocidade(super.getAceleracao() / 50);
		System.out.println("Motor acelerou em " + super.getAceleracao() + ", e a velocidade atual é " + c.getVelocidade());
	}

}
