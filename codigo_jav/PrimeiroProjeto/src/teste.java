import java.util.Scanner;

public class teste {

    // Soma iterativa do vetor
    public static int somaIterativa(int[] vetor) {
        int soma = 0;
        for (int i = 0; i < vetor.length; i++) {
            soma += vetor[i];
        }
        return soma;
    }

    // Soma recursiva do vetor
    public static int somaRecursiva(int[] vetor, int indice) {
        if (indice >= vetor.length) {
            return 0;
        } else {
            return vetor[indice] + somaRecursiva(vetor, indice + 1);
        }
    }

    // Cria vetor de números inteiros
    public static void main(String[] args) {

        int tamanho;

        Scanner scanner = new Scanner(System.in);

        // Define o numero de elementos que irão compor o vetor
        System.out.println("Quantos elementos terá o vetor: ");
        tamanho = scanner.nextInt();

        // Cria o vetor com o tamanho fornecido 
        int[] vetor = new int[tamanho];

        // Imput de valor que irá compor o vetor
        for (int i = 0; i < vetor.length; i++) {
            System.out.println("Digite o número inteiro na posição " + i + ": ");
            vetor[i] = scanner.nextInt();
        }
        for(int i = 0; i < vetor.length ; i++){
                    System.out.print(vetor[i]+" ");
        }
        System.out.println();
        // Chamada do método iterativo
        int somaIterativa = somaIterativa(vetor);
        System.out.println("A soma dos números inteiros de forma iterativa é: " + somaIterativa);

        // Chamada do método recursivo
        int somaRecursiva = somaRecursiva(vetor, 0);
        System.out.println("A soma dos números inteiros de forma recursiva é: " + somaRecursiva);
        scanner.close();
    }
}