import java.util.Scanner;

public class ex04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cont = 1;
        String cor;
        
        System.out.println("Iremos fabricar sua porta!");
        int choose = 0;
        while(choose > 4 || choose < 1){
            System.out.println("Digite por favor a cor da porta \n1º Azul \n2° Verde \n3° Preto \n4° Branco");
            choose = sc.nextInt();
        }
        switch(choose){
            case 1:
                cor = "Azul";
                break;
            case 2:
                cor = "Verde";
                break;
            case 3:
                cor = "Preto";
                break;
            case 4:
                cor = "Branco";
                break;  
            default:
                cor = "Cinza";               
        }   

        System.out.println("Agora vamos as dimensões: \nDigite por favor o comprimento: ");
        float comp = sc.nextFloat();
        System.out.println("Agora a largura: ");
        float larg = sc.nextFloat();
        System.out.println("Agora a espessura");
        float esp = sc.nextFloat();
        
        Porta porta = new Porta(cor, comp, larg, esp);
        
        while(cont == 1){
            System.out.println("As informações da porta são: \nCor: "+ porta.getCor() + "\nComprimento: " +porta.getDimensaoY() +"\nLargura: "+ porta.getDimensaoX()+ "\nEspessura: "+porta.getDimensaoZ());
            
            cont = 0;
        }
        sc.close();
    }
}

class Porta{
    boolean aberta = false;
    String cor;
    float dimensaoX, dimensaoY, dimensaoZ;

    public Porta(String cor, float dimensaoX, float dimensaoY, float dimensaoZ){
        this.cor = cor;
        this.dimensaoX = dimensaoX;
        this.dimensaoY = dimensaoY;
        this.dimensaoZ = dimensaoZ;
    }

    public boolean abre(){
        boolean i = this.aberta ? false : true;
        this.aberta = true;
        return i;
    }

    public boolean fecha(){
        boolean i = this.aberta ? true : false;
        this.aberta = false;
        return i;
    }

    public void pintar(String cor){
        this.cor = cor;
    }
    public boolean estaAberta(){
        return this.aberta;
    }  
    
    public String getCor() {
        return this.cor;
    }
    public float getDimensaoY() {
        return dimensaoY;
    }
    public float getDimensaoX() {
        return dimensaoX;
    }
    public float getDimensaoZ() {
        return dimensaoZ;
    }
}