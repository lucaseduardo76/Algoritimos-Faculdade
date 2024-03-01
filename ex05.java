public class ex05 {
    
}

class Conta{
    private String nome, data_abertura, senha;
    private int numero_conta, agencia;
    private double saldo;

    public Conta(String nome, String data_abertura, String senha, int numero_conta, int agencia, double saldo){
        this.nome = nome;
        this.data_abertura = data_abertura;
        this.senha = senha;
        this.numero_conta = numero_conta;
        this.agencia = agencia;
        this.saldo = saldo;
    }

    public String getNome(){
        return this.nome;
    }
    public void setNome(String i){
        this.nome = i;
    }

    public String getDataAbertura(){
        return this.data_abertura;
    }
    public void setDataAbertura(String i){
        this.data_abertura = i;
    }

    public int getNumeroConta(){
        return this.numero_conta;
    }
    public void setNumeroConta(int i){
        this.numero_conta = i;
    }

    public int getAgencia() {
        return agencia;
    }
    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }

    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getSenha() {
        return senha;
    }
    public void setSenha(String senha) {
        this.senha = senha;
    }
}

/*
 * - Nome
 * - Numero da conta
 * - Agencia
 * - Saldo
 * - Data de abertura
 * 
 * Açoes:
 * Sacar
 * Depositar
 * Calcular redimento mensal
 * Investir (calcular rendimento)
 */
