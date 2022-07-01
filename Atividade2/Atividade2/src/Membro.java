public abstract class Membro implements PostarMensagem{
    private final String nome;
    private final String email;
    private final FuncoesEnum funcao;
    private boolean horaExtra;
    public Membro(String nome, String email, FuncoesEnum funcao, boolean horaExtra) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
        this.horaExtra = horaExtra;
    }
    public String getNome() {
        return nome;
    }
    public String getEmail() {
        return email;
    }
    public FuncoesEnum getFuncao() {
        return funcao;
    }
    public boolean getHoraExtra() {
        return horaExtra;
    }
    protected void setHoraExtra(boolean horaExtra){
        this.horaExtra = !horaExtra;
    }
    @Override
    public String toString() {
        return "Membro [email=" + email + ", funcao=" + funcao + ", horaExtra=" + horaExtra + ", nome="
                + nome + "]";
    }
}