// CodeEval Longest Word
//https://www.codeeval.com/open_challenges/111/

package longestword;

public class LongestWord {

    public static void main(String[] args) {
        String line = "another line another";
        
        String[] sep = line.split(" ");
        String longest = sep[0];
        for (int i = 0; i < sep.length; i++) {
            if(longest.length()<sep[i].length()){
                longest = sep[i];
            }
        }
        System.out.println(longest);
        
        
        
    }
    
}
