import java.util.*;
import java.io.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        String st[] = s.split("");
        
        String left[] = new String[100000];
        int n =0;
        String pre="";
        for(int i=0; i<st.length; i++) {
            
            if(st[i].equals("(")) {
                left[n] = "(";
                n++;
            }
            else {
                if(n==0) {
                    answer = false;
                    break;
                }
                if(left[n-1].equals("(")){
                    n--;
                }
                
            }
            
        }
        
        if(n !=0) answer = false;
        
        return answer;
    }
}