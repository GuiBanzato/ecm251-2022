//Guilherme Lins Banzato RA: 20.01561-5

import java.util.concurrent.ThreadLocalRandom;

public class Veiculos {
    private String modelo;
    private int Custo;
    protected int ID;

    public Veiculos(int Custo, String modelo) {
        this.Custo = Custo;
        this.modelo = modelo;
        GerarID();
    }

    public int getCusto() {
        return Custo;
    }

    public String getModelo() {
        return modelo;
    }

    public void testar(){
        System.out.println("ID: "+ ID + ", custo por hora: "+ Custo);
    }

    public void GerarID(){
        this.ID = ThreadLocalRandom.current().nextInt(10000,99999);
    }


    @Override
    public String toString() {
        return "Veículo: (Custo:" + Custo + ", ID:" + ID + ", Modelo:" + modelo + ")";
    }


}