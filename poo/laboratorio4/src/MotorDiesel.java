public class MotorDiesel extends Motor {

	public void acelerar(Carro c, float quantCombustivel) {
		super.setAceleracao(quantCombustivel * 750);
		c.setVelocidade(super.getAceleracao() / 110);
		System.out.println("Motor acelerou em " + super.getAceleracao() + ", e a velocidade atual é " + c.getVelocidade());
	}

}
