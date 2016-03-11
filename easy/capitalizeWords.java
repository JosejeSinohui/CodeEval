//Code Eval - CapitalizeWords
//https://www.codeeval.com/open_challenges/93/

package capitalizewords;

public class CapitalizeWords {

    public static void main(String[] args) {
        String line = "Hello world";
        String[] palabras = line.split(" ");
        String finished = "";
        for (int i = 0; i < palabras.length; i++) {
            String[] letras = palabras[i].split("");
            for (int j = 0; j < letras.length; j++) { 
                if(j==0){
                    finished = finished + letras[j].toUpperCase();
                    
                }
                else{
                    finished = finished + letras[j];
                }
                
            }
            finished = finished + " ";
            
        }
        System.out.println(finished);
    }
    
}
