import java.util.Scanner;

public class MatrixDeterminant {
    
    // Method to calculate the determinant of a matrix
    public static double calculateDeterminant(double[][] matrix) {
        int n = matrix.length;

        // Base case for 1x1 matrix
        if (n == 1) {
            return matrix[0][0];
        }
        
        // Base case for 2x2 matrix
        if (n == 2) {
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
        }

        // Recursive case: Calculate determinant using cofactor expansion
        double determinant = 0;
        for (int col = 0; col < n; col++) {
            double[][] subMatrix = createSubMatrix(matrix, 0, col);
            determinant += Math.pow(-1, col) * matrix[0][col] * calculateDeterminant(subMatrix);
        }
        return determinant;
    }

    // Helper method to create a submatrix by removing specified row and column
    private static double[][] createSubMatrix(double[][] matrix, int excludingRow, int excludingCol) {
        int n = matrix.length;
        double[][] subMatrix = new double[n - 1][n - 1];
        int r = -1;
        
        for (int i = 0; i < n; i++) {
            if (i == excludingRow)
                continue;
            r++;
            int c = -1;
            for (int j = 0; j < n; j++) {
                if (j == excludingCol)
                    continue;
                subMatrix[r][++c] = matrix[i][j];
            }
        }
        return subMatrix;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the dimension of the matrix (n for nxn): ");
        int n = scanner.nextInt();

        double[][] matrix = new double[n][n];
        System.out.println("Enter the elements of the matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = scanner.nextDouble();
            }
        }

        double determinant = calculateDeterminant(matrix);
        System.out.println("The determinant of the matrix is: " + determinant);
        scanner.close();
    }
}
