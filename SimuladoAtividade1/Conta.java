//Guilherme Lins Banzato RA:20.01561-5

package SimuladoAtividade1;

public class Conta {
    
    private int idConta;
    private double saldo;
    private Usuarios usuario;

    public Conta(Usuarios usuario, int idConta){
        this.idConta = idConta;
        this.usuario = usuario;
        saldo = 0;
    }

    public String visualizarSaldo(){
        return  String.format("R$ %.2f", saldo);
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Conta Numero:" + idConta + 
        "\n Saldo:" + visualizarSaldo() + 
        "\n Usuario:" + usuario.getNome();
    }

}
