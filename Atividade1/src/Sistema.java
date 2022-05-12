//Guilherme Lins Banzato RA: 20.01561-5

public class Sistema {

    public static void executar(){

        User user_1 = new User("Midoriya");
        User user_2 = new User("Todoroki");
        User user_3 = new User("All Might");
        User user_4 = new User("Bakugo");

        Carro c_1 = new Carro(3000, "Porsche");
        Moto m_1 = new Moto(1500, "Harley");
        Bicicleta b_1 = new Bicicleta(500, "Caloi");
        Patinete p_1 = new Patinete(500, "AlgumaMarca");

        System.out.println("ALUGUEL BICICLETA");
        user_1.aluga(b_1);
        System.out.println(b_1);
        System.out.println(user_1);

        System.out.println("ALUGUEL PATINETE");
        user_2.aluga(p_1);
        System.out.println(p_1);
        System.out.println(user_2);

        System.out.println("ALUGUEL CARRO");
        user_3.aluga(c_1);
        System.out.println(c_1);
        System.out.println(user_3);

        System.out.println("ALUGUEL MOTO");
        user_4.aluga(m_1);
        System.out.println(m_1);
        System.out.println(user_4);
    }

}