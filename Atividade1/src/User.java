//Guilherme Lins Banzato RA: 20.01561-5

public class User {
    private String name;
    private Veiculos veículos;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Veiculos getVeiculos() {
        return veículos;
    }

    public void setVeiculos(Veiculos veículos) {
        this.veículos = veículos;
    }

    @Override
    public String toString() {
        return "Usuário: (" + name + ")";
    }

    public void aluga(Veiculos veículos){
        setVeiculos(veículos);
    }
    
}