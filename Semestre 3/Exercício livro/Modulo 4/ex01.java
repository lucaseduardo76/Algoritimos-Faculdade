public class ex01{
    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        for(int i = 1; i<= 6; i++){
            System.out.println(fibonacci.calcularFibonacci(i));
        }
    }
}

class Fibonacci{
    int calcularFibonacci(int i){
        if(i <= 1){
            return 0;
        }else if(i <= 2){
            return 1;
        }else{
            return calcularFibonacci(i - 2) + calcularFibonacci(i - 1);
        }
    }
}