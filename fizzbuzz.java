import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.Charset;
import java.util.List;
import static java.lang.Integer.parseInt;

public class Main {

    public static boolean multiple(int x, int y) {
        return x % y == 0;
    }

    public static void fizzbuzz(int a, int b, int n) {
        for(int i = 1; i <= n; i++) {
            boolean fizz = multiple(i, a);
            boolean buzz = multiple(i, b);

            if(fizz && buzz) {
                System.out.print("FB");
            } else if(fizz) {
                System.out.print("F");
            } else if(buzz) {
                System.out.print("B");
            } else {
                System.out.print(i);
            }

            if(i < n) {
                System.out.print(" ");
            }
        }

        System.out.println();
    }

    public static void main(String[] args) throws Exception {
        String filename = args[0];

        Path file = Paths.get(filename);
        Charset charset = Charset.forName("US-ASCII");

        List<String> lines = Files.readAllLines(file, charset);
        for (String line : lines) {
            String[] parts = line.split(" ");
            fizzbuzz(parseInt(parts[0]), parseInt(parts[1]), parseInt(parts[2]));
        }
    }
}
