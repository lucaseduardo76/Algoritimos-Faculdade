import java.util.Scanner;

public class ex04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cont = 1;
        String cor;
        
        System.out.println("Iremos fabricar sua porta!");
        int choose = 0;
        while(choose > 4 && choose < 1){
            System.out.println("Digite por favor a cor da porta \n 1º Azul \n 2° Verde \n 3° Preto \n 4° Branco");
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

        System.out.println("Agora vamos as dimensões: \n Digite por favor o comprimento: ");
        int comp = sc.nextInt();
        System.out.println("Agora a largura: ");
        int esp = sc.nextInt();
        int larg = sc.nextInt();
        System.out.println("Agora a espessura");
        
        Porta porta = new Porta(cor, comp, larg, esp);
        
        while(cont == 1){

            
            
        }
        sc.close();
    }
}

class Porta{
    boolean aberta = false;
    String cor;
    double dimensaoX, dimensaoY, dimensaoZ;

    public Porta(String cor, double dimensaoX, double dimensaoY, double dimensaoZ){
        this.cor = cor;
        this.dimensaoX = dimensaoX;
        this.dimensaoY = dimensaoY;
        this.dimensaoZ = dimensaoZ;
    }

    boolean abre(){
        boolean i = this.aberta ? false : true;
        this.aberta = true;
        return i;
    }

    boolean fecha(){
        boolean i = this.aberta ? true : false;
        this.aberta = false;
        return i;
    }

    void pintar(String cor){
        this.cor = cor;
    }
    boolean estaAberta(){
        return this.aberta;
    }    
}