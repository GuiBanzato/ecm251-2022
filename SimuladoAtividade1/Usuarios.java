//Guilherme Lins Banzato RA:20.01561-5

package SimuladoAtividade1;

public class Usuarios {
    
    private String nome;
    private String senha;
    private String email;

    public Usuarios(String nome, String senha, String email){
        this.nome = nome;
        this.nome = nome;
        this.email = email;
        
    }

    public void visualizarUsuarios(){
        System.out.println("Dados do Cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("Senha:" + senha);
        System.out.println("E-mail:" + email);
        
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getSenha(){
        return senha;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }

    public String getEmail(){
        return email;
    }
   
    public void setEmail(String email){
        this.email = email;
    }
}
