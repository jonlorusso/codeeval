
class Main {

    public static boolean isPrime(int x) {
        double sqr = Math.sqrt(x);

        for(int i = 2; i <= sqr; i++) {
           if(x % i == 0) {
               return false;
           }
        }

        return true;
    }

    public static void main(String[] args) {
        int sum = 0;
        int count = 0;
        int i = 2;

        while(count < 1000) {
            if(isPrime(i)) {
                sum += i;
                count++;
            }

            i++;
        }

        System.out.println(sum);
    }
}
