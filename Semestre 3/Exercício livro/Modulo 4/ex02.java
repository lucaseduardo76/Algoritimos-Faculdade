public class ex02{
    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        for(int i = 1; i<= 3; i++){
            System.out.println(fibonacci.calcularFibonacci(i));
        }
    }
}

class Fibonacci{
    int calcularFibonacci(int i){
        return i <= 1 ? 0 : calcularFibonacci(i - 2) + calcularFibonacci(i - 1);
    }
}