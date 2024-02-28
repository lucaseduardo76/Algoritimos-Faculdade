public class ex03 {
   public static void main(String[] args) {
    Pessoa pessoa = new Pessoa("Lucas", 22);
    pessoa.aniversario();
   }
}

class Pessoa{
    private String nome;
    private int idade;

    Pessoa(String n, int i){
        this.nome = n;
        this.idade = i;
    }

    public int getIdade() {
        return idade;
    }

    public String getNome() {
        return nome;
    }

    public void setIdade(int i){
        this.idade = i;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void aniversario(){
        this.idade += 1;
        System.out.println("Parabens " + this.nome + " agora você tem "+ this.idade + " anos");
    }
}
