public class ScriptGuys extends Membro{

    public ScriptGuys(String nome, String email, boolean horaExtra) {
        super(nome, email, FuncoesEnum.SCRIPTGUYS, horaExtra);
    }

    @Override
    public void mostrarMensagem(Membro membro) {
        System.out.println(membro.getNome()+" (" +membro.getFuncao()+ ") "+ ":");
        if(membro.getHoraExtra())
        {
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        }
        else
        {
            System.out.println("Prazer em ajudar novos amigos de código!");
        }  
    }
}