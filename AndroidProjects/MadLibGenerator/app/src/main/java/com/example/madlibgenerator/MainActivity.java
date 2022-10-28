package com.example.madlibgenerator;

//Setting visibility of widgets - https://stackoverflow.com/questions/7348150/android-why-setvisibilityview-gone-or-setvisibilityview-invisible-do-not

//Setting the edit text hint - https://stackoverflow.com/questions/9153213/programmatically-set-edit-text-hint-in-android

//Where I got my madlibs - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.happinessishomemade.net%2Fhalloween-mad-libs-printable%2F&psig=AOvVaw0IRZDaz2ZECaWwbrkmCAYL&ust=1666465414842000&source=images&cd=vfe&ved=2ahUKEwjBzfbJgfL6AhUEQUIHHVLuAigQr4kDegUIARDUAQ


import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    EditText question1, question2, question3, question4, question5, question6, question7, question8;
    Button MadLib1, MadLib2, MadLib3, randomMadLib, submitBTN, resetBTN;
    TextView output;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        question1 = findViewById(R.id.question1);
        question2 = findViewById(R.id.question2);
        question3 = findViewById(R.id.question3);
        question4 = findViewById(R.id.question4);
        question5 = findViewById(R.id.question5);
        question6 = findViewById(R.id.question6);
        question7 = findViewById(R.id.question7);
        question8 = findViewById(R.id.question8);
        submitBTN = findViewById(R.id.submitBTN);
        output = findViewById(R.id.output);
        MadLib1 = findViewById(R.id.MadLib1);
        MadLib2 = findViewById(R.id.MadLib2);
        MadLib3 = findViewById(R.id.MadLib3);
        randomMadLib = findViewById(R.id.randomMadLib);
        resetBTN = findViewById(R.id.resetBTN);


        question1.setVisibility(View.INVISIBLE);
        question2.setVisibility(View.INVISIBLE);
        question3.setVisibility(View.INVISIBLE);
        question4.setVisibility(View.INVISIBLE);
        question5.setVisibility(View.INVISIBLE);
        question6.setVisibility(View.INVISIBLE);
        question7.setVisibility(View.INVISIBLE);
        question8.setVisibility(View.INVISIBLE);
        submitBTN.setVisibility(View.INVISIBLE);
        output.setVisibility(View.INVISIBLE);
        resetBTN.setVisibility(View.INVISIBLE);




//        submitBTN.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) { submit();
//
//            }
//        });

        MadLib1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MadLib1();
            }
        });

        MadLib2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MadLib2();
            }
        });

        MadLib3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MadLib3();
            }
        });

        randomMadLib .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                randomMadLib();
            }
        });

        resetBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reset();
            }
        });
    }

    private void MadLib1() {
        question1.setHint("give me a plural noun");
        question2.setHint("give me a  plural noun");
        question3.setHint("give me a noun");
        question4.setHint("give me a noun");
        question5.setHint("give me a noun");
        question6.setHint("give me a plural noun");
        question7.setHint("give me a adjective");
        question8.setHint("give me a noun");

        question1.setVisibility(View.VISIBLE);
        question2.setVisibility(View.VISIBLE);
        question3.setVisibility(View.VISIBLE);
        question4.setVisibility(View.VISIBLE);
        question5.setVisibility(View.VISIBLE);
        question6.setVisibility(View.VISIBLE);
        question7.setVisibility(View.VISIBLE);
        question8.setVisibility(View.VISIBLE);
        submitBTN.setVisibility(View.VISIBLE);
        output.setVisibility(View.VISIBLE);
        MadLib1.setVisibility(View.INVISIBLE);
        MadLib2.setVisibility(View.INVISIBLE);
        MadLib3.setVisibility(View.INVISIBLE);
        randomMadLib.setVisibility(View.INVISIBLE);

        submitBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                resetBTN.setVisibility(View.VISIBLE);
                output.setText(String.format("Halloween is my favorite holiday, because we get to dress up in " +
                        "%s and visit %s in our %s saying '%s or %s!' in exchange for a bag of %s. It's so %s! My favorite candy is %s", question1.getText(), question2.getText(), question3.getText(), question4.getText(), question5.getText(), question6.getText(), question7.getText(), question8.getText()));
            }
        });
    }

        private void MadLib2() {
            question1.setHint("give me an adjective");
            question2.setHint("give me a  noun");
            question3.setHint("give me an adjective");
            question4.setHint("give me an adjective");
            question5.setHint("give me a plural noun");
            question6.setHint("give me a plural noun");
            question7.setHint("give me a adjective");
            question8.setHint("give me a noun");

            question1.setVisibility(View.VISIBLE);
            question2.setVisibility(View.VISIBLE);
            question3.setVisibility(View.VISIBLE);
            question4.setVisibility(View.VISIBLE);
            question5.setVisibility(View.VISIBLE);
            question6.setVisibility(View.VISIBLE);
            question7.setVisibility(View.VISIBLE);
            question8.setVisibility(View.VISIBLE);
            submitBTN.setVisibility(View.VISIBLE);
            output.setVisibility(View.VISIBLE);
            MadLib1.setVisibility(View.INVISIBLE);
            MadLib2.setVisibility(View.INVISIBLE);
            MadLib3.setVisibility(View.INVISIBLE);
            randomMadLib.setVisibility(View.INVISIBLE);

            submitBTN.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    resetBTN.setVisibility(View.VISIBLE);
                    output.setText(String.format("This Year, I'm going to dress up as a(n) %s %s. My costume is going to be so %s! It will be made with %s " +
                            "%s and %s, so it's sure to win the %s %s contest!", question1.getText(), question2.getText(), question3.getText(), question4.getText(), question5.getText(), question6.getText(), question7.getText(), question8.getText()));
                }
            });
        }
            private void MadLib3() {
                question1.setHint("give me a plural noun");
                question2.setHint("give me a  plural noun");
                question3.setHint("give me a adverb");
                question4.setHint("give me a verb");
                question5.setHint("give me a noun");
                question6.setHint("give me a noun");
                question7.setHint("give me a noun");
                question8.setHint("give me a verb ending in s");

                question1.setVisibility(View.VISIBLE);
                question2.setVisibility(View.VISIBLE);
                question3.setVisibility(View.VISIBLE);
                question4.setVisibility(View.VISIBLE);
                question5.setVisibility(View.VISIBLE);
                question6.setVisibility(View.VISIBLE);
                question7.setVisibility(View.VISIBLE);
                question8.setVisibility(View.VISIBLE);
                submitBTN.setVisibility(View.VISIBLE);
                output.setVisibility(View.VISIBLE);
                MadLib1.setVisibility(View.INVISIBLE);
                MadLib2.setVisibility(View.INVISIBLE);
                MadLib3.setVisibility(View.INVISIBLE);
                randomMadLib.setVisibility(View.INVISIBLE);

                submitBTN.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        resetBTN.setVisibility(View.VISIBLE);
                        output.setText(String.format("I also love to carve %s for Halloween! I use special carving %s to %s %s a face into my %s." +
                                "Then, we put a %s inside and light it so that the %s %s! Spooky!", question1.getText(), question2.getText(), question3.getText(), question4.getText(), question5.getText(), question6.getText(), question7.getText(), question8.getText()));
                    }
                });
            }
        private void randomMadLib() {
            question1.setHint("give me a plural noun");
            question2.setHint("give me a  plural noun");
            question3.setHint("give me a noun");
            question4.setHint("give me a noun");
            question5.setHint("give me a noun");
            question6.setHint("give me a plural noun");
            question7.setHint("give me a adjective");
            question8.setHint("give me a noun");

            question1.setVisibility(View.VISIBLE);
            question2.setVisibility(View.VISIBLE);
            question3.setVisibility(View.VISIBLE);
            question4.setVisibility(View.VISIBLE);
            question5.setVisibility(View.VISIBLE);
            question6.setVisibility(View.VISIBLE);
            question7.setVisibility(View.VISIBLE);
            question8.setVisibility(View.VISIBLE);
            submitBTN.setVisibility(View.VISIBLE);
            output.setVisibility(View.VISIBLE);
            MadLib1.setVisibility(View.INVISIBLE);
            MadLib2.setVisibility(View.INVISIBLE);
            MadLib3.setVisibility(View.INVISIBLE);
            randomMadLib.setVisibility(View.INVISIBLE);

            submitBTN.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String[] MadLibs = {"Halloween is my favorite holiday, because we get to dress up in " +
                    "%s and visit %s in our %s saying '%s or %s!' in exchange for a bag of %s. It's so %s! My favorite candy is %s", "This Year, I'm going to dress up as a(n) %s %s. My costume is going to be so %s! It will be made with %s " +
                    "%s and %s, so it's sure to win the %s %s contest!", "I also love to carve %s for Halloween! I use special carving %s to %s %s a face into my %s." +
                    "Then, we put a %s inside and light it so that the %s %s! Spooky!"};
                    Random rand = new Random();
                    resetBTN.setVisibility(View.VISIBLE);
                    output.setText(String.format(MadLibs[rand.nextInt(3)],question1.getText(), question2.getText(), question3.getText(), question4.getText(), question5.getText(), question6.getText(), question7.getText(), question8.getText()));
                }
            });
        }
            private void reset(){
                question1.setVisibility(View.INVISIBLE);
                question2.setVisibility(View.INVISIBLE);
                question3.setVisibility(View.INVISIBLE);
                question4.setVisibility(View.INVISIBLE);
                question5.setVisibility(View.INVISIBLE);
                question6.setVisibility(View.INVISIBLE);
                question7.setVisibility(View.INVISIBLE);
                question8.setVisibility(View.INVISIBLE);
                submitBTN.setVisibility(View.INVISIBLE);
                output.setVisibility(View.INVISIBLE);
                MadLib1.setVisibility(View.VISIBLE);
                MadLib2.setVisibility(View.VISIBLE);
                MadLib3.setVisibility(View.VISIBLE);
                randomMadLib.setVisibility(View.VISIBLE);
                resetBTN.setVisibility(View.INVISIBLE);


                question1.setText("");
                question2.setText("");
                question3.setText("");
                question4.setText("");
                question5.setText("");
                question6.setText("");
                question7.setText("");
                question8.setText("");
                output.setText("output");

            }


        //private void submit() {
//            output.setText(String.format("Halloween is my favorite holiday, because we get to dress up in " +
//                    "%s and visit %s in our %s saying '%s or %s!' in exchange for a bag of %s. It's so %s! My favorite candy is %s", question1.getText(),question2.getText(),question3.getText(),question4.getText(),question5.getText(),question6.getText(),question7.getText(),question8.getText()));
        //}

}