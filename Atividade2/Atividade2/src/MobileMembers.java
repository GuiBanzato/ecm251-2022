public class MobileMembers extends Membro{

    public MobileMembers(String nome, String email, boolean horaExtra) {
        super(nome, email, FuncoesEnum.MOBILEMEMBERS, horaExtra);
    }

    @Override
    public void mostrarMensagem(Membro Membro) {
        System.out.println(Membro.getNome()+" (" +Membro.getFuncao()+ ") "+ ":");
        if(Membro.getHoraExtra())
        {
            System.out.println("Happy_C0d1ng. Maskers");
        }
        else
        {
            System.out.println("Happy Coding!");
        }
    }

}