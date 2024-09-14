public class PrincipalCarro {
    public static void main(String[] args) throws Exception {
        Motor motor1 = new MotorDiesel();
        Motor motor2 = new MotorFlex();
        Carro carro1 = new Carro("gol", "preto", motor1);
        Carro carro2 = new Carro("ford ka", "cinza", motor2);
        
        System.out.println("\n\n--Carro 1:");
        carro1.acelerar(0);
        carro1.abastecer(12);
        carro1.ligar();
        carro1.acelerar(10);

        System.out.println("\n--Carro 2:");
        carro2.acelerar(0);
        carro2.abastecer(12);
        carro2.ligar();
        carro2.acelerar(10);

    }
}

// O que acontece se acelerar-mos um carro sem combustível?
// Caso o carro esteja desligado, ele nem tentará acelerar, porém caso esteja ligado, ele tentará acelerar, porém a aceleração não terá combustivel e irár desligar.

// Qual a velocidade de um carro com motor flex, se acelerarmos com 10 unidades de combustível? E se o motor for a diesel?
// No motor disel 68
// No motor flex 100


