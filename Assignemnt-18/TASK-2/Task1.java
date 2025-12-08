public class Task1 {

    /**
     * Checks if a number is positive, negative, or zero.
     * @param num the number to check
     */
    public static void checkNumber(int num) {

        if (num > 0) {
            System.out.println("The number is positive");
        } else if (num < 0) {
            System.out.println("The number is negative");
        } else {
            System.out.println("The number is zero");
        }
    }


    public static void main(String[] args) {
        // Test with different inputs
        checkNumber(-5);   // Output: The number is negative
        checkNumber(0);    // Output: The number is zero
        checkNumber(7);    // Output: The number is positive
    }
}
