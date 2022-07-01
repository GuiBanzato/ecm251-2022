public class BigBrothers extends Membro{

    public BigBrothers(String nome, String email, boolean horaExtra) {
        super(nome, email, FuncoesEnum.BIGBROTHERS, horaExtra);
    }

    @Override
    public void mostrarMensagem(Membro membro) {
        System.out.println(membro.getNome()+" (" +membro.getFuncao()+ ") "+ ":");
        if(membro.getHoraExtra())
        {
            System.out.println("...");
        }
        
        else
        {
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        } 
    }
}