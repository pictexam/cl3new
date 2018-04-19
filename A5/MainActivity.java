package com.example.assignment.calculator_app;

import android.content.Context;
import android.content.res.AssetManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    Button addd, sub, mul, div, tan, sin, cos, sqrt, clear, save, recall, fileread;
    TextView res;

    EditText num1, num2;
    double saved_value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }
    public void init(){
        addd=findViewById(R.id.add);
        //addd=findViewById(R.id.add);
        sub=findViewById(R.id.sub);
        mul=findViewById(R.id.mul);
        div=findViewById(R.id.div);
        sin=findViewById(R.id.sin);
        res=findViewById(R.id.res);
        recall=findViewById(R.id.recall);
        save=findViewById(R.id.save);
        fileread=findViewById(R.id.fileread);
        saved_value=0;
        num1=findViewById(R.id.num1);
        num2=findViewById(R.id.num2);
        recall.setOnClickListener(this);
        sub.setOnClickListener(this);
        addd.setOnClickListener(this);
        div.setOnClickListener(this);
        sin.setOnClickListener(this);
        save.setOnClickListener(this);
        fileread.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        String numb1=num1.getText().toString();
        String numb2=num2.getText().toString();
        switch (v.getId()){
            case R.id.add:
                try {
                    double ansadd = Double.parseDouble(numb1) + Double.parseDouble(numb2);
                    res.setText(String.valueOf(ansadd));
                }
                catch (Exception e){
                    e.printStackTrace();

                }
                break;
            case R.id.div:
                try {
                    BigDecimal n1 = new BigDecimal(Double.parseDouble(numb1));
                    BigDecimal n2 = new BigDecimal(Double.parseDouble(numb2));
                    BigDecimal ansdiv = n1.divide(n2, 5, BigDecimal.ROUND_HALF_UP);
                    res.setText(String.valueOf(ansdiv));
                }
                catch (Exception e){
                    e.printStackTrace();
                }
                break;
            case R.id.sin:
                double anssin=Math.sin(Double.parseDouble(numb1));
                res.setText(String.valueOf(anssin));
                break;
            case R.id.save:
                try{
                    String value=res.getText().toString();
                    saved_value=Double.parseDouble(value);
                    num1.setText("");
                    num2.setText("");
                    res.setText("Result");
                }
                catch (Exception e){
                    e.printStackTrace();
                }
                break;
            case R.id.recall:
                num1.setText(String.valueOf(saved_value));
                break;
            case R.id.fileread:
                try{
                    AssetManager am=this.getAssets();
                    InputStream is=am.open("filedata.txt");
                    BufferedReader buf=new BufferedReader(new InputStreamReader(is));
                    String n1=buf.readLine();
                    String n2=buf.readLine();
                    num1.setText(n1);
                    num2.setText(n2);
                }
                catch (Exception e){
                    e.printStackTrace();
                    break;
                }

        }
    }
}
