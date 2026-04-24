public class Contador{ 
    public static void main(String[] args){
        int n2 = 1;
        int n3 = 1;

        for(int n1 = 1; n1 <= 3; n1++){
         System.out.println("Usando o For");
         System.out.println(n1);
        }

        while (n2 <= 3){
            System.out.println("Usando o while");
            System.out.println(n2);
            n2++;
        }

        do { 
            System.out.println("Usando o Do");
            System.out.println(n3);    
        } while (n3 <= 3);        
    }
}