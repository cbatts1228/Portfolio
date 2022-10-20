import java.util.Scanner;
import java.util.Random;
import java.lang.Math;

public class BasicMathQuiz {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        Random rand = new Random();
        double answer=0.0;
        double input=0.0;
        int questions = 0;
        int percentage = 0;
        double score = 0.0;
        
        while(percentage<80 || questions<10){
            int num1 = (int)(Math.random()*100);
            int num2 = rand.nextInt(100)+1;     //1-100
            int signNumber = rand.nextInt(4);   //0-3
            if(signNumber==0){
                System.out.printf("What is %d / %d? ",num1,num2);
                answer = Math.round((double)num1/num2*100.0)/100.0;
            }
            else if(signNumber==1){
                System.out.printf("What is %d * %d? ",num1,num2);
                answer = (int)num1*num2;
            }
            else if(signNumber==2){
                System.out.printf("What is %d + %d? ",num1,num2);
                answer = (int)num1+num2;
            }
            else{
                System.out.printf("What is %d - %d? ",num1,num2);
                answer = (int)num1-num2;
            }
            input = ui.nextDouble();
            
            //check to see if the user answered the expression correctly
            if(input==answer){
                System.out.println("Great job! You can do basic math!");
                score++;
            }
            else{
                System.out.printf("skill issue, the answer is %f ",answer);
                System.out.println();
            }
            //output their points
            questions++;
            percentage = (int)((score/questions)*100);
            System.out.println("You got "+percentage+"% out of "+questions);
            
        }
    }
}