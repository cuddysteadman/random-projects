public class RandomFunctionGenerator {
    public static final String[] functions = {"ln", "sin", " * ", " / ", "sqrt", "e^", "^"};
    public static final int[] numbers = {2, 3, 4, 5, 6, 7, 8, 9, 10};
    public static void main(String[] args) {
        randomFunction();
    }
    public static void randomFunction() {
        String toPrint = "Error";
        if ((int) (Math.random() * 2) == 0) {
            String numerator = "" + functions[(int) (Math.random() * functions.length)] + "(";
            String denominator = "" + functions[(int) (Math.random() * functions.length)] + "(";
            if (numerator.equals("^(") || numerator.equals(" * (") || numerator.equals(" / (")) {
                numerator = "" + numbers[(int) (Math.random() * numbers.length)] + numerator;
            } if (denominator.equals("^(") || denominator.equals(" * (") || denominator.equals(" / (")) {
                denominator = "" + numbers[(int) (Math.random() * numbers.length)] + denominator;
            }
            for (int i = 0; i < ((int) (Math.random() * 3)); i++) {
                numerator += "" + numbers[(int) (Math.random() * numbers.length)];
            }
            numerator += "x)";
            for (int i = 0; i < ((int) (Math.random() * 3)); i++) {
                denominator += "" + numbers[(int) (Math.random() * numbers.length)];
            }
            denominator += "x)";
            if (numerator.length() < denominator.length()) {
                if ((denominator.length() - numerator.length()) % 2 == 0) {
                    for (int i = 0; i < (denominator.length() - numerator.length()) / 2; i++) {
                        System.out.print(" ");
                    }
                } else {
                    for (int i = 0; i < (denominator.length() - numerator.length()) / 2 + 1; i++) { // the +1 is simply a matter of preference; you won't always be perfect
                        System.out.print(" ");
                    }
                }
            }
            System.out.println("(" + numerator + ")");
            for (int i = 0; i < Math.max(numerator.length(), denominator.length()) + 2; i++) {
                System.out.print("-");
            }
            System.out.println();
            if (denominator.length() < numerator.length()) {
                if ((numerator.length() - denominator.length()) % 2 == 0) {
                    for (int i = 0; i < (numerator.length() - denominator.length()) / 2; i++) {
                        System.out.print(" ");
                    }
                } else {
                    for (int i = 0; i < (numerator.length() - denominator.length()) / 2 + 1; i++) { // the +1 is simply a matter of preference; you won't always be perfect
                        System.out.print(" ");
                    }
                }
            }
            System.out.println("(" + denominator + ")");
            return;
        }
        String numerator = "" + functions[(int) (Math.random() * functions.length)] + "(";
        if (numerator.equals("^(") || numerator.equals(" * (") || numerator.equals(" / (")) {
            numerator = "" + numbers[(int) (Math.random() * numbers.length)] + numerator;
        }
        for (int i = 0; i < ((int) (Math.random() * 3)); i++) {
            numerator += "" + numbers[(int) (Math.random() * numbers.length)];
        }
        numerator += "x)";
        System.out.println(numerator);
    }
}
