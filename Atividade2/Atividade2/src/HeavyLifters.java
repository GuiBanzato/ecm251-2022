public class HeavyLifters extends Membro{

    public HeavyLifters(String nome, String email, boolean horaExtra) {
        super(nome, email, FuncoesEnum.HEAVYLIFTERS, horaExtra);
    }

    @Override
    public void mostrarMensagem(Membro membro) {
        System.out.println(membro.getNome()+" (" +membro.getFuncao()+ ") "+ ":");
        if(membro.getHoraExtra())
        {
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
        else
        {
            System.out.println("Podem contar conosco!");
        }
    }
    
}