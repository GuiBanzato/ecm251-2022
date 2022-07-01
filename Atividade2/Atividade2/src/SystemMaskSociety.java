import java.util.ArrayList;
import java.util.List;

public class SystemMaskSociety {
    public static void run(){

        List<Membro> membros = new ArrayList<Membro>();

        membros.add(new MobileMembers("Luffy", "monkey.d.luffy@gmail.com", false) );

        membros.add(new HeavyLifters("Zoro", "roronoa.zoro@gmail.com", false) );

        membros.add(new ScriptGuys("Sanji", "vinsmoke.sanji@gmail.com", false) );

        membros.add(new BigBrothers("Usopp", "god.usopp@gmail.com", false) );

        mostrarMensagens(membros);

        trocarHorario(membros);

        mostrarMensagens(membros);

        trocarHorario(membros);

        removeMembro(membros, FuncoesEnum.HEAVYLIFTERS);
        
        removeMembro(membros, FuncoesEnum.SCRIPTGUYS);

        mostraMembros(membros);

        mostrarMensagens(membros);

        System.out.println("Sistema Encerrado");
    }

    public static void mostraMembros(List<Membro> membros){
        System.out.println("Membros cadastrados:");
        for(Membro membro : membros){
            System.out.println(membro);
        }
    }

    public static void trocarHorario(List<Membro> membros){
        System.out.println("Trocando horário");
        for (Membro membro : membros){
            membro.setHoraExtra(membro.getHoraExtra());
        }
    }

    public static void mostrarMensagens(List<Membro> membros){
        System.out.println("Mensagens:");
        for (Membro membro : membros){
            membro.mostrarMensagem(membro);
        }
    }

    public static void removeMembro(List<Membro> membros, FuncoesEnum funcao){
        for (Membro membro : membros){
            if(membro.getFuncao() == funcao){
                membros.remove(membro);
                break;
            }
        }
    }
}