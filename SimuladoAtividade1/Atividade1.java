package SimuladoAtividade1;

public class Atividade1 {
    public void run(){
        Usuarios usuario = new Usuarios("Midoria", "123456", "allmight_wannbe@gmail.com");
        Conta conta = new Conta(usuario, 1234);
        System.out.println(conta);
    }
}
