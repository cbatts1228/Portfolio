import java.util.Scanner;
import java.util.Random;

public class BattsPasswordGenerator{
    public static void main(String[] args){
        Scanner ui = new Scanner(System.in);
        System.out.println("Passsword MUST be 8 characters long and have at least 1 letter, number, and special character");
        System.out.println("How many characters do you want?");
        int characters = ui.nextInt();
        System.out.println("How many numbers do you want?");
        int numbers = ui.nextInt();
        System.out.println("How many special characters do you want?");
        int specialChar = ui.nextInt();
        int length = characters+numbers+specialChar;
        String password = "";
        Random r = new Random();

        while(length != 8 || characters<1 || numbers<1 || specialChar<1){
            System.out.println("Password did not minimum requirements");
            System.out.println("How many characters do you want?");
            characters = ui.nextInt();
            System.out.println("How many numbers do you want?");
            numbers = ui.nextInt();
            System.out.println("How many special characters do you want?");
            specialChar = ui.nextInt();
            length = characters+numbers+specialChar;
        }

        for(int i=0;i<characters;i++){
            int charType = r.nextInt(2);
            if(charType == 0){
                // got random letter from ascii table code from https://stackoverflow.com/questions/2626835/is-there-functionality-to-generate-a-random-character-in-java
                char c = (char)(r.nextInt(26) + 'a');
                String s = Character.toString(c);
                password = password+s;
            }
            else{
                char c = (char)(r.nextInt(26) + 'A');
                String s = Character.toString(c);
                password = password+s;
            }
        }
        for(int i=0;i<numbers;i++){
            int num = r.nextInt(10);
            String n = Integer.toString(num);
            password= password+n;
        }

        for(int i=0;i<specialChar;i++){
            String specialCharacters="! @$%^&*()_-+={[}]|:;'<,>.?";
            //grabbing random item from string code from https://beginnersbook.com/2013/12/java-string-charat-method-example/
            char ch = specialCharacters.charAt(r.nextInt(specialCharacters.length()));
            String sp = Character.toString(ch);
            password = password+sp;

        }

        System.out.println(password);

        
    }

    
}